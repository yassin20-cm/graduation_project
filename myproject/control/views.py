from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Request
from .forms import RequestForm,RequestStatusForm
from .forms import UserSignupForm
from django.contrib.auth import login

# Create your views here.

def requests(request):

    return render(request, 'control/home.html', {'requests': Request.objects.all().order_by('-request_date')})

def login(request):

    return render(request,'control/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()

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
