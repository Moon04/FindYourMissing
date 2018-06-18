from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


class MissingPerson(models.Model):
    userID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=40)
    SecondName = models.CharField(max_length=40)
    Sex = models.CharField(max_length=15)
    AgeBeforeMissing = models.CharField(max_length=3)
    DateOfBirth = models.CharField(max_length=10)
    HairColour = models.CharField(max_length=50)
    EyesColour = models.CharField(max_length=50)
    Weight = models.CharField(max_length=4)
    Height = models.CharField(max_length=4)
    MissingFrom = models.CharField(max_length=150)
    MissingDate = models.CharField(max_length=10)
    RelativeID = models.CharField(max_length=15)
    RelativeRelation = models.CharField(max_length=80)
    Details = models.CharField(max_length=4000)
    MissingPersonImage = models.ImageField(upload_to='missingperson/')

    def get_absolute_url(self):
        return reverse('home:missingDetailsView', kwargs={'pk': self.pk})

    def __str__(self):
        return self.FirstName + self.SecondName


class FoundPerson(models.Model):
    userID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    Sex = models.CharField(max_length=15)
    FoundIn = models.CharField(max_length=150)
    FoundDate = models.CharField(max_length=10)
    Location = models.CharField(max_length=150)
    Details = models.CharField(max_length=4000)
    FoundPersonImage = models.ImageField(upload_to='foundperson/')

    def get_absolute_url(self):
        return reverse('home:foundDetailsView', kwargs={'pk': self.pk})

    def __str__(self):
        return self.id
