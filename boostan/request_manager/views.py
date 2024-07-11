from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from member.models import Member, Student, Teacher, Course, Score


class SideMenuView(View):
    """
    This view renders the side menu for the user.
    """
    def get(self, request):
        if not request.user or not request.user.is_authenticated:
            return JsonResponse({"sideMenu": "<h1>nothing here</h1>"})

        user = request.user
        member = Member.objects.get(user_profile=user)
        data = None
        name = user.first_name + ' ' + user.last_name

        if member.position == "student":
            data = {
                "sideMenu": """
                        <li><a onclick="profile()" href="#">مشخصات من</a></li>
                        <li><a onclick="courses()" href="#">کلاس های من</a></li>
                        <li><a onclick="studentScores()" href="#">نمرات من</a></li>
                        <li><a onclick="" href="#">درخواست های من</a></li>
                        <li><a onclick="" href="#">اساتید من</a></li>
                        """,
                "name": name,
            }
        elif member.position == "teacher":
            data = None
        elif member.position == "admin":
            data = {
                "sideMenu": """
                    <li><a onclick="admin_all_members()" href="#">همه اعضا</a></li>
                """,
                "name": name,
            }
        return JsonResponse(data)


def profile(req):
    """
    This function returns profile data.
    It is available through an ajax_request.
    """
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
                        <li><ul class="inner_profile_details"><li>نام و نام خانوادگی:</li><li><h4>{first_name} {last_name}</h4></li></ul></li>
                        <li><ul class="inner_profile_details"><li>شماره ترم:</li><li><h4><h4>{student.passed_terms}</h4></h4></li></ul></li>
                        <li><ul class="inner_profile_details"><li>دانشکده:</li><li><h4>{student.department}</h4></li></ul></li>
                    </ul>
                </aside>
                <div class="content_display"></div>
            </div>    
        """

    data = {
        "first": first_name,
        "last": last_name,
        "structure": structure,
    }
    return JsonResponse(data)


def admin_all(req):
    """
    This functions returns all users with some details about them in json format.
    It is available through an ajax request.
    """
    if not req.user or not req.user.is_authenticated:
        return JsonResponse({"structure": "<h1>اطلاعاتی یافت نشد، مجدد وارد شوید</h1>"})

    user = req.user
    member = Member.objects.get(user_profile=user)

    if member.position != "admin":
        return JsonResponse({"admin_all": "<h1>nothing here</h1>"})

    members = Member.objects.all()
    cards = ""
    for member in members:
        cards += f"""
            <div class="card">
                <ul>
                    <li><img src="{member.profile_picture.url}" alt=""></li>
                    <li><ul><li>نام:</li><li>{member.user_profile.first_name} {member.user_profile.last_name}</li></ul></li>
                    <li><ul><li>نقش:</li><li>{member.position}</li></ul></li>
                    <li><ul><li>کد ملی:</li><li>{member.national_code}</li></ul></li>
                </ul>
            </div>
        """
    # national code = profile picture - position
    structure = f"""
        <div class="card_container">    
            {cards}
        </div>
    """

    data = {
        "structure": structure,
    }
    return JsonResponse(data)


def member_courses(req):
    if not req.user or not req.user.is_authenticated:
        return JsonResponse({"courses": "<h1>اطلاعاتی یافت نشد، مجدد وارد شوید</h1>"})
    user = req.user
    cards = ""
    member = Member.objects.get(user_profile=user)
    if member.position == "student":
        courses = Course.objects.filter(students__member_profile__user_profile_id=user.id)
        for course in courses:
            cards += f"""
                <div class="card">
                <ul>
                    <li><ul><li>نام کلاس:</li><li>{course.name}</li></ul></li>
                    <li><ul><li>تعداد دانشجویان:</li><li>{course.students.count()}</li></ul></li>
                    <li><ul><li>نام استاد:</li><li>{course.teacher}</li></ul></li>
                </ul>
            </div>
            """
    structure = f"""
        <div class="card_container">    
            {cards}
        </div>
    """
    return JsonResponse({"structure": structure})


def student_scores(req):
    if not req.user or not req.user.is_authenticated:
        return JsonResponse({"courses": "<h1>اطلاعاتی یافت نشد، مجدد وارد شوید</h1>"})
    user = req.user
    member = Member.objects.get(user_profile=user)
    if member.position != "student":
        return JsonResponse({"courses": "<h1>شما دانش اموز نیستید!</h1>"})
    student = Student.objects.get(member_profile=member)
    cards = ""
    scores = Score.objects.filter(student__member_profile=member)
    for score in scores:
        cards += f"""
            <div class="card">
                <ul>
                    <li><ul><li>نام درس:</li><li>{score.course}</li></ul></li>
                    <li><ul><li>نمره:</li><li>{score.score}</li></ul></li>
                </ul>
            </div>
            """

    structure = f"""
            <div class="card_container">    
                {cards}
            </div>
        """

    data = { "structure": structure }
    return JsonResponse(data)
