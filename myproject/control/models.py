from django.db import models

# Create your models here.

class User(models.Model):
    ACADEMIC_YEAR_CHOICES = [
        ('first_year', 'First Year'),
        ('second_year', 'Second Year'),
        ('third_year', 'Third Year'),
        ('fourth_year', 'Fourth Year'),
        ('Graduated','Graduated'),
    ]
    
    user_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=255, unique=True) 
    academic_year = models.CharField(
        max_length=20, 
        choices=ACADEMIC_YEAR_CHOICES
    )
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profiles/%y/%m/%d',default='/profiles/24/11/20/default.jpg', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
    class Meta:
        ordering=["user_name"]






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
    related_file = models.FileField(upload_to='request_files/%y/%m/%d')
    def __str__(self):
        return self.user.user_name
    class Meta:
        ordering=["user"]


