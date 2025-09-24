from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Merek')
    model = models.CharField(max_length=100, verbose_name='Model')
    year = models.IntegerField(verbose_name='Tahun')
    color = models.CharField(max_length=50, verbose_name='Warna')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Harga')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pemilik')
    
    class Meta:
        verbose_name = 'Mobil'
        verbose_name_plural = 'Mobil'
        ordering = ['-created_at']
        permissions = [
            ('can_view_all_cars', 'Can view all cars'),
            ('can_add_car', 'Can add car'),
            ('can_change_car', 'Can change car'),
            ('can_delete_car', 'Can delete car'),
        ]
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
