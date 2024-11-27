from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from app.forms import LocationForm
from app.models import Location


def create_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list-locations")

    else:
        form = LocationForm()
    template_name = "location/create.html"

    return render(request, template_name, {"form": form})


def list_locations(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, 10)

    page_number = request.GET.get("page", 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)

    elided_page_range = paginator.get_elided_page_range(
        number=page_number, on_each_side=1, on_ends=0
    )

    context = {"page_obj": page_obj, "elided_page_range": elided_page_range}

    template_name = "location/list.html"
    return render(request, template_name, context)


def update_location(request, pk):
    instance = get_object_or_404(Location, pk=pk)
    form = LocationForm(request.POST or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("list-locations")

    context = {
        "object": instance,
        "form": form,
    }

    template_name = "location/update.html"
    return render(request, template_name, context)


def delete_location(request, pk):
    template_name = "location/delete.html"
    instance = get_object_or_404(Location, pk=pk)

    if request.method == "POST":
        instance.delete()
        return redirect("list-locations")

    return render(request, template_name, {"object": instance})
