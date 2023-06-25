from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import create_resume, degree_info, extra_activities, intermediate_info, job_details, school_info, skills
# Create your views here.
def index(request):
    return render(request,'index.html')
def form(request):
    return render(request, 'form.html')
def resume(request):
    return render(request, 'resume.html')
def personal(request):
     print("submitted")
     if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        state=request.POST.get("state")
        country=request.POST.get("country")
        address=request.POST.get("address")
        dob=request.POST.get("dob")
        gender=request.POST.get("gender")
        aboutyou=request.POST.get("aboutyou")
        degree=request.POST.get("degree")
        degreecity=request.POST.get("degreecity")
        university=request.POST.get("school")
        degreestartmonth=request.POST.get("degreestartmonth")
        degreestartyear=request.POST.get("degreestartyear")
        degreeendmonth=request.POST.get("degreeendmonth")
        degreeendyear=request.POST.get("degreeendyear")
        degreepercent=request.POST.get("degreepercent")
        schoolboard=request.POST.get("schoolboard")
        schoolcity=request.POST.get("schoolcity")
        school=request.POST.get("school")
        schoolstartmonth=request.POST.get("schoolstartmonth")
        schoolstartyear=request.POST.get("schoolstartyear")
        schoolendmonth=request.POST.get("schoolendmonth")
        schoolendyear=request.POST.get("schoolendyear")
        schoolpercent=request.POST.get("schoolpercent")
        programSkill=request.POST.get("programSkill")
        operatingSkill=request.POST.get("operatingSkill")
        DatabaseSkill=request.POST.get("DatabaseSkill")
        IDESkill=request.POST.get("IDESkill")
        FrameworkSkill=request.POST.get("FrameworkSkill")
        otherSkill=request.POST.get("otherSkill")
        hobbies1=request.POST.get("hobbies1")
        hobbies2=request.POST.get("hobbies2")
        achivements1=request.POST.get("achivements1")
        achivements2=request.POST.get("achivements2")
        extra=request.POST.get("extra")
        strengths1=request.POST.get("strengths1")
        strengths2=request.POST.get("strengths2")
        language=request.POST.get("language")
        schoolpercent=request.POST.get("schoolpercent")
        schoolpercent=request.POST.get("schoolpercent")        
        jobtitle=request.POST.get("jobtitle")
        jobcity=request.POST.get("jobcity")
        companyname=request.POST.get("companyname")
        jobstartmonth=request.POST.get("jobstartmonth")
        jobstartyear=request.POST.get("jobstartyear")
        jobendmonth=request.POST.get("jobendmonth")
        jobendyear=request.POST.get("jobendyear")
        project=request.POST.get("project")
        internship=request.POST.get("internship")
        projectteam=request.POST.get("projectteam")
        position=request.POST.get("position")
        projecttitle=request.POST.get("projecttitle")
        intermediate=request.POST.get("intermediate")
        intercity=request.POST.get("intercity")
        college=request.POST.get("college")
        interstartmonth=request.POST.get("interstartmonth")
        interstartyear=request.POST.get("interstartyear")
        interendmonth=request.POST.get("interendmonth")
        interendyear=request.POST.get("interendyear")
        interpercent=request.POST.get("interpercent")
       
        create=create_resume(fname=fname,lname=lname,phone=phone,email=email,city=city,pincode=pincode,state=state,country=country,address=address,dob=dob,gender=gender,aboutyou=aboutyou)

        create.save()
        edu=degree_info(degree=degree,degreecity=degreecity,university=university,degreestartmonth=degreestartmonth,degreestartyear=degreestartyear,degreeendmonth=degreeendmonth,degreeendyear=degreeendyear,degreepercent=degreepercent)
        edu.save()
        job=job_details(jobtitle=jobtitle,jobcity=jobcity,companyname=companyname,jobstartmonth=jobstartmonth,jobstartyear=jobstartyear,jobendmonth=jobendmonth,jobendyear=jobendyear,project=project,internship=internship,projectteam=projectteam,position=position,projecttitle=projecttitle)
        job.save()

        extra=extra_activities(hobbies1=hobbies1,hobbies2=hobbies2,achivements1=achivements1,achivements2=achivements2,extra=extra,strengths1=strengths1,strengths2=strengths2,language=language)
        extra.save()

        skill=skills(programSkill=programSkill,operatingSkill=operatingSkill,DatabaseSkill=DatabaseSkill,IDESkill=IDESkill,FrameworkSkill=FrameworkSkill,otherSkill=otherSkill)
        skill.save()
        
        inter=intermediate_info(intermediate=intermediate,intercity=intercity,college=college,interstartmonth=interstartmonth,interstartyear=interstartyear,interendmonth=interendmonth,interendyear=interendyear,interpercent=interpercent)
        inter.save()
        ssc=school_info(schoolboard=schoolboard,schoolcity=schoolcity,school=school,schoolstartmonth=schoolstartmonth,schoolstartyear=schoolstartyear,schoolendmonth=schoolendmonth,schoolendyear=schoolendyear,schoolpercent=schoolpercent)
        ssc.save()

        result1 = create_resume.objects.last()
        result2 = degree_info.objects.last()
        result3 = job_details.objects.last()
        result4 = extra_activities.objects.last()
        result5 = skills.objects.last()
        result6 = intermediate_info.objects.last()
        result7 = school_info.objects.last()
        context = {
            'create_resume':result1,
            'degree_info':result2,
            'job_details':result3,
            'extra_activities':result4,
            'skills':result5,
            'intermediate_info':result6,
            'school_info':result7,
        }   
        return render(request, 'resume.html',context)


def resume(request):
    result1 = create_resume.objects.last()
    result2 = degree_info.objects.last()
    result3 = job_details.objects.last()
    result4 = extra_activities.objects.last()
    result5 = skills.objects.last()
    result6 = intermediate_info.objects.last()
    result7 = school_info.objects.last()
    context = {
            'create_resume':result1,
            'degree_info':result2,
            'job_details':result3,
            'extra_activities':result4,
            'skills':result5,
            'intermediate_info':result6,
            'school_info':result7,
    }
    return render(request, 'resume.html',context)

def updateform(request):
    result1 = create_resume.objects.last()
    result2 = degree_info.objects.last()
    result3 = job_details.objects.last()
    result4 = extra_activities.objects.last()
    result5 = skills.objects.last()
    result6 = intermediate_info.objects.last()
    result7 = school_info.objects.last()
    context = {
            'create_resume':result1,
            'degree_info':result2,
            'job_details':result3,
            'extra_activities':result4,
            'skills':result5,
            'intermediate_info':result6,
            'school_info':result7,
    }
    return render(request, 'updateform.html',context)

def pdf_resume(request):
    result1 = create_resume.objects.last()
    result2 = degree_info.objects.last()
    result3 = job_details.objects.last()
    result4 = extra_activities.objects.last()
    result5 = skills.objects.last()
    result6 = intermediate_info.objects.last()
    result7 = school_info.objects.last()
    context = {
            'create_resume':result1,
            'degree_info':result2,
            'job_details':result3,
            'extra_activities':result4,
            'skills':result5,
            'intermediate_info':result6,
            'school_info':result7,
    }

    template_path = 'pdfresume.html'

    # Create a Django response object, and specify content_type as pdf
    
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="Resume.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response