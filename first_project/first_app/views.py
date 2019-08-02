from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
from . import forms

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS")
            print ("NAME: " +form.cleaned_data['name'])
            print ("EMAIL: " +form.cleaned_data['email'])
            print ("TEXT: " +form.cleaned_data['text'])
            
    form_dict = {'form': form} 
    return render(request,'first_app/form_page.html',context=form_dict)