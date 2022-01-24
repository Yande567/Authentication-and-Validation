from django.urls import path, include
from login import settings
from . import views
from django.contrib.auth import views as auth_views, logout

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    # path('forgot_password', views.forgot_password, name='forgot_password'),
    # path('change_password/<token>', views.change_password, name='change_password'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset', auth_views.PasswordResetView.as_view(
        template_name='authentication/password/password_reset.html'), name="password_reset"),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password/password_reset_complete.html'),
         name='password_reset_complete'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),

]
