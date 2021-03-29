from django.shortcuts import render
from django.contrib.auth.models import auth
from django.shortcuts import render,redirect
from account.models import User
from payment.models import finalpayment
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm

class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Login(CreateView):
    template_name = 'signin.html'
    def post(self, request, *args, **kwargs):
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request, user)
            # print('a staff logged in')
            if user.is_authenticated and user.is_staff:
                auth.login(request, user)
                # print('a staff logged in')
                return render(request, 'staffpage.html')
            elif user.is_authenticated and user.is_applicant:
                return render(request, 'applicant.html')
            elif user.is_authenticated and user.is_accountant:
                allpayments=finalpayment.objects.all()
                return render(request, 'account1.html', {'allpayments':allpayments})
            elif user.is_authenticated and user.is_admin:
                return render(request, 'admin.html')
            else:
                auth.login(request, user)
                current_user = request.user
                # print('this is a student')
                return render(request, 'student_dashboard.html',{'current_user': current_user})
    def get(self, request, *args, **kwargs):
        return render(request,'signin.html')







