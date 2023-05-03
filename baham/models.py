from django.db import models
class Vehicle(models.Model):
    model_id = models.AutoField(primary_key=True, db_column='id')
    vendor = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False, default="Unknown")
class Companion(models.Model):
    companion_id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'companion'
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True, db_column='id')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    companion = models.OneToOneField(Companion, on_delete=models.CASCADE, null=True, blank=True)
class AppUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
class Owner(AppUser):
    pass
class CompanionUser(AppUser):
    pass
