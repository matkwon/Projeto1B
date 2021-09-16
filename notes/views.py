from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'post':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            Note(title=title, content=content).save()
        elif request.POST.get('type') == 'delete':
            Note.objects.filter(id=request.POST.get('id')).delete()
        elif request.POST.get('type') == 'update':
            note = Note.objects.get(id=request.POST.get('id'))
            note.title = request.POST.get('new-title')
            note.content = request.POST.get('new-content')
            note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})