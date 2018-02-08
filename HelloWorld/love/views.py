from django.shortcuts import render
#from django.shortcuts import HttpResponse
from love import models


user_list = [
	{"user":"jack","pwd":"123"},
	{"user":"rose","pwd":"132"},
]



# Create your views here.

def index(request):
    #return HttpResponse("Hello World!")
    #
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        temp = {"user":username, "pwd":password}
        models.UserInfo.objects.create(user=username, pwd=password)
        #user_list.append(temp)
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html",{"data": user_list})