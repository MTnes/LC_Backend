from django.db import models

# Create your models here.

class Badge(models.Model):
    badge_name = models.CharField(max_length=64, blank=False)
    image = models.ImageField(upload_to='badges',blank=False)
    min_score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    def __str__(self):
        return self.badge_name


class Session(models.Model):
    id = models.IntegerField(blank=False,unique=True,primary_key=True)
    PILLAR = (
        ('SELF MANAGEMENT', 'Self Management'),
        ('SELF AWARENESS', 'Self Awareness'),
        ('RESPONSIBLE DECISION MAKING', 'Responsible Decision Making'),
        ('SOCIAL AWARENESS', 'Social Awareness'),
        ('RELATIONSHIP SKILLS', 'Relationship Skills')
    )
    compitency = models.CharField(max_length=64, choices=PILLAR)
    theme = models.CharField(max_length=64,blank=True)
    name = models.CharField(max_length=128,blank=True)
    index = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
    moral = models.TextField(blank=True)

    def __str__(self):
        return (self.name)

class Media_Content(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    serial_number = models.IntegerField(default=0)
    media_content = models.ImageField(upload_to='content',blank=True)
    text_content = models.TextField(blank=True)

    def __str__(self):
        return (self.session.name + " - " + str(self.serial_number))

class Questions_Mapping(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.CharField(max_length=128, default="", blank = False)
    option_A = models.CharField(max_length=128, default="", blank = False)
    option_B = models.CharField(max_length=128, default="", blank = False)
    option_C = models.CharField(max_length=128, default="", blank = False)
    option_D = models.CharField(max_length=128, default="", blank = True)
    OPTIONS = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    )
    correct_answer = models.CharField(max_length=64, choices=OPTIONS)

    def __str__(self):
        return (self.session.name + " - " + self.question)


class Feedback(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback
