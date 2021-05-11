import datetime
from django.db import models
from django.utils import timezone
from PIL import Image
from django import forms
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    role_in_team = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=200)
    official_pix = models.ImageField()

    def __str__(self) :
        return self.name

class Experiece(models.Model) :
    id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    from_date = models.CharField(max_length=200)
    to_date = models.DateField()
    place = models.DateField()
    role = models.TextField()

    def __str__(self) :
        return self.role


class Education(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    year = models.DateField()
    certification = models.CharField(max_length=200)
    class_of_degree = models.CharField(max_length=200)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self) :
        return self.certification

class Skills(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill1 = models.DateField()
    skill2 = models.CharField(max_length=200)
    skill3 = models.CharField(max_length=200)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self) :
        return self.certification

class Bios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    home_add = models.CharField(max_length=200)
    dob = models.DateField(default=0)
    phone_n = models.IntegerField(default=0)
    height = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

    def was_published_recently(self) :
        now = timezone.now()
        return now - dob

class PhotoGallery(models.Model):
    id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    pix1 = models.ImageField()
    pix2 = models.ImageField()
    pix3 = models.ImageField()
    pix4 = models.ImageField()
    pix5 = models.ImageField()


class Contacts(forms.Form) :
    emails = forms.EmailField()
    message = forms.TextField()


    def __str__(self) :
        return self.emails

