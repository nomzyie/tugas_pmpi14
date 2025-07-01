from django.urls import path
from .views import (
    AnggotaListCreateAPIView, AnggotaDetailAPIView,
    BukuListCreateAPIView, BukuDetailAPIView,
    TransaksiListCreateAPIView, TransaksiDetailAPIView,
    PengembalianAPIView
)

urlpatterns = [
    # Anggota
    path('anggota/', AnggotaListCreateAPIView.as_view(), name='anggota-list'),
    path('anggota/<int:pk>/', AnggotaDetailAPIView.as_view(), name='anggota-detail'),

    # Buku
    path('buku/', BukuListCreateAPIView.as_view(), name='buku-list'),
    path('buku/<int:pk>/', BukuDetailAPIView.as_view(), name='buku-detail'),

    # Transaksi
    path('transaksi/', TransaksiListCreateAPIView.as_view(), name='transaksi-list'),
    path('transaksi/<int:pk>/', TransaksiDetailAPIView.as_view(), name='transaksi-detail'),

    # Pengembalian
    path('pengembalian/<int:pk>/', PengembalianAPIView.as_view(), name='pengembalian'),
]