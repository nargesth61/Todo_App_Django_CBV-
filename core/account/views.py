from django.shortcuts import render
from django.views.generic import CreateView,FormView,View
from django.views.generic.base import TemplateView
from account.forms import UserForm,Userlogin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# this viwe is for register users
class signup_user(CreateView):
    form_class = UserForm
    success_url = '/register/login/'
    template_name = 'signup.html'
    def form_valid(self, form):
       user = form.save(commit=False)
       password = self.request.POST['password']
       user.set_password(password)
       user.save()
       return super().form_valid(form)

# this class for login and authenticated user after register
class LoginFormView(FormView):
    template_name = 'login.html'
    form_class =Userlogin
    success_url ='/todo/'
    def form_valid(self,form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password'] 
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active and user.is_authenticated:
            login(self.request, user)
            print("yes")
            return super(LoginFormView, self).form_valid(form)

#for logout user
#  
class logout_view(LoginRequiredMixin,View):
      def get(self, request):
        logout(request)
        return redirect('/register/')
            
