from urllib import request
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from .models import Equipment

# форма добавления редактирования оборудования
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'equipment_type', 'name', 'owner', 'desc', 'port_cnt']
        error_messages = {
            # 'place': {
            #     'unique': 'На этом месте уже есть оборудование!',
            # },
            NON_FIELD_ERRORS: {
                'unique_together': "В данном шкафу это место занято!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # прописываем пустое значение вместо '-------' 
        self.fields['rack'].empty_label = 'Выберите стойку...'
        # каждому полю формы прописываем класс 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    def clean_place(self):
        place = self.cleaned_data['place'].upper()
        if place[0] not in ['A', 'S', 'M', 'F']:
            raise ValidationError('Укажите корректное место!')
        return place

class EquipmentUpdateForm(EquipmentForm):
    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'equipment_type', 'name', 'owner', 'desc']
        error_messages = {
            'place': {
                'unique': 'На этом месте уже есть оборудование!',
            },
            NON_FIELD_ERRORS: {
                'unique_together': "Оборудование на таком месте уже существует!",
            }
        }