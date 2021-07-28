from django.shortcuts import render,redirect,render_to_response
from django.contrib import messages
from .models import Libro,Autor

# Create your views here.
def index(request):
    libros = Libro.objects.all()
    context = {
        "libros" : libros
    }
    return render(request,'index.html',context)

def addBook(request):
    if request.method == 'POST':
        Libro.objects.create(title=request.POST["title"],desc=request.POST["desc"])
        return redirect('/')


def books(request,idbook):
    request.session["idbook"] = idbook
    libro = Libro.objects.get(id=idbook)
    filtered_entry = Autor.objects.all()
    for exclude_entry in libro.autores.all():
        filtered_entry = filtered_entry.exclude(id=exclude_entry.id)
    context = {
        "libro" : libro,
        "addAutors" : filtered_entry
    }
    return render(request,'books.html',context)

def addAuthor(request):
    if request.method == 'GET':
        idbook = request.session["idbook"]
        if request.GET["author"] != "0":
            idbook = request.session["idbook"]
            Autor.objects.get(id=request.GET["author"]).libros.add(Libro.objects.get(id=idbook))
        else:
            messages.info(request,"No se ha seleccionado ningun Autor")
        return redirect(f'books/{idbook}')



def authorIndex(request):
    author = Autor.objects.all()
    context = {
        "authors" : author
    }
    return render(request,'authors.html',context)

def addNewAuthor(request):
    if request.method == 'POST':
        Autor.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],notas=request.POST["notes"])
        return redirect('/author')


def authors(request,idauthor):
    request.session["idauthor"] = idauthor
    autor = Autor.objects.get(id=idauthor)
    filtered_entry = Libro.objects.all()
    for exclude_entry in autor.libros.all():
        filtered_entry = filtered_entry.exclude(id=exclude_entry.id)
    context = {
        "autores" : autor,
        "books" : filtered_entry
    }
    return render(request,'author.html',context)

def addNewBook(request):
    if request.method == 'GET':
        idauthor = request.session["idauthor"]
        if request.GET["book"] != "0":
            idauthor = request.session["idauthor"]
            Libro.objects.get(id=request.GET["book"]).autores.add(Autor.objects.get(id=idauthor))
            return redirect(f'author/{idauthor}')
        else:
            messages.info(request,"No se ha seleccionado ningun libro")
    return redirect(f'author/{idauthor}')
        