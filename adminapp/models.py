from django.db import models

# Create your models here.

app_status_choice = (
    ('Pending' , 'Pending'),
    ('Approved' , 'Approved'),
    ('Denied' , 'Denied'),
)

class Application(models.Model):
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100, null=True, blank=True)
    phone         = models.CharField(max_length=50, null=True, blank=True)
    dob           = models.DateField()
    email         = models.EmailField()
    address       = models.TextField(null=True, blank=True)
    city          = models.CharField(max_length=100, null=True, blank=True)
    country       = models.CharField(max_length=100, null=True, blank=True)
    religion      = models.CharField(max_length=100, null=True, blank=True)
    job           = models.CharField(max_length=100, null=True, blank=True)
    annual_income = models.CharField(max_length=100, null=True, blank=True)
    app_status    = models.CharField(max_length=100,choices=app_status_choice, default='Pending')
    dateapplied   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name)
