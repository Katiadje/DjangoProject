from django.db import models

# Country model
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['country']

    def __str__(self):
        return self.country

# Film model (correctement en dehors de Country)
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film'
        ordering = ['title']

    def __str__(self):
        return self.title

# User model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'

# City model
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    capital = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='city_pictures/', blank=True, null=True)  # <-- ici
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'city'
        ordering = ['city']

    def __str__(self):
        return self.city