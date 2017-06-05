from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserRequest, RequestType
from django.utils import timezone
import random, string

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    user_requests = UserRequest.objects.filter(user=request.user)
    rand_request_string = None
    if len(user_requests) > 0:
        rand_request = user_requests[random.randint(0, len(user_requests) - 1)]
        req_date = rand_request.request_date.replace(microsecond = 0, second = 0)
        rand_request_string = "You have requested %s at %s on %s" % (rand_request.type.typename, req_date.time(), req_date.date())
    return render(request, 'didnotguess/index.html', {'user': request.user, 'rand_request': rand_request_string})

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
        record_request(request, type)
        return render(request, 'didnotguess/app.html', {'type': type, 'result': result})

def requests_story_current(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    requests = UserRequest.objects.filter(user=request.user)
    return render(request, 'didnotguess/requests.html', {'requests': requests, 'all': False})

def requests_story_all(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    requests = UserRequest.objects.all()
    return render(request, 'didnotguess/requests.html', {'requests': requests, 'all': True})

def statistics(request):
    if not request.user.is_authenticated:
        return redirect('didnotguess:login')
    all_requests_count = len(UserRequest.objects.filter(user = request.user))
    type_requests = []
    for t in RequestType.objects.all():
        type_requests.append("%s : %s" % (t.typename, len(UserRequest.objects.filter(type = t, user = request.user))))
    return render(request, 'didnotguess/statistics.html', {'all_requests_count': all_requests_count, 'type_requests': type_requests, 'username': request.user.username})

def gen_random_number(request):
    return generator_view(request, 'gen_random_number', True)

def gen_random_number_list(request):
    return generator_view(request, 'gen_random_number_list', False)

def get_random_word_from_text(request):
    return generator_view(request, 'get_random_word_from_text', False)

def gen_random_password(request):
    return generator_view(request, 'gen_random_password', True)

def gen_random_password_list(request):
    return generator_view(request, 'gen_random_password_list', False)

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
                except (KeyError):
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
                else:
                    if type == 'gen_random_password_list':
                        try:
                            count = request.POST['count']
                        except (KeyError):
                            return redirect('didnotguess:%s' % type)
                        else:
                            result = []
                            for index in range(int(count)):
                                result.append(random_password())
                            request.session['result'] = result
                            return redirect('didnotguess:%s' % type)


def random_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+~"
    length = random.randint(8, 20)
    password = ''
    for index in range(length):
        ind = random.randint(0, len(alphabet) - 1)
        password += alphabet[ind]
    return password

def record_request(request, type):
    r_type = RequestType.objects.get(typename=type)
    record = UserRequest(user=request.user, type=r_type, request_date=timezone.now())
    record.save()