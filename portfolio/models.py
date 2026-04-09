from django.db import models

class Computed(models.Model):  
    input = models.IntegerField()
    output = models.IntegerField()
    time_computed = models.DateTimeField(null=True)

    def __str__(self):
        return(f"{self.input} -> {self.output}")


