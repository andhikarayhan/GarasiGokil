from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from appmain.forms import ItemForm
from appmain.models import Item


def show_main(request):
    items = Item.objects.all()
    items_count = Item.objects.count() + 3
    context = {
        'app': 'FasTrack',
        'name': 'Andhika Finnanda Rayhan',
        'class': 'PBP E',
        'cars': [
            {
                'brand': 'BMW',
                'model': 'M3',
                'amount': 1,
                'engine_spec': '3.0L Twin-turbocharged I6, 473 hp'
            },
            {
                'brand': 'BMW',
                'model': 'X5',
                'amount': 2,
                'engine_spec': '3.0L Twin-turbocharged I6, 335 hp'
            },
            {
                'brand': 'Mercedes-Benz',
                'model': 'E-Class',
                'amount': 1,
                'engine_spec': '3.0L Twin-turbocharged V6, 362 hp'
            }
        ],
        'items': items,
        'items_count': items_count,
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('appmain:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")