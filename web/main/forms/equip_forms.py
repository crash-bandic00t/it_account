from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from ..models import Equipment, Port, Rack

# форма добавления редактирования оборудования
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['complex', 'rack', 'place', 'type', 'name', 'owner', 'desc', 'port_cnt']
        # замена стандартного сообщения об ошибке unique_together
        error_messages = {
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

    # проверка места оборудования, чтобы 1 буква была из списка
    def clean_place(self):
        place = self.cleaned_data['place'].upper()
        if place[0] not in ['A', 'S', 'M', 'F']:
            raise ValidationError('Укажите корректное место!')
        return place


# наследуемся от предыдущего класса чтобы не переписывать проверки и инит
# отдельная форма для того, чтобы нельзя было поменять port_cnt
class EquipmentUpdateForm(EquipmentForm):
    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'type', 'name', 'owner', 'desc']
        error_messages = {
            'place': {
                'unique': 'На этом месте уже есть оборудование!',
            },
            NON_FIELD_ERRORS: {
                'unique_together': "Оборудование на таком месте уже существует!",
            }
        }
