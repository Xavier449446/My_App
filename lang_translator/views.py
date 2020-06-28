from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'lang_translator/home.html')

def about(request):
    return render(request,'lang_translator/about.html')

def temp(request):
    return render(request,'lang_translator/temp.html')