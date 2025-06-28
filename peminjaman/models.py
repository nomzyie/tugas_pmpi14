from django.db import models

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    stok = models.IntegerField()

class TransaksiPeminjaman(models.Model):
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField(null=True, blank=True)
    dikembalikan = models.BooleanField(default=False)