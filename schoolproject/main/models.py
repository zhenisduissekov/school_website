from django.db import models


# Create your models here.
class Lesson(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Teacher(models.Model):
    firstName = models.CharField("Имя", max_length=50)
    lastName = models.CharField("Фамилия", max_length=50)
    className = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Pupil(models.Model):
    firstName = models.CharField("Имя", max_length=50)
    lastName = models.CharField("Фамилия", max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
