from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import CustomUserCreationForm
from .forms import NoteCreateForm
from .models import Note

# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required()
def dashboardView(request):
    return render(request,'dashboard.html')

def notes(request):
    notes = Note.objects.all()
    return render(request, 'notes.html',{'notes':notes})

def note_details(request, id):
    note=get_object_or_404(Note, note_id=id)
    return render(request,'note_details.html',{'note':note}) 

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form})


def create_note(request):
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_details', id=note.note_id)
    else:
        form = NoteCreateForm()
    return render(request, 'create_note.html', {'form': form})
