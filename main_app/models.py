from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Badge(models.Model):
    badge_name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='badges',blank=False)
    min_score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    def __str__(self):
        return self.badge_name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level_reached = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Badge_Allot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

    def __str__(self):
        return (self.user.username + " :- " + self.badge.badge_name)

class Session(models.Model):
    id = models.IntegerField(blank=False,unique=True,primary_key=True)
    session_id = models.CharField(unique=True, max_length=10, blank=False, default="")

    PILLAR = (
        ('SELF MANAGEMENT', 'Self Management'),
        ('SELF AWARENESS', 'Self Awareness'),
        ('RESPONSIBLE DECISION MAKING', 'Responsible Decision Making'),
        ('SOCIAL AWARENESS', 'Social Awareness'),
        ('RELATIONSHIP SKILLS', 'Relationship Skills')
    )

    session_name = models.CharField(max_length=64, choices=PILLAR)
    quality_focused = models.CharField(max_length=50,blank=False)
    check_in_content = models.TextField(blank=True)
    introduce_to_session = models.TextField(blank=True)
    close_content = models.TextField(blank=True)
    # learning_to = models.TextField(blank=True)
    how_am_i_learning = models.TextField(blank=True)
    achievements_today = models.TextField(blank=True)

    def __str__(self):
        return (self.session_id + " - " + self.session_name + " | " + self.quality_focused)

class Media_Content(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    serial_number = models.IntegerField(default=0)
    media_content = models.FileField(upload_to='content',blank=True)
    text_content = models.TextField(blank=True)

    def __str__(self):
        return (self.session.session_id + self.serial_number)

class Creative_Space(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='creative_space',blank=True)
    any_text = models.TextField(blank=True)

    def __str__(self):
        return self.session.session_name

class Questions_Mapping(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=0)
    question = models.CharField(max_length=100, default="")
    option_A = models.CharField(max_length=100, default="")
    option_B = models.CharField(max_length=100, default="")
    option_C = models.CharField(max_length=100, default="")
    option_D = models.CharField(max_length=100, default="")
    correct_answer = models.CharField(max_length=100, default='A')

    def __str__(self):
        return (self.session.session_name.name + self.question_number)

class Result_Session(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback
