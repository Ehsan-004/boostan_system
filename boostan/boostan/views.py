from django.shortcuts import render, redirect, reverse
from django.views import View
from member.models import Member

class IndexView(View):
    http_method_names = ['get', ]
    template_name = 'base.html'

    def get(self, request):
        if request.user and not request.user.is_authenticated:
            return redirect('members:login')
        user = request.user
        member = Member.objects.get(user_profile=user)

        if member.position == "student":
            context = {
                'member': member,
                'role': 'دانشجو'
            }
            return render(request, self.template_name, context)
        elif member.position == "teacher":
            context = {
                'member': member,
            }
            return render(request, self.template_name, context)
        elif member.position == "admin":
            context = {
                'member': member,
            }
            return render(request, self.template_name, context)

        return redirect('home')
