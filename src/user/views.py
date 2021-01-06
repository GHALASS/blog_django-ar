from django.contrib import auth
from django.shortcuts import redirect, render
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
        username = request.POST['username']
        password = request.POST['password']
        user  = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'هناك خطأ في إسم المستخدم أو كلمة المرور.')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
        'form':form,
    })

def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج',
    })