from django.shortcuts import render


def index_page(request):
    context = {"page_name": "Телефонная книга"}

    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass

    return render(request, "phone_book/index_page.html", context)
