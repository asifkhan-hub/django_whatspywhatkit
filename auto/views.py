import pywhatkit as kit
from django.shortcuts import render, redirect
from .models import WhatsAppMessage
from .forms import WhatsAppMessageForm
import threading

def send_whatsapp_message(request):
    if request.method == 'POST':
        form = WhatsAppMessageForm(request.POST)
        if form.is_valid():
            whatsapp_message = form.save()
            # Schedule the WhatsApp message
            send_message_thread = threading.Thread(target=send_message, args=(whatsapp_message,))
            send_message_thread.start()
            return redirect('message_sent')
    else:
        form = WhatsAppMessageForm()
    return render(request, 'send_message.html', {'form': form})

def message_sent(request):
    return render(request, 'message_sent.html')

def send_message(whatsapp_message):
    try:
        # Your PyWhatKit code to send WhatsApp messages
        kit.sendwhatmsg(
            whatsapp_message.phone_number,
            whatsapp_message.message,
            whatsapp_message.scheduled_time.hour,
            whatsapp_message.scheduled_time.minute
        )
    except Exception as e:
        # Handle exceptions here, e.g., log the error
        print(f"Error sending WhatsApp message: {str(e)}")
