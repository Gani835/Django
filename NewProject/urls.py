from django.urls import path
from .import views
urlpatterns=[
    path('usersignuppage',views.UserSignUpPage),
    path('backpage',views.BacktoPage),
    path('userloginpage',views.UserLoginPage),
    path('mainpage',views.MainPage),
    
    path('signingup',views.SigningUpPage),
    path('dropdown',views.dropdown),
    path('auth',views.Authentication,name='authent'),
    path('logout',views.userlogout),
    path('signup',views.UserSignUp,name='signup'),
    # From ecommerce app. . . .
    path('userloging',views.Authenticating),
    path('usersignup',views.SignUpPage),
    path('logoutpage',views.LogoutPage),
    path('homePage',views.EcommercePage),
]   