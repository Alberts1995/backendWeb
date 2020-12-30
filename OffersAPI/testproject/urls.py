"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import IndexView, SignInView, SingUPView, LogoutView, UserView, UsersView, MessageDeleteView, Offers, Excel_View


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("signin", SignInView.as_view(), name="signin"),
    path("signup", SingUPView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("users", UsersView.as_view(), name="users"),
    path("users/<str:username>", UserView.as_view(), name="user"),
    path("messages/<int:id>delete", MessageDeleteView.as_view(), name="message_delete"),
    path("offers", Offers.as_view(), name ="hu"),
    path('Excel', Excel_View.as_view(), name='export_users_csv'),
    #path("Excel", Excel_View.as_view(), name ="Excel")
]
