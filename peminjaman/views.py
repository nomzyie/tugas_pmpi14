from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from datetime import date

from .models import Anggota, Buku, TransaksiPeminjaman
from .serializers import AnggotaSerializer, BukuSerializer, TransaksiSerializer

# Endpoint Root
@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Selamat datang di API Sistem Informasi Perpustakaan",
        "endpoint_anggota": "/api/anggota/",
        "endpoint_buku": "/api/buku/",
        "endpoint_transaksi": "/api/transaksi/",
        "endpoint_pengembalian": "/api/pengembalian/<id>/"
    })

# Anggota
class AnggotaListCreateAPIView(APIView):
    def get(self, request):
        anggota = Anggota.objects.all()
        serializer = AnggotaSerializer(anggota, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnggotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnggotaDetailAPIView(APIView):
    def get(self, request, pk):
        anggota = get_object_or_404(Anggota, pk=pk)
        serializer = AnggotaSerializer(anggota)
        return Response(serializer.data)

    def put(self, request, pk):
        anggota = get_object_or_404(Anggota, pk=pk)
        serializer = AnggotaSerializer(anggota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        anggota = get_object_or_404(Anggota, pk=pk)
        serializer = AnggotaSerializer(anggota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anggota = get_object_or_404(Anggota, pk=pk)
        anggota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Buku
class BukuListCreateAPIView(APIView):
    def get(self, request):
        buku = Buku.objects.all()
        serializer = BukuSerializer(buku, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BukuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BukuDetailAPIView(APIView):
    def get(self, request, pk):
        buku = get_object_or_404(Buku, pk=pk)
        serializer = BukuSerializer(buku)
        return Response(serializer.data)

    def put(self, request, pk):
        buku = get_object_or_404(Buku, pk=pk)
        serializer = BukuSerializer(buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        buku = get_object_or_404(Buku, pk=pk)
        serializer = BukuSerializer(buku, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        buku = get_object_or_404(Buku, pk=pk)
        buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Transaksi Peminjaman
class TransaksiListCreateAPIView(APIView):
    def get(self, request):
        transaksi = TransaksiPeminjaman.objects.all()
        serializer = TransaksiSerializer(transaksi, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransaksiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransaksiDetailAPIView(APIView):
    def get(self, request, pk):
        transaksi = get_object_or_404(TransaksiPeminjaman, pk=pk)
        serializer = TransaksiSerializer(transaksi)
        return Response(serializer.data)

    def put(self, request, pk):
        transaksi = get_object_or_404(TransaksiPeminjaman, pk=pk)
        serializer = TransaksiSerializer(transaksi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        transaksi = get_object_or_404(TransaksiPeminjaman, pk=pk)
        serializer = TransaksiSerializer(transaksi, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaksi = get_object_or_404(TransaksiPeminjaman, pk=pk)
        transaksi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pengembalian Buku
class PengembalianAPIView(APIView):
    def post(self, request, pk):
        transaksi = get_object_or_404(TransaksiPeminjaman, pk=pk)

        if transaksi.dikembalikan:
            return Response({"detail": "Buku sudah dikembalikan."}, status=status.HTTP_400_BAD_REQUEST)

        transaksi.tanggal_kembali = date.today()
        transaksi.dikembalikan = True
        transaksi.save()

        serializer = TransaksiSerializer(transaksi)
        return Response(serializer.data, status=status.HTTP_200_OK)