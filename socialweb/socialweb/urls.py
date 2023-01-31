"""socialweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignupView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="login"),
    path("index",views.IndexView.as_view(),name="index"),
    path("post/addpost",views.PostAddView.as_view(),name="addpost"),
    path("posts/comments/add/<int:id>",views.add_comment,name="addcomment"),
    # path("posts/<int:id>/like",views.like_view,name="like"),
      path("answers/<int:id>/remove",views.remove_comment,name="remove-answer"),
      path("post/profile/<int:id>/remove",views.remove_post,name="remove-post"),
    path("post/profile",views.MypostView.as_view(),name="profile"),
    path("account/logout",views.signout_view,name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
