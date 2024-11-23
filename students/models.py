from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    mobile = models.CharField(max_length=20)
    roll = models.IntegerField()
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name
    
class StudentDetail(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=191)
    mother_name = models.CharField(max_length=191)
    address = models.TextField(null=True)
    nationality = models.CharField(max_length=191)
    birth_date = models.DateField()
    birth_certificate = models.IntegerField()
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.father_name