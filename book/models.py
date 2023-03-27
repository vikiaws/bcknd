from django.db import models

# Create your models here.
def upload_path(instance,filename):
    return '/'.join([filename])
class Beeline(models.Model):
    beeLine_Request_Number = models.CharField(max_length=30)
    job_description = models.CharField(max_length=500) 
    department = models.CharField(max_length=100)
    no_of_positions = models.IntegerField()
    priority = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    cv_DeadLine = models.DateField()
    billing_Rate = models.CharField(max_length=100)
    hours_per_week = models.IntegerField()
    contact_person = models.CharField(max_length=30)
    date_request = models.DateField()
    file= models.FileField(null=True,blank=True,upload_to=upload_path,default='settings.MEDIA_ROOT/anonymous.jpg')
   
    

    


class Profile(models.Model):
    current_Status = models.CharField(max_length=100)
    name_of_candidate = models.CharField(max_length=100)
    prodapt_practice = models.CharField(max_length=30)
    prodapt_POC = models.CharField(max_length=50)
    next_step = models.CharField(max_length=200)
    dutch_Language = models.CharField(max_length=5)
    location_relocation = models.CharField(max_length=30)
    experience = models.IntegerField()
    #resume_Shared = models.CharField(max_length=5)
    client_Interview = models.CharField(max_length=5)
    cv_Attachment = models.FileField(null=True,blank=True,upload_to=upload_path)
    comments = models.CharField(max_length=1000,default=False)
    beeline = models.ForeignKey(Beeline,related_name="beeline", on_delete=models.CASCADE)


# class Upload(models.Model):
#     name= models.FileField(null=True,blank=True,upload_to=upload_path)


