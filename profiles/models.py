from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    """"Модель профиля пользователя"""
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="profile/", blank=True, null=True) #ВНИМАНИЕ!!!
    email_two = models.EmailField("Доп. e-mail")
    phone = models.CharField("Телефон", max_length=25)
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50, blank=True, null=True)
    slug = models.SlugField("URL", max_length=50, default='')
    # date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    #TODO: Адрес, гео база

    def __str__(self):
        return self.first_name



    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})



    def delete(self, *args, **kwargs):
        for advert in self.advert_objects.all():
            advert.delete()
            super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




