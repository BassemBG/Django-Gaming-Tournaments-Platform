from django.db import models
from django.core.validators import RegexValidator, ValidationError 
from datetime import date


def validate_sponsorship_date(start_date):
        
        today = date.today()

        if start_date < today:
            raise ValidationError("The date cannot be in the past. Please select a date from today onwards.")

        return start_date

# Enumeration for Sponsor Type
class SponsorType(models.TextChoices):
    CORPORATE = 'corporate', 'Corporate'
    SMALL_BUSINESS = 'small_business', 'Small Business'
    GOVERNMENTAL = 'governmental', 'Governmental'
    NO_DEFINED = 'not defined', 'Not Defined' 

# Enumeration for Sponsorship Status
class SponsorshipStatus(models.TextChoices):
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'
    ACTIVE = 'active', 'Active'
    INACTIVE = 'inactive', 'Inactive'
    PENDING = 'pending', 'Pending'
    TERMINATED = 'terminated', 'Terminated'

# Sponsor Model
class Sponsor(models.Model):
    cin_validator = RegexValidator(
        regex = r'\d{8}$',
        message = "this field must contain exactly 8 digits"
    )
    
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message="Please enter a valid email address."
)

    
    identifier = models.CharField(max_length=8,primary_key=True ,null = False, validators = [cin_validator])
    email = models.EmailField(max_length= 254 , unique=True, validators = [email_validator])
    responsible = models.CharField(max_length=255)  
    address = models.CharField(max_length=255)
    website = models.URLField(max_length=200)
    type = models.CharField(
        max_length=50,
        choices=SponsorType.choices,
        default=SponsorType.NO_DEFINED,
    )

    def _str_(self):
        return self.responsible
    
    class Meta:
        verbose_name_plural = 'Sponsors'

#Sponsorship Model
class Sponsorship(models.Model):
    sponsorID = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    #tournamentID = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    
    status = models.CharField(
        max_length=50,
        choices=SponsorshipStatus.choices,
        default=SponsorshipStatus.PENDING,
    )
    sponsorship_amount = models.FloatField()
    start_date = models.DateField(validators=[validate_sponsorship_date])
    end_date = models.DateField()


        
    def clean (self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be set after start date")    

    def _str_(self):
        return f"{self.sponsor}"
    
    class Meta:
        #pour modifier les noms des modèles affichés dans l’interface administrateur
        verbose_name_plural = 'Sponsorships'