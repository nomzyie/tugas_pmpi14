from django.shortcuts import render

from rest_framework import viewsets
from .models import Anggota, Buku, TransaksiPeminjaman
from .serializers import AnggotaSerializer, BukuSerializer, TransaksiSerializer

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = TransaksiPeminjaman.objects.all()
    serializer_class = TransaksiSerializer
