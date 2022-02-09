from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=35, default='ZICTA')
    job_title = models.CharField(max_length=40)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.job_title

class Requirements(models.Model):
    job_title = models.ForeignKey(Job, on_delete=models.CASCADE)
    required = models.CharField(max_length=250)

    def __str__(self):
        return self.required

class Applicants(models.Model):
    email = models.EmailField(max_length=30)
    required = models.ManyToManyField(Requirements)

    def __str__(self):
        return self.email
