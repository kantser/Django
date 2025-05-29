from django.db import models

class Service(models.Model):
    title = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка (Font Awesome)', max_length=100)
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.title
# Таблица проекты
class Project(models.Model):
    title = models.CharField('Название проекта', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='projects/')
    url = models.URLField('Ссылка на проект', blank=True)
    is_featured = models.BooleanField('Показать на главной', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField('Имя', max_length=100)
    position = models.CharField('Должность', max_length=100)
    bio = models.TextField('Биография')
    photo = models.ImageField('Фото', upload_to='team/')
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Команда'
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.position}"

class ContactRequest(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Контактная заявка'
        verbose_name_plural = 'Контактные заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f"Запрос от {self.name} ({self.created_at.strftime('%d.%m.%Y')})"
