from django import forms
from .models import Equipment

class EquipmentAddForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'equipment_type', 'name', 'owner', 'desc', 'port_cnt']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rack'].empty_label = 'Выберите стойку...'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.error_messages = {
            #     'required': 'required error',
            #     'unique': 'My error',
            # }
        