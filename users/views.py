from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm)

from .models import Employee

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
                'form' : form,
                'title' : 'Register'
              }
    return render(request,'register.html',context)



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
                'u_form': u_form,
                'p_form': p_form
              }
    return render(request,'profile.html',context)


def comingSoon(request):
    context = {

              }
    return render(request,'coming_soon.html',context)

@login_required
def home(request):
    context = {
                'is_employee': request.user.profile.is_employee
              }
    return render(request,'index.html',context)



def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

