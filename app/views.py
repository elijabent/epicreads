from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index_request(request):
    return render(request, 'app/index.html', {
        'request': request
    })

def catalog_request(request):
    return render(request, 'app/catalog.html')

def admin_dashboard(request):
    if request.user.is_staff:
        return render(request, 'app/admin/dashboard.html', {'books': Book.objects.all().order_by('views').values()})
    else:
        return redirect('/')
    
def admin_dashboard_new_book(request):
    if request.method == 'GET':
        if request.user.is_staff:
            return render(request, 'app/admin/new_book.html')
        else:
            return redirect('/')
    elif request.method == 'POST':
        if request.user.is_staff:
            form_data = request.POST
            image_data = request.FILES
            title = form_data.get('title')
            author_first = form_data.get('author-first')
            author_last = form_data.get('author-last')
            cover_front = image_data.get('front-cover')
            cover_back = image_data.get('back-cover')
            summary = form_data.get('summary')
            price = form_data.get('price')
            published = form_data.get('published')

            print(cover_front)
            print(cover_back)

            print(request.FILES)
        
            new_book = Book.objects.create(title=title, author_first=author_first, author_last=author_last, cover_front=cover_front, cover_back=cover_back, summary=summary, price=price, published=published, stars=5)
            new_book.save()
            return redirect('/admin_dashboard')

def admin_dashboard_edit_book(request, id):
    if request.method == 'GET':
        if request.user.is_staff:
            book = Book.objects.get(id=id)
            return render(request, 'app/admin/editbook.html', {
                'book': book,
                'book_front_cover_img_name': book.cover_front.path.rsplit('\\', 1)[-1],
                'book_back_cover_img_name': book.cover_back.path.rsplit('\\', 1)[-1]
            })
        else:
            return redirect('/')
    elif request.method == 'POST':
        if request.user.is_staff:
            form_data = request.POST
            image_data = request.FILES
            book = Book.objects.get(id=id)
            book.title = form_data.get('title')
            book.author_first = form_data.get('author-first')
            book.author_last = form_data.get('author-last')
            if 'front-cover' in image_data:
                book.cover_front = image_data.get('front-cover')
            if 'back-cover' in image_data:
                book.cover_back = image_data.get('back-cover')
            book.summary = form_data.get('summary')
            book.price = form_data.get('price')
            book.published = form_data.get('published')
            try:
                book.save()
                messages.success(request, 'Book changes saved successfully')
                return redirect('app:admin_dashboard_edit_book')
                print(messages)
            except:
                messages.error(request, "An error occurred trying to save changes made to book")
                for message in get_messages(request):
                    print(message)
            return redirect('/admin_dashboard')
        else:
            return redirect('/')