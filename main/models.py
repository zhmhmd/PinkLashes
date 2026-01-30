from django.db import models
from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class Service(models.Model):
    img = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Master(models.Model):
    POSITION_CHOICES = [
        ('top_master','Top Master'),
        ('master','Master'),
        ('trainee','Trainee'),
    ]
    img = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)
    name = models.CharField(verbose_name='Название', max_length=150)
    position = models.CharField(verbose_name='Позиция', choices=POSITION_CHOICES, default='master')
    experience = models.CharField(verbose_name='Опыт', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=1500)
    telegramm = models.URLField(verbose_name='Телеграмм', null=True, blank=True)
    instagram = models.URLField(verbose_name='Инстаграм', null=True, blank=True)
    tiktok = models.URLField(verbose_name='Тик Ток', null=True, blank=True)
    whatsapp = models.URLField(verbose_name='Ваттсап', null=True, blank=True)
    youtube = models.URLField(verbose_name='Ютуб', null=True, blank=True)
    services = models.ManyToManyField(Service, verbose_name='сервисы')

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Gallery(models.Model):
    img = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Review(models.Model):
    SCORE_CHOICES=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    score = models.IntegerField(verbose_name='Оценка', choices=SCORE_CHOICES, default=1)
    comment = models.TextField(verbose_name='Комментарий', max_length=1500)

    def __str__(self):
        return f"{self.id} - Оценка мастера {self.master}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class TypeOfService(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    price = models.PositiveIntegerField(verbose_name='Цена')
    master = models.ManyToManyField(Master, verbose_name='Мастер')

    def __str__(self):
        return f"{self.id} - Тип услуги {self.title}"
    
    class Meta:
        verbose_name = 'Тип сервиса'
        verbose_name_plural = 'Типы сервесов'

    
class SignUp(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    services = models.ManyToManyField(Service, verbose_name='сервисы')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    date = models.DateField(verbose_name='Дата', auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name='Время', auto_now=False, auto_now_add=False)
    comment = models.TextField(verbose_name='Комментарий', max_length=1500)

    def __str__(self):
        return f"{self.id} - Записаться {self.name}"
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'