from django.urls import path

from blog.views import ProductFilter
from user.views import LogoutView, RegisterView, LoginView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view())

]



