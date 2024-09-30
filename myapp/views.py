# myapp/views.py
from django.http import HttpResponse
from .signals import emit_signal

def trigger_signal(request):
    emit_signal()
    return HttpResponse("Signal emitted!")
