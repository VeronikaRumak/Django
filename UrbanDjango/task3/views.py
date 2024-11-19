from django.shortcuts import render


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):

    context = {
        'product1': {'name': 'Шахматные фигуры', 'button': 'Купить'},
        'product2': {'name': 'Шахматная доска', 'button': 'Купить'},
        'product3': {'name': 'Шахматные часы', 'button': 'Купить'},
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    return render(request, 'third_task/cart.html')
