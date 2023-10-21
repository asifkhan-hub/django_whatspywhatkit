from django.db import models

class WhatsAppMessage(models.Model):
    phone_number = models.CharField(max_length=20, default='')  # Provide a default value here
    message = models.TextField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.phone_number
