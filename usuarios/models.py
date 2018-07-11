from django.db import models


class Usuario(models.Model):
	nome = models.CharField(max_lenght = 45)
	email = models.CharField(max_lenght = 50)
	
		