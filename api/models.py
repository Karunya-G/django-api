from django.db import models

class Annote(models.Model):
    label_data = models.JSONField()

class Imagess(models.Model):
    img_data = models.ImageField(upload_to ="allimages", blank= True)