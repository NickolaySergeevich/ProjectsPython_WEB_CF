from django.shortcuts import render

from notes.models import Notes, NotesSupplements


def index_page(request):
    context = {"page_name": "Notes"}

    if request.method == "POST":
        note_header = request.POST.get("note_header")
        note_description = request.POST.get("note_description")

        note_item = Notes(note_header=note_header, note_description=note_description)
        note_item.save()

        note_supplements = (
            request.POST.get("note_supplement_one", default=None),
            request.POST.get("note_supplement_two", default=None),
            request.POST.get("note_supplement_three", default=None),
            request.POST.get("note_supplement_four", default=None),
            request.POST.get("note_supplement_five", default=None),
        )
        for note_supplement in note_supplements:
            if note_supplement:
                NotesSupplements(
                    note_id=note_item,
                    note_supplement=note_supplement,
                ).save()

    data = Notes.objects.all().values()
    for index in range(len(data)):
        data[index]["note_supplements"] = NotesSupplements.objects.filter(
            note_id=data[index]["id"]
        ).values()

    context["data"] = data

    return render(request, "notes/index_page.html", context)
