from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Rent
USER = (
('', 'Select User'),
('Owner', 'Owner'),
('Agent', 'Agent'),
)
PROPERTY_FOR = (
('', 'Select Property For'),
('Residential', 'Residential'),
('Commercial', 'Commercial'),
)
CITY= (
('', 'Select City'),
('Dehli','Delhi'),
('Mumbai','Mumbai'),
('Kolkata', 'Kolkata'),
('Channai', 'Channai'),
('Noida','Noida'),
('Gurugram', 'Gurugram'),
('Dehradun','Dehradun'),
('Bangluru','Bangluru'),
('Pune','Pune'),
)
PARKING = (
('', 'Select Parking'),
('Available, Closed', 'Available, Closed'),
('Available, Open', 'Available, Open'),
('Not Available', 'Not Available'),
)
FURNISHED_STATE=(
('', 'Select Furnished state'),
('Not Furnished', 'Not Furnished'),
('Semi-Furnished','Semi-Furnished'),
('Full Furnished','Full Furnished'),
)
PROPERTY_TYPE= (
('', 'Select Property Type'),
('1BHK','1 BHK'),
('2BHK','2 BHK'),
('3BHK','3 BHK'),
('4BHK','4 BHK'),
('5BHK','5 BHK'),
('6BHK','6 BHK'),
)
BATHROOM = (
('', 'Select bathroom'),
('1', '1 Bathroom'),
('2', '2 Bathroom'),
('3', '3 Bathroom'),
('4', '4 Bathroom'),
)
BALCONIES = (
('', 'Select Balcony'),
('1', '1 Balcony'),
('2','2 Balconies'),
('3','3 Balconies'),
('4','4 Balconies'),
)

class Rent(models.Model):
    user_info = models.CharField(max_length=10, choices=USER)
    property_for = models.CharField(max_length=50, choices=PROPERTY_FOR)
    city = models.CharField(max_length=25, choices=CITY)
    address = models.TextField(max_length = 1000)
    property_type = models.CharField(max_length = 10, choices = PROPERTY_TYPE)
    bedroom = models.PositiveIntegerField(blank=False, null=True)
    bathroom = models.CharField(max_length = 5, choices = BATHROOM)
    balconies = models.CharField(max_length = 5, choices = BALCONIES)
    parking = models.CharField(max_length = 50, choices = PARKING)
    furnished_state = models.CharField(max_length = 50, choices = FURNISHED_STATE)
    monthly_charges = models.PositiveIntegerField(blank=False, null=True)
    extra_wases = models.PositiveIntegerField(blank=False, null=True)
    facing =  models.CharField(max_length = 15, null=True)
    image1 = models.FileField(null=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    image4 =  models.FileField(null=True)

    # model forms
    def get_absolute_url(self):
        return reverse('property_portal:rent', kwargs = {'pk', self.pk})

    def __str__(self):
        return self.property_type+" : "+ self.address

#buy
class Buy(models.Model):
    user_info = models.CharField(max_length=10, choices=USER)
    property_for = models.CharField(max_length=50, choices=PROPERTY_FOR)
    city = models.CharField(max_length=25, choices=CITY)
    address = models.TextField(max_length = 1000)
    property_type = models.CharField(max_length = 10, choices = PROPERTY_TYPE)
    bedroom = models.PositiveIntegerField(blank=False, null=True)
    bathroom = models.CharField(max_length = 5, choices = BATHROOM)
    balconies = models.CharField(max_length = 5, choices = BALCONIES)
    parking = models.CharField(max_length = 50, choices = PARKING)
    furnished_state = models.CharField(max_length = 50, choices = FURNISHED_STATE)
    price = models.CharField(max_length= 20)
    facing =  models.CharField(max_length = 15, null=True)
    image1 = models.FileField(null=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    image4 =  models.FileField(null=True)

    def get_absolute_url(self):
        return reverse('property_portal:buy', kwargs = {'pk', self.pk})

    def __str__(self):
        return self.property_type+" : "+ self.address

# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True, default = 0)
    city = models.CharField(max_length = 15, null=True, default = '')


    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user = kwargs['instance'])

    post_save.connect(create_profile, sender = User)
