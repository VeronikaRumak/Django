from django.shortcuts import render


def base(request):
    return render(request, 'fourth_task/menu.html')


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    context = {
        'products': [
            {'name': 'Шахматные фигуры', 'button': 'Купить'},
            {'name': 'Шахматная доска', 'button': 'Купить'},
            {'name': 'Шахматные часы', 'button': 'Купить'},
        ]
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')



