from django.contrib import admin
from django.urls import include, path
from oj import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("oj/leaderboard/", views.leaderboard, name="leaderboard"),
    path("oj/errlogin/", views.errlogin, name="errlogin"),
    path("oj/erregister/", views.erregister, name="erregister"),
    path("oj/usercheck/", views.usercheck, name="usercheck"),
    path("oj/newuser/", views.newuser, name="newuser"),
    path("oj/logcheck/", views.logcheck, name="logcheck"),
    path("oj/<str:user_name>/", views.index, name="index"),
    path("oj/", include("oj.urls")),
]
