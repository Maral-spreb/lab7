from django.shortcuts import render, get_object_or_404
from orm_app.models import Item 



# 1. All() - бүх мэдээллийг авах
def index(request):
    items = Item.objects.all()  # бүх item-г авах
    return render(request, 'index.html', {'items': items})

# 2. Get() - нэг мөр бичлэг авах (дэлгэрэнгүй page)
def item_detail(request, item_id):
    # item_id-тай item-г авах, байхгүй бол 404
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'detail.html', {'item': item})

# 3. Filter() - нөхцөл тохирсон бичлэгүүд
from django.shortcuts import render
from orm_app.models import Item

def item_filter(request):
    query = request.GET.get('q')  # input-с утга авах
        
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()

    return render(request, 'filter.html', {'items': items, 'query': query})