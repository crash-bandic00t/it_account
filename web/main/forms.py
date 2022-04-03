from django import forms
from .models import Equipment
from django.core.exceptions import ValidationError

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'equipment_type', 'name', 'owner', 'desc', 'port_cnt']
        error_messages = {
            'place': {
                'unique': 'На этом месте уже есть оборудование!',
            }
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rack'].empty_label = 'Выберите стойку...'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    # def clean_place(self):
    #     place = self.cleaned_data['place']
    #     if place == '1':
    #         raise ValidationError('Ошибка!')
    #     return place


class EquipmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'equipment_type', 'name', 'owner', 'desc']
        error_messages = {
            'place': {
                'unique': 'На этом месте уже есть оборудование!',
            }
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'