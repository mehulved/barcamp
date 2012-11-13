from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Camp(models.Model): 
    name = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    venue_address = models.TextField(null=True, blank=True)
    venue_latitude = models.FloatField(null=True, blank=True)
    venue_longitude = models.FloatField(null=True, blank=True)
    volunteers = models.ManyToManyField(UserProfile, related_name="volunteer",
            null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    # Email address is stored in user model
    # Do we want phone number? 

class TimeSlot(models.Model): 
    camp = models.ForeignKey(Camp)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Track(models.Models): 
    camp = models.ForeignKey(Camp)
    room = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)

class Session(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    speaker = models.ManyToManyField(UserProfile, related_name="speaker")
    camp = models.ForeignKey(Camp)
    slot = models.ManyToManyField(TimeSlot, null=True, blank=True)
    track = models.ForeignKey(Track, null=True, blank=True)
    attendees = models.ManyToManyKey(UserProfile, related_name="attendee",
            null=True, blank=True)

    # Need to ensure that a given session cannot overlap with another session 
    # in a given track and a given time slot at a given barcamp. 
