from django.urls import path

from app import views
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('home/',views.home_view),
	path('base/',views.base_view),
	path('profile/',views.profile_view),
	path('signup/',views.signup_view),
	path('activation/',views.activation_view),
	 path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',success_url='/app/password_changed_done/')),
	
	path('password_changed_done/',views.password_changed_done_view),
	path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password-reset/password_reset_form.html',
             subject_template_name='registration/password-reset/password_reset_subject.txt',
             email_template_name='registration/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]