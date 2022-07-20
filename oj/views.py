from django.shortcuts import render, get_object_or_404
from .models import Problem, Solution, TestCases, User
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
import os, filecmp
import sys

# Will point towards Login Pge
def login(request):

    return render(request, "oj/login.html")


# Will provide you a list of problems and direct to problem-desc page.
def index(request, user_name):
    user = get_object_or_404(User, pk=user_name)
    problems = Problem.objects.all()
    context = {"problems": problems, "user": user}
    return render(request, "oj/index.html", context)


# Details of the problem and submission page
def problem_details(request, user_name, problem_id):
    user = get_object_or_404(User, pk=user_name)
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {"problem": problem, "user": user}
    return render(request, "oj/details.html", context)


# This page accepts the submission code file and gives verdict of code submitted by
# comparing actual output with recieved output


def submission(request, user_name, problem_id):
    sol = request.FILES["solution"]
    with open("oj/Evaluation/sol.cpp", "wb+") as destination:
        for chunk in sol.chunks():
            destination.write(chunk)
    problem = get_object_or_404(Problem, pk=problem_id)
    user = get_object_or_404(User, pk=user_name)

    verdict = "ACCEPTED"
    sol = "oj/Evaluation/sol.cpp"
    inp = "oj/Evaluation/inp.txt"
    out = "oj/Evaluation/out.txt"
    actout = "oj/Evaluation/actout.txt"

    for testcase in problem.testcases_set.all():
        with open(inp, "w+") as destination:
            for i in testcase.input:
                destination.write(i)
        os.system("g++ oj/Evaluation/sol.cpp")
        os.system("a.exe <oj/Evaluation/inp.txt >oj/Evaluation/out.txt")
        with open(actout, "w+") as destination:
            for i in testcase.output:
                destination.write(i)
        if filecmp.cmp(out, actout, shallow=False):

            verdict = "ACCEPTED"

        else:

            verdict = "WRONG_ANSWER"
            break
    recent_solution = Solution()
    recent_solution.problem = Problem.objects.get(pk=problem_id)
    recent_solution.verdict = verdict
    recent_solution.submission_time = timezone.now()
    recent_solution.code_file = sol
    recent_solution.user = User.objects.get(pk=user_name)
    recent_solution.save()

    return HttpResponseRedirect(reverse("leaderboard"))


# Leaderboard page
def leaderboard(request):

    solutions = Solution.objects.all().order_by("submission_time").reverse()[:15]
    return render(request, "oj/leaderboard.html", {"solutions": solutions})


# This function checks whether after logging in the username and is correct or not
# if not then redirects to login page
def logcheck(request):

    user_name = request.POST["username"]
    pass_word = request.POST["password"]
    try:
        obj = User.objects.get(pk=user_name)

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("errlogin"))

    else:
        if obj.password == pass_word:

            return HttpResponseRedirect(
                reverse("index", kwargs={"user_name": user_name})
            )
        else:
            return HttpResponseRedirect(reverse("errlogin"))


# This is the redirected login page after entering wrong credentials
# with a warning
def errlogin(request):
    return render(request, "oj/errlogin.html")


# Registration page for newuser.
def newuser(request):
    return render(request, "oj/newuser.html")


# Checks if the username is already taken or not while entering in newusername.
def usercheck(request):

    username = request.POST["username"]
    password = request.POST["password"]
    try:
        obj = User.objects.get(pk=username)

    except User.DoesNotExist:
        user_a = User()
        user_a.username = username
        user_a.password = password
        user_a.save()
        return HttpResponseRedirect(reverse("login"))

    else:
        return HttpResponseRedirect(reverse("erregister"))


# Redirects to register page if username is already taken with a caution message.
def erregister(request):

    return render(request, "oj/erregister.html")
