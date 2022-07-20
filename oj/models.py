from asyncio.windows_events import NULL
from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Problem(models.Model):
    Statement = models.TextField()
    Name = models.CharField(max_length=255)
    Level = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=NULL)

    verdict = models.CharField(max_length=255)
    submission_time = models.DateTimeField()
    code_file = models.TextField()

    def __str__(self):
        return self.problem.Name + " " + self.verdict


class TestCases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.input
