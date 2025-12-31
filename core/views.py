from django.shortcuts import render
from .models import HubContent # This must match the class name above

def home_view(request):
    # Task 5: HubDB Filtering logic
    category_query = request.GET.get('category')
    if category_query:
        items = HubContent.objects.filter(category=category_query)
    else:
        items = HubContent.objects.all()
        
    return render(request, 'index.html', {'items': items})