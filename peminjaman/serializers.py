from rest_framework import serializers
from .models import Anggota, Buku, TransaksiPeminjaman

class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaksiPeminjaman
        fields = '__all__'