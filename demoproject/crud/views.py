from django.shortcuts import render,redirect
from . models import contact,image,slider
from django.contrib import messages

def home(request):
    sliderimage = slider.objects.all()
    return render(request,'home.html',{'sliderimage':sliderimage})

def aboutus(request):
    return render(request,'aboutus.html')

def gallery(request):
    images = image.objects.all()
    return render(request,'gallery.html',{'images':images})

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        cont = contact(name=name,email=email,message=message)
        cont.save()
        messages.success(request, 'Your Message Sent Successfully, We Will Be Contact You Shortly..!')
    else:
        messages.warning(request, 'Please Fill Carefully')
    return render(request,'contactus.html')
