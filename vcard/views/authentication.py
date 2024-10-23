from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from .models import User, Profile
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    error_message = None
    if request.method == 'POST':
        req = dict(request.POST)
        csrf_token, username, password, request_type = [i[0] for i in req.values()]
        email = username
        username = email.split("@")[0]
        if request_type == "signin":
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if 'data' in request.session and len(request.session['data']) > 0:
                    return redirect("/")
                else:
                    return redirect("/vcard/create/")
            else:
                error_message = "Sai tên đăng nhập hoặc mật khẩu."
    return render(request, 'vcard/login.html', {'error_message': error_message})

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email đã được đăng kí, Vui lòng sử dụng tài khoản khác.')
            return render(request, "vcard/register.html")
        user = User(email=email, username=email, password=make_password(password))
        user.save()
        login(request, user)
        return redirect('create/format')
    return render(request, "vcard/register.html")
    # if request.method == "POST":
    #     email = request.POST.get("email")
    #     password = make_password(request.POST.get("password"))
    #     user = User(email=email, username=email, password=password)
    #     user.save()
    #     login(request, user)
    #     return redirect('create/format')
    # return render(request, "vcard/register.html")


def reset_password_view(request):
    messages.get_messages(request).used = True
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            # Tạo một token cho người dùng
            token = str(uuid.uuid4())
            profile, created = Profile.objects.get_or_create(user=user)
            profile.reset_token = token  # Lưu token
            profile.save()

            # Gửi email thông báo
            reset_link = f"{request.scheme}://{request.get_host()}/vcard/reset-password-confirm/{token}/"
            send_mail(
                "Yêu cầu đặt lại mật khẩu",
                f"Bạn đã yêu cầu đặt lại mật khẩu. Nhấn vào liên kết này để đặt lại mật khẩu: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, "Đường dẫn đặt lại mật khẩu đã được gửi đến email của bạn.")
            return redirect('vcard:reset_password')
        except User.DoesNotExist:
            messages.error(request, "Email không tồn tại.")
            return redirect('vcard:reset_password')

    return render(request, 'vcard/reset_password.html')


def confirm_reset_password_view(request, token):
    profile = get_object_or_404(Profile, reset_token=token)

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Kiểm tra mật khẩu xác nhận
        if new_password == confirm_password:
            user = profile.user
            user.password = make_password(new_password)  # Mã hóa mật khẩu mới
            user.save()

            # Xóa token sau khi đổi mật khẩu
            profile.reset_token = None
            profile.save()

            # messages.success(request, "Mật khẩu của bạn đã được đặt lại thành công!")
            return redirect('/vcard/login/')  # Chuyển hướng tới trang đăng nhập
        else:
            messages.error(request, "Mật khẩu và xác nhận mật khẩu không khớp.")

    return render(request, 'vcard/reset_password_confirm.html', {'token': token})

# def password_reset_done_view(request):
#     return render(request, 'password_reset_done.html')

# def password_reset_complete_view(request):
#     return render(request, 'password_reset_complete.html')
