from django.db import models
from apps.users.models import CustomUser


class TransportType(models.Model):
    name = models.CharField(max_length=255,)

    class Meta:
        verbose_name= 'Вид Транспорта'
        verbose_name_plural= 'Виды транспорта'

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=255,)

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural= 'Категории'

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    Country models
    """
    name = models.CharField(max_length=100,
                            verbose_name= 'Страна',
                            unique = True,)
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name

class City(models.Model):
    """
    City models
    """
    country = models.ForeignKey(Country, on_delete = models.CASCADE,
                                            verbose_name = 'Страна')
    name = models.CharField(max_length=50,
                            verbose_name= 'Город',
                            unique = True,)
    class Meta:
        verbose_name= 'Название города'
        verbose_name_plural= 'Название городов'

    def __str__(self):
        return self.name


class Trips(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='trip_city_from')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE,related_name='trip_city_to')
    departure_date = models.DateField(auto_now=True)
    arrival_date = models.DateField(auto_now=True)
    weight = models.FloatField()
    categoty= models.ForeignKey(Categories, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=19, decimal_places=2)
    transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE)
    comment= models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Поездка'
        verbose_name_plural= 'Поездки'
    
    


class Packages(models.Model):
    title = models.CharField(max_length=255,)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city_from = models.ForeignKey(City, on_delete=models.CASCADE,related_name='packages_city_from')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE,related_name='packages_city_to')
    date = models.DateField(auto_now=True)
    weight = models.FloatField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=19, decimal_places=10)
    comment= models.TextField()
    recipient_name =models.CharField(max_length=100,)
    recipient_contact = models.CharField(max_length=100,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)
        verbose_name= 'Посылка'
        verbose_name_plural= 'Посылки'

    def __str__(self):
        return self.title


class Pictures(models.Model):
    trip_id = models.ForeignKey(Trips, related_name='trips', on_delete=models.CASCADE, blank=True)
    packages_id = models.ForeignKey(Packages, related_name='packages', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='pictures')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Deals(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='deals_user')
    executor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='deals_executor')
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='deals_package')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return self.package

class Status(models.Model):
    name =models.CharField(max_length=100,)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return self.name


class Logs(models.Model):
    deal_id = models.ForeignKey(Deals,on_delete=models.CASCADE,)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    def __str__(self):
        return self.status


class Faq(models.Model):
    question = models.CharField(max_length=255,blank=True)
    answer = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.question

class SocialMedia(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255,)