from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import EmailForm
from .models import Email
import random  
# Create your views here.

def random_string(length):  
    sample_string = 'pqrstuvwxy'
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    return result

def convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

class HomeView(View):
	def get(self, request):
		form = EmailForm()
		return render(request, 'index.html', {'form': form})
	
	def post(self, request):
		if request.method == 'POST':
			email = request.POST['email']

			user = User.objects.create_user(username=random_string(20), email=email)
			user.save()
            
			return redirect('success')
		else:
			return render(request, 'index.html')

        
class SuccessView(View):

    def get(self, request):
        return render(request, "success.html")


class EmailsView(View):

	def get(self, request):		
		usuario = list(User.objects.values('email'))
		context=""
		for tdict in usuario:
			for key in tdict:
				context+=f'{tdict[key]}, '
		return render(request, "emails.html", {'usuario': context})