from django.db import models
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE = (('full time','Full Time'),('part time','Part Time'),('internship','Internship'))

class Location(models.Model):

    def get_absolute_url(self):
        return reverse('job-create')
        
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
        
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
        
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('job-create')
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
        
    def get_category_id(cls,id):
        category = Category.object.get(pk = id)
        return category
       
class Job(models.Model):
    title = models.CharField(max_length =50)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    jobtype = models.CharField(choices=JOB_TYPE,max_length=15)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    siteurl = models.URLField(max_length=200, null=True, blank=True) 




    def get_absolute_url(self):
        return reverse('index')
        
    def save_job(self):
        self.save()
        
    def delete_job(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def get_all_jobs(cls):
        all_jobs = Job.objects.all()
        return all_jobs
    
    @classmethod
    def get_job_by_id(cls, id):
        a_job = Job.objects.get(id=id)
        return a_job    
    
    @classmethod
    def search_by_category(cls,search_term):
        title = cls.objects.filter(category__name__icontains=search_term)
        return title
