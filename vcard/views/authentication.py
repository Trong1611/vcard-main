from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def login_view(request):
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
                    return redirect("/vcard/create/format")
                else:
                    return redirect("/")
            else:
                error_message = "Sai tên đăng nhập hoặc mật khẩu."
    return render(request, 'vcard/login.html', {'error_message': error_message})
    # if request.method == 'POST':
    #     req = dict(request.POST)
    #     csrf_token, username, password, request_type,  = [i[0] for i in req.values()]
    #     email = username
    #     username = email.split("@")[0]
    #     if request_type == "signin":
    #         user = authenticate(request, username=email, password=password)
    #         if user is not None:
    #             login(request, user)
    #             if 'data' in request.session and len(request.session['data']) > 0:
    #                 return redirect("/vcard/create/format")
    #             else:
    #                 return redirect("/")
    #         else:
    #             return redirect('/vcard/login')
    #     elif request_type == "signup":
    #         user = User(username=username,
    #                     email=email,
    #                     password=password).save()
    #         login(request, user)
    #         return redirect('/')
    # return render(request, 'vcard/login.html')


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
    return render(request, "vcard/reset-password.html")
