from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.models import User
import random, secrets, string

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    return render(request, 'didnotguess/index.html', {'user': request.user})
    
def login(request):
    message = request.session.pop('login_message', 'Enter name and password to login')
    return render(request, 'didnotguess/login.html', {'message': message})
    
def loginuser(request):
    try:
        name = request.POST['username']
        password = request.POST['userpassword']
    except (KeyError):
        return HttpResponse('Data has not been transfered')
    else:
        user = authenticate(username = name, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('didnotguess:index')
        else:
            request.session['login_message'] = 'Username or/and Password are incorrect'
            return redirect('didnotguess:login')
            
def registration(request):
    error = request.session.pop('registration_error', None)
    return render(request, 'didnotguess/registration.html', { 'error': error })
    
def registrationuser(request):
    try: 
        name = request.POST['username']
        password = request.POST['userpassword']
        confirm = request.POST['confirmpassword']
    except (KeyError):
        return HttpResponse("Data has not been transfered")
    else:
        try:
            u = User.objects.get(username=name)
        except (User.DoesNotExist):
            if password != confirm:
                request.session['registration_error'] = 'Passwords are not equal'
                return redirect('didnotguess:registration')
            else:
                u = User.objects.create_user(username=name, password=password)
                return redirect('didnotguess:login')
        else:
            request.session['registration_error'] = 'User with this name already exists'
            return redirect('didnotguess:registration')
            
def logout(request):
    auth_logout(request)
    return redirect('didnotguess:login')
    
def generator_view(request, type, result_is_necessary):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    request.session['request_type'] = type
    result = request.session.pop('result', None)
    if result is None:
        if result_is_necessary:
            return execution(request)
        else:
            return render(request, 'didnotguess/app.html', {'type': type})
    else:
        return render(request, 'didnotguess/app.html', {'type': type, 'result': result})

def gen_random_number(request):
    return generator_view(request, 'gen_random_number', True)

def gen_random_number_list(request):
    return generator_view(request, 'gen_random_number_list', False)
    
def get_random_word_from_text(request):
    return generator_view(request, 'get_random_word_from_text', False)

def gen_random_password(request):
    return generator_view(request, 'gen_random_password', True)
    
def gen_random_password_list(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    request.session['request_type'] = 'gen_random_password_list'
    return render(request, 'didnotguess/app.html', {'type': 'gen_random_password_list'})
    
def execution(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    type = request.session.pop('request_type', None)
    if type is None:
        return HttpResponse("No execution has been planned")
    if type == 'gen_random_number':
        request.session['result'] = random.randint(-10000,10000)
        return redirect('didnotguess:%s' % type)
    else: 
        if type == "gen_random_number_list":
            try:
                from_val = request.POST['from']
                to_val = request.POST['to']
            except (KeyError):
                return redirect("didnotguess:%s" % type)
            else:
                result = []
                for index in range(int(from_val),int(to_val)+1):
                    result.append(index)
                request.session['result'] = result
                return redirect("didnotguess:%s" % type)
        else:
            if type == 'get_random_word_from_text':
                try:
                    text = request.POST['text']
                except:
                    return redirect("didnotguess:%s" % type)
                else:
                    words = text.split()
                    ind = random.randint(0, len(words) - 1)
                    request.session['result'] = words[ind]
                    return redirect('didnotguess:%s' % type)
            else:
                if type == 'gen_random_password':
                    request.session['result'] = random_password()  # change get_random_password() to random_password() GORDUN
                    return redirect("didnotguess:%s" % type)
                
                
                
                
                
def random_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+=.,`~'"
    length = random.randint(8, 20)
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password                