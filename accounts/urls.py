from django.urls import path
from .views import user_login , dashboard_view ,SignUpView ,  user_register , edit_user
from django.contrib.auth.views import LoginView , LogoutView  , PasswordChangeView , PasswordChangeDoneView  , \
PasswordResetDoneView , PasswordResetConfirmView , PasswordResetView , PasswordResetCompleteView 

urlpatterns = [
    # path("login/", user_login , name="login")
    path("login/", LoginView.as_view() , name="login") , 
    path("logout/", LogoutView.as_view() , name="logout"),
    path('password-change/' , PasswordChangeView.as_view() , name = 'password_change') ,
    path('password-change-done/' , PasswordChangeDoneView.as_view() , name ='password_change_done') ,
    path('password-reset/' , PasswordResetView.as_view() , name ='password_reset') ,
    path('password-reset/done/' , PasswordResetDoneView.as_view() , name ='password_reset_done') , 
    path('password-rest/<uidb64>/<token>/' , PasswordResetConfirmView.as_view() , name ='password_reset_confirm') ,
    path('password-rest/complete/' , PasswordResetCompleteView.as_view() , name ='password_reset_complete') ,
    path('profile/', dashboard_view , name="user_profile") , 
    path("signup/", user_register , name="user_register") ,
    path('profile/edit/' , edit_user , name = "edit_user_informations") ,
#   path("signup/", SignUpView.as_view() , name="user_register")
]