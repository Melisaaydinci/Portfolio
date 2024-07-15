from ninja import Schema

class PersonelKnowledgeSerializer(Schema):
    full_name: str
    mail: str
    phone: str

class SkillSerializer(Schema):
    
    name: str
    definition: str

class ProjectSerializer(Schema):
    
    name: str
    definition: str

class ServiceSerializer(Schema):
   
    name: str
    definition: str