from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os



SEMESTER=[
    ('1','semester 1'),
    ('2','semester 2'),
    ('3','semester 3'),
    ('4','semester 4'),
    ('5','semester 5'),
    ('6','semester 6'),
    ('7','semester 7'),
    ('8','semester 8'),
]


DEPARTMENT=[
    ('CE','Computer engineering'),
    ('MH','Mechanical engineering'),
    ('EC','Electrical engineering'),
    ('CH','Chemical engineering'),
]

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    semester = models.CharField(max_length=1,choices=SEMESTER)
    department = models.CharField(max_length=4,choices=DEPARTMENT)
    document = models.FileField(upload_to='files/')
    def __str__(self):
        return self.title
    
    def delete(self,*args,**kwargs):
        if os.path.isfile('media/'+self.document.name):
            os.remove('media/'+self.document.name)
        super(Note, self).delete(*args,**kwargs)



