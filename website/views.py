from django.shortcuts import render, redirect
from django.conf import settings
from .models import Admission
from .forms import AdmissionForm
from django.contrib import messages


def index(requests):
    return render(requests, 'index.html')

def contact(requests):
    return render(requests, 'contact-us.html')

def gallery(requests):
    return render(requests, 'gallery-photo.html')

def admission(requests):
    if requests.method == 'POST':
        form = AdmissionForm(requests.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = requests.POST['name']
            father_name = requests.POST['father_name']
            guardian_name = requests.POST['guardian_name']
            occupation = requests.POST['occupation']
            dob = requests.POST['dob']
            phone = requests.POST['phone']
            email = requests.POST['email']
            qualification = requests.POST['qualification']
            address = requests.POST['address']
            city = requests.POST['city']
            pincode = requests.POST['pincode']
            religion = requests.POST['religion']
            sex  = requests.POST['sex']
            nationality = requests.POST['nationality']
            

            messages.success(requests, ("There is an error in your form please try again.. "))

            return render(requests, 'admission.html', {'name': name,
                'father_name' : father_name,
                'guardian_name' : guardian_name,
                'occupation': occupation,
                'dob': dob,
                'phone':phone,
                'email': email,
                'qualification': qualification,
                'address': address,
                'city':city,
                'pincode':pincode,
                'religion':religion,
                'sex' : sex,
                'nationality': nationality
            })

        messages.success(requests, ("Your form has been submitted successfully."))
        return redirect('/')
    else:
        return render(requests, 'admission.html')

def about(requests):
    return render(requests, 'about.html')