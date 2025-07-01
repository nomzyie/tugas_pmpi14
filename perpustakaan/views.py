from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Selamat datang di API Sistem Informasi Perpustakaan",
        "endpoint_anggota": "/api/anggota/",
        "endpoint_buku": "/api/buku/",
        "endpoint_transaksi": "/api/transaksi/",
        "endpoint_pengembalian": "/api/pengembalian/<id>/",
    })
