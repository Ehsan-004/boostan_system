from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from member.models import Member, Student, Teacher


class SideMenuView(View):
    def get(self, request):
        if not request.user or not request.user.is_authenticated:
            return JsonResponse({"sideMenu": "<h1>nothing here</h1>"})

        user = request.user
        member = Member.objects.get(user_profile=user)
        data = None

        if member.position == "student":
            data = {
                "sideMenu": """
                        <li><a onclick="profile()" href="#">مشخصات من</a></li>
                        <li><a onclick= href="">نمرات من</a></li>
                        <li><a onclick= href="">درخواست های من</a></li>
                        <li><a onclick= href="">اساتید من</a></li>
                        """,
                "name": user.first_name + " " + user.last_name,
            }
        elif member.position == "teacher":
            data = None
        return JsonResponse(data)


def profile(req):
    if not req.user or not req.user.is_authenticated:
        return None
    first_name = req.user.first_name
    last_name = req.user.last_name
    member = Member.objects.get(user_profile=req.user)
    profile_picture = member.profile_picture.url
    structure = None

    if member.position == "student":
        student = Student.objects.get(member_profile=member)
        structure = f"""
            <div class="profile_main_container">
                <aside class="profile_details">
                    <ul>
                        <li><img id="profile_details_picture" src="{profile_picture}" alt=""></li>
                        <li><ul><li>نام و نام خانوادگی:</li><li><h4>{first_name} {last_name}</h4></li></ul></li>
                        <li><ul><li>شماره ترم:</li><li><h4><h4>{student.passed_terms}</h4></h4></li></ul></li>
                        <li><ul><li>دانشکده:</li><li><h4>{student.department}</h4></li></ul></li>
                    </ul>
                </aside>
                <div class="content_displaay"></div>
            </div>    
        """

    data = {
        "first": first_name,
        "last": last_name,
        "structure": structure,
    }
    return JsonResponse(data)
