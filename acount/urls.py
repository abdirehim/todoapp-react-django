from django.contrib import admin
from django.urls import path

from acount import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view()),
]

