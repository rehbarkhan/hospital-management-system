from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']      # mainly using for pagination.


class Profile(ModelBase):
    _gender = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=_gender)

    address = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    discharged_date = models.DateTimeField(editable=False, null=True, blank=True)
    @property
    def discharge_patient(self):
        from django.utils import timezone
        self.discharge_patient = timezone.now()
class User(AbstractUser):
    email = models.EmailField(max_length=120, unique=True)
    Profile = models.OneToOneField(Profile, related_name='UserProfile', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class InventoryType(ModelBase):
    inventory_type = models.CharField(max_length=120)

class PatientTestReportName(ModelBase):
    report_name = models.CharField(max_length=120)
    def __str__(self):
        return str(self.report_name)
    

class PatientTestReport(ModelBase):
    ReportName = models.ForeignKey(PatientTestReportName, on_delete=models.CASCADE, related_name='PatientTestReportReportName')
    PatientName = models.ForeignKey(Profile, related_name='PatientTestReportPatientName', on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Profile, related_name='PatientTestReportDoctor', on_delete=models.CASCADE)

class Inventory(ModelBase):
    InventoryType = models.ForeignKey('InventoryType', on_delete=models.CASCADE, related_name='InventoryInventoryType')
    count = models.PositiveBigIntegerField()


    @property
    def increase(self, increased_by):
        self.count += increased_by
    
    @property
    def decreased(self, decreased_by):
        self.count -= decreased_by


class BillingItems(ModelBase):
    item_type = models.CharField(max_length=120)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.item_type)

class Billing(ModelBase):
    User = models.ForeignKey(User, related_name='BillingUser', on_delete=models.CASCADE)
    paid = models.PositiveSmallIntegerField(editable=False)
    BillingItems = models.ManyToManyField('BillingItems')

    @property
    def total(self):
        sum = 0
        for data in self.BillingItems.objects.all():
            sum += data.price
        return sum

