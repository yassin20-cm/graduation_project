from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Request
from .forms import RequestForm,RequestStatusForm
from .forms import SignupForm,UserLoginForm
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password



# Create your views here.

def requests(request):
    user = None
    if 'user_id' in request.session:
        try:
            user = User.objects.get(user_id=request.session['user_id'])
        except User.DoesNotExist:
            user = None

    all_requests = Request.objects.all().order_by('-request_date')
    return render(request, 'control/home.html', {'requests': all_requests, 'custom_user': user})



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(user_name=user_name)
                
                if check_password(password, user.password):
                    
                    request.session['user_id'] = user.user_id
                    return redirect('user_profile',user_id=user.user_id)
                else:
                    form.add_error('password', 'Invalid username or password.')
            except User.DoesNotExist:
                form.add_error('user_name', 'User not found.')

    else:
        form = UserLoginForm()

    return render(request, 'control/login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            return render(request, 'control/signup.html', {'message': 'Signup successful!'})
        else:
            return render(request, 'control/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'control/signup.html', {'form': form})



def user_detail(request, user_id):
    user = get_object_or_404(User, user_id=user_id)  
    create_request_form = RequestForm()
    update_status_form = None

    if request.method == 'POST':
        if 'create_request' in request.POST: 
            create_request_form = RequestForm(request.POST, request.FILES)
            if create_request_form.is_valid():
                new_request = create_request_form.save(commit=False)
                new_request.user = user
                new_request.save()
                return redirect('user_profile', user_id=user.user_id)  

        elif 'update_status' in request.POST: 
            request_id = request.POST.get('request_id')
            request_to_update = get_object_or_404(Request, request_id=request_id, user=user) 
            update_status_form = RequestStatusForm(request.POST, instance=request_to_update)
            if update_status_form.is_valid():
                update_status_form.save()
                return redirect('user_profile', user_id=user.user_id)  
            else:
                update_status_form = RequestStatusForm(instance=request_to_update)

    requests = user.requests.all()  
    context = {
        'user': user,
        'create_request_form': create_request_form,
        'update_status_form': update_status_form,
        'requests': requests,
    }
    return render(request, 'control/user_profile.html', context)


@csrf_exempt  
def update_request_status(request, request_id):
    if request.method == "POST":
        try:
            new_status = request.POST.get('status')
            req = Request.objects.get(request_id=request_id)
            req.request_state = new_status
            req.save()
            return JsonResponse({'success': True})
        except Request.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Request not found'})

from django.shortcuts import redirect

def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')



 





