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

# Create your views here.

def requests(request):

    return render(request, 'control/home.html', {'requests': Request.objects.all().order_by('-request_date')})




def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(user_name=user_name)
                
                if user.password == password:
                    
                    request.session['user_id'] = user.user_id
                    return redirect('home')
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
            form.save()
            return render(request, 'control/signup.html', {'message': 'Signup successful!'})
        else:
            return render(request, 'control/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'control/signup.html', {'form': form})




def user_detail(request, user_id):
    user = get_object_or_404(User, user_id=user_id) 

    
    if request.method == 'POST' and 'create_request' in request.POST:
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = user 
            new_request.save()
            return redirect('user_detail', user_id=user.id)

    
    elif request.method == 'POST' and 'update_status' in request.POST:
        request_id = request.POST.get('request_id')
        request_to_update = get_object_or_404(Request, request_id=request_id, user=user)
        form = RequestStatusForm(request.POST, instance=request_to_update)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = RequestForm()

    return render(request, 'control/user_details.html', {'user': user, 'form': form, 'requests': user.requests.all()})






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
