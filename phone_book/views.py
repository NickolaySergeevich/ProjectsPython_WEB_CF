from django.shortcuts import render

from phone_book.models import PhoneBook


def index_page(request):
    context = {"page_name": "Телефонная книга"}

    if request.method == "POST":
        contact_name = request.POST.get("contact_name")
        contact_surname = request.POST.get("contact_surname")
        contact_phone = request.POST.get("contact_phone")
        contact_note = request.POST.get("contact_note")

        PhoneBook(
            contact_name=contact_name,
            contact_surname=contact_surname,
            contact_phone=contact_phone,
            contact_note=contact_note,
        ).save()
    elif request.method == "GET":
        user_choose = request.GET.get("radio_filter")
        if user_choose == "filter_all":
            context["filter_all"] = True
        elif user_choose == "filter_name":
            context["filter_name"] = True
        elif user_choose == "filter_surname":
            context["filter_surname"] = True

    context["data"] = PhoneBook.objects.all()

    return render(request, "phone_book/index_page.html", context)
