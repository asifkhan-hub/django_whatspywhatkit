from django import forms
from .models import WhatsAppMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field

class WhatsAppMessageForm(forms.ModelForm):
    class Meta:
        model = WhatsAppMessage
        fields = ['phone_number', 'message', 'scheduled_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Field('phone_number', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('message', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('scheduled_time', css_class='form-control datetimepicker'),
                css_class='form-group'
            ),
            Submit('submit', 'Send', css_class='btn btn-primary')
        )
