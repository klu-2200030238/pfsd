from django.shortcuts import render, redirect
from .models import *  # Assuming your model is named 'student'
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect


# Create your views here.




def mymainpage(request):
    return render(request, "mainpage.html")


def myabout(request):
    return render(request, "about.html")


def mycontact(request):
    return render(request, "contact.html")


def myfestivals(request):
    return render(request, "festivals.html")


def mytraditions(request):
    return render(request, "traditions.html")

def myunsolvedmysteries(request):
    return render(request, "unsolvedmysteries.html")

def myhangingpillars(request):
    return render(request, "hangingpillars.html")
def mypadmanabhaswamytemple(request):
    return render(request, "padmanabhaswamytemple.html")


def mymagnetichill(request):
    return render(request, "magnetichill.html")
def myganeshchaturthi(request):
    return render(request, "ganeshchaturthi.html")

def myroopkundskeletonlake(request):
    return render(request, "roopkundskeletonlake.html")



def mydiwali(request):
    return render(request, "diwali.html")


def myramadan(request):
    return render(request, "ramadan.html")


def mychristmas(request):
    return render(request, "christmas.html")


def mycultures(request):
    return render(request, "cultures.html")


def mynorth(request):
    return render(request, "north.html")

def mysouth(request):
    return render(request, "south.html")

def myeast(request):
    return render(request, "east.html")

def mywest(request):
    return render(request, "west.html")



def mytraditions(request):
    return render(request, "traditions.html")

def myjoint(request):
    return render(request, "joint.html")

def mykathakali(request):
    return render(request, "kathakali.html")

def mykerala(request):
    return render(request, "kerala.html")
def mymanipur(request):
    return render(request, "manipur.html")

def myhistorical(request):
    return render(request,"historical.html")

def myagra(request):
    return render(request,"agra.html")

def myellora(request):
    return render(request,"ellora.html")

def myredfort(request):
    return render(request,"redfort.html")

def mygateway(request):
    return render(request,"gateway.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        student = sdp.objects.create(username=username, email=email, password=password)
        student.save()
        return render(request, 'signin.html')  # Redirect to login page after successful signup
    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        try:
            sdp.objects.get(Username=username, password=password)
            return redirect('mainpage')
        except sdp.DoesNotExist:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    return render(request,'signin.html')


