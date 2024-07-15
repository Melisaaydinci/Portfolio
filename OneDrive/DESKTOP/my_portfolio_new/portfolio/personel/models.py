from django.db import models

def hero_directory_path(instance,filename):
    return f'Hero/{filename}'

def proje_directory_path(instance,filename):
    return f'Projects/{filename}'

def service_directory_path(instance,filename):
    return f'Services/{filename}'

def skill_directory_path(instance,filename):
    return f'Skills/{filename}'
def icon_directory_path(instance,filename):
    return f'Icons/{filename}'

class PersonelKnowledge(models.Model):
    profession=models.CharField(unique=True,max_length=100,null=True)
    definition=models.TextField(max_length=1000,null=True)
    photo=models.ImageField(upload_to=hero_directory_path,null=True)
    first_name=models.CharField(unique=True,max_length=50,null=True)
    last_name=models.CharField(unique=True,max_length=50,null=True)
    mail=models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14)
    cv=models.FileField(null=True)

    def __str__(self):
         return f"Personel Knowledge"
    
class Skill(models.Model):
    icon=models.ImageField(upload_to=skill_directory_path,null=True)
    name=models.CharField(unique=True,max_length=25,null=True)
    definition=models.CharField(null=True,max_length=200)

    def __str__(self):
         return self.name
    
class Service(models.Model):
    icon=models.ImageField(upload_to=service_directory_path,null=True)
    name=models.CharField(unique=True,max_length=25,null=True)
    definition=models.CharField(null=True,max_length=200)

    def __str__(self):
         return self.name

class Project(models.Model):
    photo=models.ImageField(upload_to=proje_directory_path,null=True)
    name=models.CharField(unique=True,max_length=25,null=True)
    definition=models.TextField(max_length=1000,null=True)

    def __str__(self):
         return self.name

class SocialMedia(models.Model):
    icon=models.ImageField(upload_to=proje_directory_path,null=True)
    name=models.CharField(unique=True,max_length=25,null=True)
    link=models.CharField(unique=True,max_length=50,null=True)
    definition=models.CharField(null=True,max_length=200)

    def __str__(self):
         return self.name