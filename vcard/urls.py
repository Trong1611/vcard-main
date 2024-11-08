from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from . import views
from vcard.views.landing import landing_view 
from vcard.views.authentication import login_view, register_view, reset_password_view, confirm_reset_password_view
from vcard.views.create_qr import create_qr_view
from vcard.views.user import list_vcard, delete_vcard
from vcard.views.style_qr import style_qr_view



app_name = 'vcard'
urlpatterns = [
    path('', landing_view),
    path('admin/', admin.site.urls),
    # create and style
    path('create/', create_qr_view),
    path('create/format', style_qr_view),

    # user_vcard interaction
    path('list', list_vcard),
    path('delete/<int:vcard_id>', delete_vcard, name='delete'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('reset-password/', reset_password_view, name='reset_password'),
    path('reset-password-confirm/<uuid:token>/', confirm_reset_password_view, name='confirm_reset_password'),
    # path('password_reset/done/', password_reset_done_view, name='password_reset_done'),
    # path('reset/done/', password_reset_complete_view, name='password_reset_complete'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]
