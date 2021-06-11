from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name= request.POST['name']
        email = request.POST['email']
        reason = request.POST['reason']
        content = request.POST['content']
    
        if len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, reason=reason, content=content)
            contact.save()
            messages.success(request, "Your message has been sent!")
            messages.warning(request, "I will respond back soon!")
    return render(request, 'index.html')