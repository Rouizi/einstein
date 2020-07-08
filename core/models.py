from django.db import models


class School(models.Model):
    school_year = models.CharField(max_length=30)

    def __str__(self):
        return self.school_year


class Wihda(models.Model):
    name = models.CharField(max_length=70)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Wihdat'


class Exercise(models.Model):
    name = models.CharField(max_length=150, default='التمرين __')
    link = models.URLField()
    wihda = models.ForeignKey(Wihda, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name[:10]} {self.wihda.name}'

    class Meta:
        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'
