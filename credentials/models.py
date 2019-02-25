from django.db import models

# Create your models here.


class AboutMe(models.Model):
    """
    Model to hold information about myself
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Software Developer')
    description = models.TextField()
    address = models.CharField(max_length=500)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='credentials/static/img')

    class Meta:

        verbose_name_plural = "About Me"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_fullname(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return self.first_name


class Expertise(models.Model):
    """
    model that displays my expertise skills
    """
    expertise = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:

        verbose_name_plural = 'Expertise'


class Skill(models.Model):
    """
    model that holds the skills I possess and still learning
    """

    skill = models.CharField(max_length=250)
    percentage = models.IntegerField(default=0, help_text='percentage of competency for this skill')

    def __str__(self):
        return self.skill


class Education(models.Model):
    """"
    model that houses my education over the years
    """
    date = models.CharField(max_length=250)
    education = models.CharField(max_length=250, verbose_name='education')
    institute = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return '%s %s' % (self.date, self.institute)


class Interest(models.Model):
    """
    model that displays my interest
    """
    interest = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.interest


class Project(models.Model):
    """"
    model that houses my projects I've created
    """
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    image = models.ImageField(upload_to='credentials/static/img')

    def __str__(self):
        return self.title


class SocialMedia(models.Model):

    social_name = models.CharField(max_length=100)
    social_icon = models.CharField(max_length=50, default='fa-fa-icon')
    social_link = models.CharField(max_length=300)

    def __str__(self):
        return self.social_name











