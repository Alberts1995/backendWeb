from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import Message
import requests
import pandas as pd
from datetime import datetime, date, time
from .models import SQLite
import dateparser
import datetime
import xlwt



bd = SQLite()


All = []
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
    
class SignInView(View):
    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        username = request.POST["Username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

        return redirect(reverse("hu"))


class SingUPView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        username = request.POST["Username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect(reverse("index"))

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
        return render(request, "users.html", {"users":users, "username":username})


class UserView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        if not user:
            return Http404()
        massages = Message.objects.filter(author=user).order_by("-created_at").all()
        return render(request, "user.html", {"user_":user ,"messages":massages})

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



class Offers(View):
    def get(self,request):
        day_to = datetime.date.today()
        info = bd.select_information(day_to, day_to)
        new_info = []
        for x in info:
            Confirmed = []
            Pending	= []
            Hold = []
            Confirmed.append((x[5].split(", ")[0].split("[")[1].split("]")[0], x[5].split(", ")[1].split("[")[1].split("]")[0], x[5].split(", ")[2].split("[")[1].split("]")[0]))
            Pending.append((x[6].split(", ")[0].split("[")[1].split("]")[0], x[6].split(", ")[1].split("[")[1].split("]")[0], x[6].split(", ")[2].split("[")[1].split("]")[0]))
            Hold.append((x[7].split(", ")[0].split("[")[1].split("]")[0], x[7].split(", ")[1].split("[")[1].split("]")[0], x[7].split(", ")[2].split("[")[1].split("]")[0]))
            new_info.append((x[0], x[1], x[2], x[3], x[4], Confirmed[0], Pending[0], Hold[0], x[8], x[9]))
            Confirmed.clear()
        All.append(new_info)
        return render(request, "offer.html", context={"info": new_info})
    def post(self, request):
        All.clear()
        date_from = request.POST["date_from"]
        date_to = request.POST["date_to"]
        info = bd.select_information(date_from, date_to)
        new_info = []
        for x in info:
            Confirmed = []
            Pending	= []
            Hold = []
            Confirmed.append((x[5].split(", ")[0].split("[")[1].split("]")[0], x[5].split(", ")[1].split("[")[1].split("]")[0], x[5].split(", ")[2].split("[")[1].split("]")[0]))
            Pending.append((x[6].split(", ")[0].split("[")[1].split("]")[0], x[6].split(", ")[1].split("[")[1].split("]")[0], x[6].split(", ")[2].split("[")[1].split("]")[0]))
            Hold.append((x[7].split(", ")[0].split("[")[1].split("]")[0], x[7].split(", ")[1].split("[")[1].split("]")[0], x[7].split(", ")[2].split("[")[1].split("]")[0]))
            new_info.append((x[0], x[1], x[2], x[3], x[4], Confirmed[0], Pending[0], Hold[0], x[8], x[9]))
            Confirmed.clear()
        All.append(new_info)
        return render(request, "offer.html", context={"info": new_info})


class Excel_View(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="segmentaciya.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws =  wb.add_sheet("segmentaciya", cell_overwrite_ok=True)

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ["Webmster", "Category", "Offer", "Rekl", "Country", "Confirmed", "Charge", "Revenue", "Earning", 
                                                                        "Pending", "Charge", "Revenue", "Earning",  
                                                                        "Hold", "Charge", "Revenue", "Earning",  
                    "Sours", "Date"]
        

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = All
        for row in rows:
            for x in row:
                row_num += 1
                a = x[0], x[1], x[2], x[3], x[4], "",x[5][0], x[5][1], x[5][2], "", x[6][0], x[6][1], x[6][2], "", x[7][0], x[7][1], x[7][2], x[8], x[9]
                print(a)
                for col_num in range(len(a)):
                    ws.write(row_num, col_num, str(a[col_num]), font_style)
        wb.save(response)
        return response

# class Excel_View(View):
#     def get(self, request):
#         return render(request, "Excel.html")
    
#     def post(self, request):
#         Excel = request.POST["Excel"]
#         df = pd.DataFrame(All)
#         df.to_excel('test.xls')
#         return redirect(reverse("hu"))