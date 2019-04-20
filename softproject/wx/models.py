from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Pet(models.Model):
    PetKind = models.CharField(max_length=20)
    intro = models.TextField()
    maxOld = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    Morphological_characteristic = models.TextField()
    Personality_characteristics = models.TextField()
    Breeding_method = models.TextField()
    comb = models.TextField()
    imgName = models.CharField(max_length=20)

    class Meta:
        db_table = 't_pet'
