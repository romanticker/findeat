from django.shortcuts import render


def main(request):
    return render(request, "main.html")
#127.0.0.1

def burger_list(request):
    return render(request, "burger_list.html")
#127.0.0.1/burgurs/

def APImap(request):
    return render(request, "APImap.html")
#127.0.0.1/APImap/