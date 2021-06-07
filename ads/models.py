from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    company = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    desc = models.TextField()
    
    industries = [
        #('skrot ktory jest przechowywany w bazie danych', 'pelna nazwa widoczna dla uzytkownika')
        ('','Choose industry'),
        ('re', 'Real estate'),
        ('ht', 'Health'),
        ('at', 'Automotive'),
        ('ft', 'Fitness'),
    ]
    industry = models.CharField(max_length=2, choices=industries, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #likes - ManyToManyField

    def __str__(self):
        return self.company

    def display_industry(self):
        for industry in self.industries:
            if self.industry in industry:
                toDisplay = industry[1]
        return toDisplay
