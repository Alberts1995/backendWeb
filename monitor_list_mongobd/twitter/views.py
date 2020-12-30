from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import Message
import requests
import datetime
from datetime import  date
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from .models import Posts, Selec
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
db = client['Monitor']
series_day = db['Day']
series_month = db['Month']
series_day_total = db['day_total ']
series_month_total = db['month_total']
bd = Selec()





def get_response_url(url):
    headers = {
    'API-Key': 'API-Key'
    }
    while True:
        responce = requests.get(url, headers=headers, timeout=300)
        if responce.status_code==200:
            return responce.json()
        else:
            continue
            
def percent(morj, plan):
    return str(round((float(morj)/float(plan))*100))+' %'

class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "signin.html")
        return render(request, "index.html")

class SignInView(View):
    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        username = request.POST["Username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        return render(request, "index.html")


class SingUPView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        username = request.POST["Username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect(reverse("hu"))

class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect(reverse("index"))

class UsersView(View):
    def get(self, request):
        username = request.GET.get("username", "")
        if username:
            users = User.objects.filter(username__contains=username)
        else:
            users = User.objects.all()
        return render(request, "users.html", {"users": users, "username": username})

class UserView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        if not user:
            return Http404()
        massages = Message.objects.filter(author=user).order_by("-created_at").all()
        return render(request, "user.html", {"user_": user, "messages": massages})

    def post(self, request, username):
        user = User.objects.get(username=username)
        if request.user != user:
            return HttpResponseForbidden()

        text = request.POST["text"]
        message = Message(text=text, author=user)
        message.save()

        return self.get(request, username)

class MessageDeleteView(View):
    def post(self, request, id):
        message = Message.objects.filter(pk=id).first()
        if not message:
            return Http404()
        if message.author != request.user:
            return HttpResponseForbidden()
        message.delete()

        return redirect(reverse("user", kwargs={
            "username": request.user,
        }))

class Day_merj(View):
    def get(self, request):
        Total_Day = {}
        day = {'FB': bd.sel_fb_day(series_day), 'scheme':bd.sel_sxem_day(series_day), "other": "0", "Total": bd.sel_day(series_day_total)}
        Month = {'FB': bd.sel_fb_month(series_month), 'scheme':bd.sel_sxem_month(series_month), "other": "0", "Total": bd.sel_month(series_month_total)}
        Total_Day["TotalInformation_month"] = Month
        Total_Day["Total_Day"] = day
        return JsonResponse(Total_Day)
        
 
