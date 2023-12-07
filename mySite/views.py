from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HtmlForms
from django.db import connection
from django.contrib import messages


def index(request):
  
  form = HtmlForms()
  
  if request.method == 'POST':
    form = HtmlForms(request.POST)
    
    if form.is_valid():
       fName = form.cleaned_data['fName']
       lName = form.cleaned_data['lName']
       email = form.cleaned_data['email']
       address = form.cleaned_data['address']
      
       with connection.cursor() as cursor:
        sql = "INSERT INTO users(first_name,last_name,email,address) VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, [fName,lName,email,address])
        
        messages.success(request, "Data Inserted Successfully!")
        return redirect("index")
      
  context = {'form': form}    
  return render(request, 'index.html', context=context)
