from django.shortcuts import render, HttpResponse, redirect

import requests


# Create your views here.
def index(request):
    return HttpResponse("Welcome to my website")


def user_list(request):
    return HttpResponse("User list")


def home(req):
    my_list = ["spam", "ham", "eggs"]
    # http: // www.chinaunicom.com / api / article / NewsByIndex / 1 / 2021 / 02 / news
    res = requests.get(
        "https://newsapi.org/v2/everything?q=tesla&from=2022-02-11&sortBy=publishedAt&apiKey=c739d0d5c7824835b9b0d246612f1224")
    content = res.json()
    return render(req, "home.html", {"n1": my_list, "n2": content})


def test(req):
    print(req.method)
    print(req.GET)
    print(req.POST)

    return HttpResponse("Success")


def login(req):
    if req.method == "GET":
        return render(req, "login.html")
    print(req.POST)
    username = req.POST.get("username")
    password = req.POST.get("password")
    if username == "root" and password == "123":
        return redirect("https://www.google.com.au/")
    return render(req, "login.html", {"erro_message": "username or password wrong!"})
