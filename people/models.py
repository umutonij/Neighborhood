from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class NeighborHood(models.Model):
    name = models.CharField(max_length = 30,null = True)
    location = models.CharField(max_length = 30,null = True)
    post = models.CharField(max_length = 60,null = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    # admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_neiborhood(self):
        self.delete() 
    
    def find_neiborhood(self):
        self.find(neigborhood_id) 


    def update_neiborhood(self):
        self.objects.filter(id = self.pk).update(**kwargs) 
    
    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts 

    

    
    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains = search_term)
        return project

class User(models.Model):
    name = models.CharField(max_length = 30,null = True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete = models.CASCADE, null=True)
    email_address = models.CharField(max_length = 30,null = True)

    

class Business(models.Model):
    business_name = models.CharField(max_length = 30,null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    neighborhood_id = models.ForeignKey(NeighborHood, on_delete = models.CASCADE, null=True)
    business_email_address = models.CharField(max_length = 30,null = True)
    
    def __str__(self):
            return self.business_name

    def update_business(self):
        self.objects.filter(id = self.pk).update(**kwargs) 

    def find_business(self):
        self.find(business_id) 

    def delete_business(self):
        self.delete() 

    def create_business(self):
        self.create() 

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = HTMLField()
    profile_pic = models.ImageField(upload_to='images/')
    contact_info= models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles




