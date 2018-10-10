from django.shortcuts import render, redirect
from django.http import Http404
from main.models import Author
from main.forms import AuthorForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def author_list(request):
    # if request.user.is_authenticated:
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/list.html', context)
    # return redirect('login')


@login_required
def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("Author not found")
    context = {
        'author': author,
        'books': author.books.all()
    }
    return render(request, 'author/detail.html', context)


@login_required
def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'author/new.html', context)


@login_required
def book_list(request):
    return render(request, 'book/list.html')


def show_color(request):
    if 'color' in request.COOKIES:
        return HttpResponse('Your color: {}'.format(request.COOKIES['color']))
    return HttpResponse("Your color empty")


def set_color(request):
    if 'color' in request.GET:
        response = HttpResponse('Your color is now {}'.format(request.GET['color']))
        response.set_cookie('color', request.GET['color'])
        return response
    else:
        return HttpResponse("You didn't give a color.")


