from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout


class StudentLoginView(View):
    http_method_names = ['get', 'post']
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if False in [username, password]:
            return render(request, self.template_name, {'error': 'لطفا هر دو مورد را وارد کنید.'})

        user = authenticate(username=username, password=password)

        if user is None or not user.is_active:
            return render(request, self.template_name, {'error': 'نام کاربری یا رمز عبور اشتباه است.'})


        try:
            login(request, user)
            return redirect('home')
        except:
            return render(request, self.template_name, {'error': 'خطایی رخ داد.'})


class RegisterView(View):
    http_method_names = ['get', 'post']
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)

    def post(self, request):
        pass


class LogoutView(View):
    http_method_names = ['get', ]

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        logout(request)
        return redirect('home')
