from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import subprocess, os
def smsAPI(request, number, message):
#     message = message.replace(" ", "%")
#     p1 = subprocess.Popen(['/home/pi/env/bin/python', '/home/pi/senior_project/sendSMS.py', number, message])
# #    print(message)
#     p1.wait()
#     if p1.returncode == 0:
#         return HttpResponse('Success')
#     else:
#         return HttpResponse('Failed')
    return HttpResponse('Success')