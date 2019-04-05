from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class NeighbourHood(models.Model):
    name = models.CharField(max_length = 30,null = True)
    location = models.CharField(max_length = 30,null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    # admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_neiborhood(self):
        NeighbourHood.objects.filter(id = self.pk).delete() 
    
    def find_neiborhood(self):
        NeighbourHood.objects.filter(id = self.pk).find(neigborhood_id) 


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