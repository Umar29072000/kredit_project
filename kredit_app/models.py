from django.db import models

class Kredit(models.Model):
    kontrak_no = models.CharField(max_length=20)
    client_name = models.CharField(max_length=100)
    harga_mobil = models.DecimalField(max_digits=10, decimal_places=2)
    dp_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    tenor_tahun = models.IntegerField()
    bunga_tahunan = models.DecimalField(max_digits=5, decimal_places=2)
    tgl_mulai = models.DateField()
