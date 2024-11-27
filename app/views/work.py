from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from app.forms import WorkForm
from app.models import Work

def works_done(request):
    works = Work.objects.all()
    template_name = "works_done.html"
    return render(request, template_name, {"works": works})

def create_work(request):
    if request.method == "POST":
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list-works")

    else:
        form = WorkForm()
    template_name = "works/create.html"

    return render(request, template_name, {"form": form})

def list_works(request):
    works = Work.objects.all()
    paginator = Paginator(works, 10)

    page_number = request.GET.get("page", 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)

    elided_page_range = paginator.get_elided_page_range(
        number=page_number, on_each_side=1, on_ends=0
    )

    context = {"page_obj": page_obj, "elided_page_range": elided_page_range}

    template_name = "works/list.html"
    return render(request, template_name, context)

def update_work(request, pk):
    instance = get_object_or_404(Work, pk=pk)
    form = WorkForm(request.POST or None, request.FILES, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("list-works")

    context = {
        "object": instance,
        "form": form,
    }

    template_name = "works/update.html"
    return render(request, template_name, context)

def delete_work(request, pk):
    template_name = "works/delete.html"
    instance = get_object_or_404(Work, pk=pk)

    if request.method == "POST":
        instance.delete()
        return redirect("list-works")

    return render(request, template_name, {"object": instance})