from django.contrib import admin
from .models import Anggota, Buku, TransaksiPeminjaman

# Daftarkan model ke admin site
admin.site.register(Anggota)
admin.site.register(Buku)
admin.site.register(TransaksiPeminjaman)
