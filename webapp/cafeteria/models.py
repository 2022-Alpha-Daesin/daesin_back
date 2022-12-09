from django.db import models

# Create your models here.
class Cafeteria(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.date} : {self.name}'


class Menu(models.Model):
    division = models.CharField(max_length=25)
    food = models.TextField()
    cafeteria = models.ForeignKey(Cafeteria,on_delete=models.CASCADE,related_name='menus')

    def __str__(self):
        return f'{self.menu.name}-[{self.division}]'