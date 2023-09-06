from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Salsabila Aulia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)