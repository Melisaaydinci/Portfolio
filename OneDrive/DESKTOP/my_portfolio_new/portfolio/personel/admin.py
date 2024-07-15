from django.contrib import admin
from .models import PersonelKnowledge,Project,Skill,Service,SocialMedia

@admin.register(PersonelKnowledge)
class PersonelKnowledge(admin.ModelAdmin):
    list_display=['profession']

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display=['name']

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display=['name']

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display=['name']

@admin.register(SocialMedia)
class SocialMedia(admin.ModelAdmin):
    list_display=['name']