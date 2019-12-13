from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, HttpResponse
import requests
import json
import openpyxl
import re
import smtplib, ssl

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "projectsmy77@gmail.com"
            receiver_email = str(form.cleaned_data.get('email'))
            password = "proj123ects123"
            message = """\
            Welcome to E-repute! 
            You have successfully registered """+username+"!"
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def restPass(request):
    return render(request,'users/forgot-password.html')

#     from django.shortcuts import render, redirect
# from .forms import UserRegisterForm
# from django.contrib import messages
# from django.shortcuts import render, HttpResponse
# import requests
# import json
# import openpyxl
# import re

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

