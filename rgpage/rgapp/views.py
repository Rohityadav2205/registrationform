from django.shortcuts import HttpResponse, render,redirect

from .models import rgmodel


# Create your views here.
def index(request):
    return HttpResponse("GOKUL")


# registration form input
def registration(request):
    username = ""
    name = ""
    password = ""
    result = ""
    confirmpassword = ""

    submit = 0
    if request.GET:
        username = request.GET["username"]
        name = request.GET["name"]
        password = request.GET["password"]
        confirmpassword = request.GET["confirmpassword"]
        if password != confirmpassword:
            result = "Passwords not matched"
            return render(request, "create.html",
                          {"username": username, "name": name, "password": password, "confirmpassword": confirmpassword,
                           "submit": submit,
                           "result": result})
        try:

            ms = rgmodel()
            ms.username = username
            ms.name = name
            ms.password = password

            ms.save()
            result = "Saved"
        except:
            result = "Username already exists"

        print("saved data")

    return render(request, "create.html",
                  {"username": username, "name": name, "password": password, "confirmpassword": confirmpassword,
                   "submit": submit, "result": result})


# login page

def login(request):
    username = ""
    password = ""
    data = ""

    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]

        data = rgmodel.objects.filter(username=username).filter(password=password)
        # data=rgmodel.objects.filter(password=password)
        if len(data) <= 0:
            data = "no record"
        else:
              data = data[0]
              session=request.session
              session["username"]=data.username
              print(data.username)
              return redirect("/home")


    return render(request, "login.html", {"username": username, "password": password, "data": data})


def home(request):
    currentuser=request.session.get("username")
    if currentuser is None:
        return  redirect("/login")

    return render(request,"home.html",{"username":currentuser})


def logout(request):
    try:
        request.session.pop("username")
    except:
        pass
    # return HttpResponse("User logout")

    return  redirect("/registration")

# session used in django

"""
def mysession(request):
    session = request.session
    session[1] = "One"
    return render(request, "session.html", {"session": session})

def sessionset(request):
    username = ""
    password = ""
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        request.session["username"] = username
    return render(request, "sessionset.html", {"username": username, "password": password})

def sessionremove(request):
    username = ""
    if request.POST:
        username = request.POST["username"]
        try:
            request.session.pop(username)
        except:
            pass

    return render(request, "sessionremove.html", {"username": username})


def sessionview(request):
    
    return render(request, "sessionview.html", {"session": request.session.items()})
    """






