from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Role, Users, Courses
from django.contrib import messages

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_student(request):
    return render(request, "hod_template/add_student_template.html")

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        device = request.POST.get("device")
        password = request.POST.get("password")
        role_name = request.POST.get("role")
        try:
            user = Users.objects.get(name=name, email=email, password=password, device=device)
            user.save()
            role_name = Role.objects.get(role_name=role_name)
            role_name.save()
            messages.success(request, "Success")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed")
            return HttpResponseRedirect("/add_student")

def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Success")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed")
            return HttpResponseRedirect("/add_course")
        
def scanner(request):
    return render(request, "hod_template/scanner.html")