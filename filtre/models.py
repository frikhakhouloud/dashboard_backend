from django.db import models

# Create your models here.


class Division(models.Model):
    name =models.CharField(max_length=200)
    description =models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.description}'

class Profit_center(models.Model):
    name =models.CharField(max_length=200)
    description =models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.description}'

    

class Organisation(models.Model):
    name =models.CharField(max_length=200)
    description =models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.description}'

#Range of weeks to show in filter
class Range(models.Model):
    weeks_number=models.IntegerField(default=14)

    def __str__(self):
        return f'{self.weeks_number}'
    
  #apres la creation des model, il faut:
  # 1. créer et configurer la base de données postgres
  # 2.makemigrations, install psycopg2 et migrate
  # 3.importer et enregistrer les tables dans admin
  # 4.create superuser
  #5.runserver et acces au front et à l'espace admin pour ajouter des items