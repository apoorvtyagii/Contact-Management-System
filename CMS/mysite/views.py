from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

#decorator
def LoginRequired(func):
    def wrapper(request, *args, **kwargs):
        if 'email' in request.session:
            return func(request, *args, **kwargs)
        else:
            return Login(request)
    return wrapper

@LoginRequired
def MyDirectory(request):
    # objects = Contacts.objects.filter(createby=email)
    email = request.session['email']
    objects = Contacts.objects.filter(createdby=email).all()
    return render(request, 'directory.html', {"allcontacts" : objects, 'email': email}) 

@LoginRequired
def EditContact(request, **kwargs):
    contact_id = kwargs.get("contact_id", "")
    if request.method == 'POST':
        email = request.session['email']
        # check if the contact is already present in Contacts table
        if (
            Contacts.objects.filter(id=contact_id).first()
            is not None
        ):
            edit_this_contact = Contacts.objects.filter(id=contact_id).first()
            edit_this_contact.name = request.POST.get('contact_name')
            edit_this_contact.email = request.POST.get('contact_email')
            edit_this_contact.phone = request.POST.get('contact_phone')
            edit_this_contact.office = request.POST.get('contact_office')
            edit_this_contact.createdby = email
            edit_this_contact.save()
            messages.info(request, "Contact Updated")
        return MyDirectory(request)
    else:
        contact = Contacts.objects.filter(id=contact_id).first()
        return render(request, 'add.html', {'contactedit': True, 'contact': contact})

@LoginRequired
def AddContact(request):
    if request.method == 'POST':
        new_contact = Contacts.objects.create(
            name = request.POST.get('contact_name'),
            email = request.POST.get('contact_email'),
            phone = request.POST.get('contact_phone'),
            office = request.POST.get('contact_office'),
            createdby = request.session['email']
        )
        messages.info(request, "contact added!")
        return MyDirectory(request)
    else:
        return render(request, 'add.html', {'contactedit': False})

@LoginRequired
def DeleteContact(request, **kwargs):
    contact_id = kwargs.get("contact_id", "")
    if Contacts.objects.filter(id=contact_id).exists():
        contact_to_delete = Contacts.objects.filter(id=contact_id)
        contact_to_delete[0].delete()
        messages.info(request, "Dontact has been deleted")
    return redirect("mydirectory")



def Login(request):
    if request.method == 'POST':
        if IsUserAuthenticate(request.POST.get('email'), request.POST.get('password')):
            email = request.POST.get('email')
            request.session['email'] = email
            return MyDirectory(request)
    return render(request, 'login.html')

def Logout(request):
    if 'email' in request.session:
        request.session.pop('email', None)
    return render(request, 'login.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        emessage = None
        if not (
            Users.objects.filter(email=email).exists()
            and Users.objects.filter(username=username).exists()
        ):
            password = request.POST.get("password")
            user = Users.objects.create(name=username , email=email, password=password)
            user.save()
            return redirect("login")

        else:
            emessage = "ERROR IN signup: This email is already registed, please try login"
            return render(request, "signUp.html", {"emessage": emessage})

    if request.method == "GET":
        return render(request, "signUp.html")



def IsUserAuthenticate(email, password):
   if Users.objects.filter(email=email, password=password).exists():
      return True
   else:
      return False