from django.shortcuts import render

def buku(request):
    
    judul = ["Belajar Python","Belajar Java","Belajar CSS"]
    penulis = "Muhammad Azzam A.F."
    
    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')

