from django.shortcuts import render,redirect
from .models import ReversedText
# Create your views here.
# in text_reverser/views.py


def reverse_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        reversed_text = text[::-1]
        ReversedText.objects.create(original_text=text, reversed_text=reversed_text)
        return redirect('/')
    context = ReversedText.objects.all()
    queryset = {'reverse_text' : context}
    return render(request, 'home.html',queryset)


def delete_text(request,id):
    context=ReversedText.objects.get(id=id)
    context.delete()
    return redirect('/')
# in text_reverser/views.py

