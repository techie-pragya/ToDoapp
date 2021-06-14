from django.shortcuts import render,redirect
from app.forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User

from .models import UserProfile
from app.forms import UserProfileForm
# Create your views here.
def base_view(request):
	return render(request,'app/base.html')

def home_view(request):
	return render(request,'app/home.html')

def profile_view(request):
	return render(request,'app/profile.html')

def signup_view(request):
	if request.method=='POST':
		form=SignupForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.is_active=0
		user.save()
		activation_code=random.randrange(111111,999999)
		request.session['activation_code']=activation_code
		subject='Creative_you Welcomes you'
		message='''Welcome you in our website.<br /><br />
					Please click over the <a href='http://localhost:8000/app/activation/?id={}&act_code={}'>link</a> to activate your account.
				'''.format(user.id,activation_code)
		
		send_mail(subject,'','App Welcomes you',[request.POST.get('email')],fail_silently=False,html_message=message)
		return redirect('/app/home')
	else:
		form=SignupForm()
		return render(request,'app/signup.html',{'form':form})


def activation_view(request):
	uid=request.GET.get('id')
	act_code=request.GET.get('act_code')
	activation_code=str(request.session.get('activation_code'))
	try:
		user=User.objects.get(id=uid)

		if act_code==activation_code:
			user.is_active=1
			user.save()
			return redirect('/app/profile')
	except:
		print('Invalid Account')
		return render(request,'app/error.html')
	

@login_required
def profile_view(request):
	if request.method=='POST':
		pic=request.FILES.get('profpic')
		mobile=request.POST.get('mobile')
		ctid=request.POST.get('city')
		uid=request.session['_auth_user_id']
		uf=UserProfile(user_id=uid,city_id=ctid,profpic=pic,mobile=mobile)
		uf.save()
		return redirect('/app/home')
	else:
		form=UserProfileForm()
		return render(request,'app/profile.html',{'form':form})


def password_changed_done_view(request):
	return render(request,'registration/password-change/password_change_done.html')
	
