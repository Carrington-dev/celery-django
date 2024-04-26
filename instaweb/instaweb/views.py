from django.shortcuts import render
from django.http import JsonResponse

from instaweb.tasks import send_feedback_email_task

def home(request):
    send_feedback_email_task.delay()
    # send_feedback_email_task.delay(5)
    return JsonResponse({
        "message":"I am alive"
    })