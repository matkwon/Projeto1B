from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        if len(Tag.objects.filter(nome=request.POST.get('tag'))) == 0:
            tag = Tag(nome=request.POST.get('tag'))
            tag.save()
        else:
            tag = Tag.objects.filter(nome=request.POST.get('tag'))[0]
        Note(title=title, content=content, tag=tag).save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        Note.objects.filter(id=request.POST.get('id')).delete()
        if request.POST.get('tag') != None and len(Note.objects.filter(tag=Tag.objects.filter(nome=request.POST.get('tag'))[0])) == 0:
            Tag.objects.filter(nome=request.POST.get('tag')).delete()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        note = Note.objects.get(id=request.POST.get('id'))
        note.title = request.POST.get('new-title')
        note.content = request.POST.get('new-content')
        if request.POST.get('new-tag') != note.tag.nome:
            if len(Tag.objects.filter(nome=request.POST.get('new-tag'))) == 0:
                Tag(nome=request.POST.get('new-tag')).save()
            note.tag = Tag.objects.filter(nome=request.POST.get('new-tag'))[0]
        note.save()
        for i in Tag.objects.all():
            if len(Note.objects.filter(tag=i)) == 0:
                i.delete()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def tags(request):
    if request.method == 'POST':
        all_tags = Tag.objects.filter(id=request.POST.get('id'))
        notes = Note.objects.filter(tag=all_tags[0])
        return render(request, 'notes/filter.html', {'notes': notes, 'tags': all_tags})
    else:
        all_tags = Tag.objects.all()
        return render(request, 'notes/tags.html', {'tags': all_tags})

def filter_post(request):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    all_tags = Tag.objects.filter(id=request.POST.get('tag-id'))
    tag = all_tags[0]
    Note(title=title, content=content, tag=tag).save()
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/filter.html', {'notes': notes, 'tags': all_tags})

def filter_delete(request):
    Note.objects.filter(id=request.POST.get('id')).delete()
    all_tags = Tag.objects.filter(id=request.POST.get('tag-id'))
    tag = all_tags[0]
    if tag.nome != None and len(Note.objects.filter(tag=tag)) == 0:
        tag.delete()
        return redirect('index')
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/filter.html', {'notes': notes, 'tags': all_tags})

def filter_update(request):
    note = Note.objects.get(id=request.POST.get('id'))
    note.title = request.POST.get('new-title')
    note.content = request.POST.get('new-content')
    if request.POST.get('new-tag') != note.tag.nome:
        if len(Tag.objects.filter(nome=request.POST.get('new-tag'))) == 0:
            Tag(nome=request.POST.get('new-tag')).save()
        note.tag = Tag.objects.filter(nome=request.POST.get('new-tag'))[0]
    note.save()
    all_tags = Tag.objects.filter(id=request.POST.get('tag-id'))
    tag = all_tags[0]
    if tag.nome != None and len(Note.objects.filter(tag=tag)) == 0:
        tag.delete()
        return redirect('index')
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/filter.html', {'notes': notes, 'tags': all_tags})