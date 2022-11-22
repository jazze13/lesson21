from django.shortcuts import render


def index(request, fio, age, interests):
    context = {
        'fio':fio,
        'age':age,
        'interests':interests,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')