from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name="login"),
    path("<str:user_name>/", views.index, name="index"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("logcheck/", views.logcheck, name="logcheck"),
    path("errlogin/", views.errlogin, name="errlogin"),
    path("newuser/", views.newuser, name="newuser"),
    path("usercheck/", views.usercheck, name="usercheck"),
    path("erregister/", views.erregister, name="erregister"),
    path(
        "<str:user_name>/<int:problem_id>/",
        views.problem_details,
        name="problem_details",
    ),
    path(
        "<str:user_name>/<int:problem_id>/submit/", views.submission, name="submission"
    ),
]
