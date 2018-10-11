from django.db import models
from pytils.translit import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

#Модель Услуги
class Service(models.Model):
    class Meta():
        db_table = 'service'
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title

#Модель О нас
class About_us(models.Model):
    class Meta():
        db_table = 'about_us'
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title

#Модель Контакты
class Contact(models.Model):
    class Meta():
        db_table = 'contacts'
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    phone = models.TextField("Телефон", max_length=150)
    address = models.TextField("Адрес", max_length=150)
    email = models.EmailField(max_length=70)
    skype = models.TextField(max_length=150)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.phone
    
    def __str__(self):
        return self.phone

#Модель обратной связи
class Contact_form(models.Model):
	class Meta():
		db_table = 'contact_forms'
		verbose_name = "Обратная связь"
		verbose_name_plural = "Обратная связь"
	
	name = models.CharField("Имя", max_length=30)
	second_name = models.CharField("Фамилия", max_length=30)
	email = models.EmailField(max_length=70)
	message = models.TextField("Сообщение", max_length=1000)
	data = models.DateTimeField("Дата отправки", default=timezone.now)
	
	def __str__(self):
		return self.name