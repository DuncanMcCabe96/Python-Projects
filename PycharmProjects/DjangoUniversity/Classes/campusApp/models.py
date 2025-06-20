from django.db import models

# Created model of University Classes
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    #Creates model manager
    objects = models.Manager()

    def __str__(self):
        return f"{self.campus_name} ({self.state}) - ID: {self.campus_id}"

#removes added 's' that django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"

# Create your models here.
