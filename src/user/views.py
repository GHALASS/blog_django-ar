from django.shortcuts import redirect, render
from .forms import UserCreationForm, LoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # messages.success(request, 'تهانينا  {} لقد تم التسجيل بنجاح'.format(username))
            messages.success(request, f'تهانينا  {username} لقد تم التسجيل بنجاح')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title':'التسجيل',
        'form':form,
    })

def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
        'form':form
    })