from django.db import models

# Create your models here.
class create_resume(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=254)
    city=models.CharField(max_length=500, default="null")
    pincode=models.IntegerField()
    state=models.CharField(max_length=100, default="null" )
    country=models.CharField(max_length=100, default="null")
    address=models.CharField(max_length=1000, default="null")
    dob=models.DateField()
    gender=models.CharField(max_length=100, default="null")
    aboutyou=models.TextField(max_length=1000, default="null" )
    class meta:
        db_table = "main_create_resume"
    
class degree_info(models.Model):
    degree=models.TextField(max_length=1000)
    degreecity=models.TextField(max_length=1000)
    university=models.TextField(max_length=1000)
    degreepercent=models.TextField(max_length=100)
    degreestartmonth=models.CharField(max_length=1000)
    degreestartyear=models.IntegerField()
    degreeendmonth=models.CharField(max_length=1000)
    degreeendyear=models.IntegerField()
    class meta:
        db_table = "main_degree_info"
    
class school_info(models.Model):
    schoolboard=models.TextField(max_length=1000)
    schoolcity=models.TextField(max_length=1000)
    school=models.TextField(max_length=1000)
    schoolstartmonth=models.CharField(max_length=1000)
    schoolstartyear=models.IntegerField()
    schoolendmonth=models.CharField(max_length=1000)
    schoolendyear=models.IntegerField()
    schoolpercent=models.TextField(max_length=100)
    class meta:
        db_table = "main_school_info"

class intermediate_info(models.Model):
    intermediate=models.TextField(max_length=1000)
    intercity=models.TextField(max_length=1000)
    college=models.TextField(max_length=1000)
    interstartmonth=models.CharField(max_length=1000)
    interstartyear=models.IntegerField()
    interendmonth=models.CharField(max_length=1000)
    interendyear=models.IntegerField()
    interpercent=models.TextField(max_length=100)
    class meta:
        db_table = "main_intermediate_info"


class job_details(models.Model):
    jobtitle=models.TextField(max_length=1000)
    jobcity=models.TextField(max_length=1000)
    companyname=models.TextField(max_length=1000)
    jobstartmonth=models.CharField(max_length=1000)
    jobstartyear=models.IntegerField()
    jobendmonth=models.CharField(max_length=1000)
    jobendyear=models.IntegerField()
    project=models.TextField(max_length=1000)
    internship=models.TextField(max_length=1000)
    projectteam=models.TextField(max_length=1000)
    position=models.TextField(max_length=1000)
    projecttitle=models.TextField(max_length=1000)
    class meta:
        db_table = "main_job_details"
    

class extra_activities(models.Model):
   hobbies1=models.CharField(max_length=1000)
   hobbies2=models.CharField(max_length=1000)
   achivements1=models.CharField(max_length=1000)
   achivements2=models.CharField(max_length=1000)
   extra=models.CharField(max_length=1000)
   strengths1=models.CharField(max_length=1000)
   strengths2=models.CharField(max_length=1000)
   language=models.CharField(max_length=1000)
   class meta:
        db_table = "main_extra_activities"


class skills(models.Model):
   programSkill=models.TextField(max_length=1000)
   operatingSkill=models.TextField(max_length=1000)
   DatabaseSkill=models.TextField(max_length=1000)
   IDESkill=models.TextField(max_length=1000)
   FrameworkSkill=models.TextField(max_length=1000)
   otherSkill=models.TextField(max_length=1000)
   class meta:
        db_table = "main_skills"