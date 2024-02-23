from django.shortcuts import render


def index_page(request):
    context = {
        "menu_items": [
            {"link": "/", "text": "Меню"},
            {
                "link": "/calculator_two/",
                "text": "Калькулятор для второго урока на калькулятор",
            },
            {
                "link": "/calculator_three/",
                "text": "Калькулятор для третьего урока на калькулятор",
            },
            {
                "link": "/phone_book/",
                "text": "Проект 'Телефонная книга'",
            },
        ]
    }

    return render(request, "menu/index_page.html", context)
