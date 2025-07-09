from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator



# Create your models here.

def validate_password_length(value):
    if len(value) < 8:
        raise ValidationError(
            _('Password must be at least 8 characters long.'),
            params={'value': value},
        )
    

    
class User(models.Model):
    ACADEMIC_YEAR_CHOICES = [
        ('first_year', 'First Year'),
        ('second_year', 'Second Year'),
        ('third_year', 'Third Year'),
        ('fourth_year', 'Fourth Year'),
        ('Graduated', 'Graduated'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        validators=[validate_password_length],
        default='12345678'
    )
    academic_year = models.CharField(
        max_length=20, 
        choices=ACADEMIC_YEAR_CHOICES
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
    max_length=20,
    validators=[MinLengthValidator(11)],
    blank=True,
    null=True
)
    profile_image = models.ImageField(upload_to='profiles/%y/%m/%d', default='/profiles/default.jpg', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.user_name
    
    class Meta:
        ordering = ["user_name"]






class Request(models.Model):

    REQUEST_STATE_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    request_id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    request_state = models.CharField(
        max_length=10, 
        choices=REQUEST_STATE_CHOICES, 
        default='open'
    ) 
    request_date = models.DateTimeField(auto_now_add=True)
    request_description = models.TextField()  
    def __str__(self):
        return self.request_description
    class Meta:
        ordering=["user"]


