from ninja import NinjaAPI
from .models import PersonelKnowledge,Skill,Project,Service,SocialMedia
from .serializers import PersonelKnowledgeSerializer,SkillSerializer,ServiceSerializer,ProjectSerializer

api=NinjaAPI()

@api.get("/get_personel")
def get_personel(request):
    knowledge=PersonelKnowledge.objects.first()
    photo_url = request.build_absolute_uri(knowledge.photo.url)
    cv_url= request.build_absolute_uri(knowledge.cv.url)
    print("url im şu",photo_url)
    return {"first_name":knowledge.first_name,
            "last_name":knowledge.last_name,
            "profession":knowledge.profession,
            "definition":knowledge.definition,
            "photo":photo_url,
            "mail":knowledge.mail,
            "phone":knowledge.phone_number,
            "cv":cv_url,
            }


@api.get("/get_skill/{skill_name}")
def get_skill(request,  skill_name: str):
    try:
        instance = Skill.objects.get(name=skill_name)
        return {"name":instance.name,
            "definition":instance.definition,
            }
    except Skill.DoesNotExist:
        return {"error": "Skill not found"}
    except Exception as e:
        return {"error": str(e)}
    
@api.get("/get_service/{service_name}")
def get_service(request,  service_name: str):
    try:
        instance = Service.objects.get(name=service_name)
        return {"name":instance.name,
            "definition":instance.definition,
            }
    except Service.DoesNotExist:
        return {"error": "Service not found"}
    except Exception as e:
        return {"error": str(e)}
    
@api.get("/get_project/{project_name}")
def get_project(request,  project_name: str):
    try:
        instance = Project.objects.get(name=project_name)
        return {"name":instance.name,
            "definition":instance.definition,
            }
    except Project.DoesNotExist:
        return {"error": "Project not found"}
    except Exception as e:
        return {"error": str(e)}

@api.get("/get_skills")
def get_skills(request):
    skills=Skill.objects.all()
    return [{"icon":request.build_absolute_uri(skill.icon.url),
             "name":skill.name,
             "definition":skill.definition  
            }
            for skill in skills]

@api.get("/get_projects")
def get_projects(request):
    projects=Project.objects.all()
    return [{"photo":request.build_absolute_uri(project.photo.url),
             "name":project.name,
             "definition":project.definition  
            }
            for project in projects]

@api.get("/get_services")
def get_services(request):
    services=Service.objects.all()
    return [{"id":service.id,
             "name":service.name,
            "definition":service.definition  
            }

            for service in services]

@api.get("/get_socials")
def get_socials(request):
    socials=SocialMedia.objects.all()
    return [{"icon":request.build_absolute_uri(social.icon.url),
            "name":social.name,
            "link":social.link,
            "definition":social.definition,
            }
            for social in socials]

@api.post("/create_skill")
def create_skill(request, data_in: SkillSerializer):
    try:
        skill = Skill.objects.create(
            name=data_in.name,
            definition=data_in.definition
        )
        return {"message": "Skill created successfully", "skill_id": skill.id}
    except Exception as e:
        return {"error": str(e)}

@api.post("/create_service")
def create_service(request, data_in: ServiceSerializer):
    try:
        service = Service.objects.create(
            name=data_in.name,
            definition=data_in.definition
        )
        return {"message": "Service created successfully", "service_id": service.id}
    except Exception as e:
        return {"error": str(e)}
    
@api.post("/create_project")
def create_project(request, data_in: ProjectSerializer):
    try:
        project = project.objects.create(
            name=data_in.name,
            definition=data_in.definition
        )
        return {"message": "Service created successfully", "project_id": project.id}
    except Exception as e:
        return {"error": str(e)}
    




@api.put("/update_personel")
def update_personel(request, data_in: PersonelKnowledgeSerializer):
    try:
        instance = PersonelKnowledge.objects.first()
        if instance:
            instance.full_name = data_in.full_name
            instance.mail = data_in.mail
            instance.phone_number = data_in.phone
            instance.save()
            return {"message": "Personel information updated successfully"}
        else:
            return {"error": "Personel knowledge not found"}
    except Exception as e:
        return {"error": str(e)}

@api.put("/update_service/{service_id}")
def update_service(request,  service_id: int,data_in: ServiceSerializer):
    try:
        instance = Service.objects.get(id=service_id)
        instance.name = data_in.name
        instance.definition = data_in.definition
        instance.save()
        return {"message": "Service updated successfully"}
    except Service.DoesNotExist:
        return {"error": "Service not found"}
    except Exception as e:
        return {"error": str(e)}

@api.put("/update_project/{project_id}")
def update_project(request,  project_id: int,data_in: ProjectSerializer):
    try:
        instance = Project.objects.get(id=project_id)
        instance.name = data_in.name
        instance.definition = data_in.definition
        instance.save()
        return {"message": "Project updated successfully"}
    except Project.DoesNotExist:
        return {"error": "Project not found"}
    except Exception as e:
        return {"error": str(e)}
    
@api.put("/update_skill/{skill_id}")
def update_skill(request, skill_id: int,data_in: SkillSerializer):
    try:
        instance = Skill.objects.get(id=skill_id)
        instance.name = data_in.name
        instance.definition = data_in.definition
        instance.save()
        return {"message": "Skill updated successfully"}
    except Skill.DoesNotExist:
        return {"error": "Skill not found"}
    except Exception as e:
        return {"error": str(e)}