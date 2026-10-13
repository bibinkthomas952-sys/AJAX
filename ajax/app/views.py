from django.shortcuts import render
from .models import Student
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age= request.POST.get('age')
        email= request.POST.get('email') 
        item = Student(name=name, age=age,email=email)
        item.save()
        return JsonResponse({'success': True})

def get_items(request):
    items = Student.objects.all()
    data = [{'id':i.id,'name': i.name, 'age': i.age,'email':i.email} for i in items]
    return JsonResponse(data, safe=False)    


def edit_item(request):
    item_id = request.GET.get('id')
    item = Student.objects.get(id=item_id)
    data = {
        'id':item.id,
        'name': item.name,
        'age': item.age,
        'email': item.email,
    }
    return JsonResponse(data)

def update_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        item = Student.objects.get(id=item_id)
        item.name = name
        item.age = age 
        item.email=email
        item.save()
        return JsonResponse({'success': True})

def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')

        try:
            item = Student.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'success': True})

        except Student.DoesNotExist:
            return JsonResponse(
                {'success': False, 'error': 'Item not found'},
                status=404
            )

    return JsonResponse(
        {'success': False, 'error': 'Invalid request'},
        status=405
    )