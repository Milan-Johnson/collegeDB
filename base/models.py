from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    headOfDepartment = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    branchCode = models.CharField(max_length=3)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "branches"
    
    def __str__(self):
        return self.name


class Student(models.Model):
    rollNumber = models.IntegerField
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=12)
    emailId = models.CharField(max_length=50)
    dateOfBirth = models.DateField(max_length=8)
    yearOfAddmission = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Subject(models.Model):
    subjectCode = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    semister = models.CharField(max_length=2)
    credit = models.IntegerField()
    hourPerWeek = models.IntegerField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    facultyId = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=12)
    emailId = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    subject = models.ManyToManyField(Subject)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name

# class Teaches(models.Model):
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
