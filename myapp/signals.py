# myapp/signals.py
from django.dispatch import receiver, Signal
import threading

# Define a custom signal
my_signal = Signal()

# Create a receiver function that will handle the signal
@receiver(my_signal)
def my_signal_handler(*args, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Function to emit the signal
def emit_signal():
    print(f"Emitting signal from thread: {threading.current_thread().name}")
    my_signal.send(sender=None)
