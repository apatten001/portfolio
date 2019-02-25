from django.db import models

# Create your models here.



CHOICES = (("Recruiter", "Recruiter"), ("Employer", "Employer"), ("Friend","Friend"), ("Other","Other"))


class Recruiter(models.Model):
    """
    THis model will house the recruiters and employers info
    that may reach out via the website
    """

    position = models.CharField(max_length=50, choices=CHOICES)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return "Hello Arnold I'm %s and I'm a %s." % (self.name, self.position)

