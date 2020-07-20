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


class Order_name(models.Model):
    order = models.PositiveIntegerField()


class Summary_wihda(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    order_name = models.ForeignKey(
        Order_name, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    wihda = models.ForeignKey(Wihda, on_delete=models.CASCADE)

    def str(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Summary_wihdat'


class Exercise(models.Model):
    name = models.CharField(max_length=150, default='التمرين __')
    short_name = models.CharField(max_length=15, blank=True, null=True)
    order_name = models.ForeignKey(
        Order_name, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField()
    solution_link = models.URLField(null=True, blank=True)
    wihda = models.ForeignKey(Wihda, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name[:10]} {self.wihda.name}'

    class Meta:
        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'
