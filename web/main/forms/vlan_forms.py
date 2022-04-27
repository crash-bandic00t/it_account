from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from ..models import Vlan

# форма добавления редактирования оборудования
class VlanForm(forms.ModelForm):
    class Meta:
        model = Vlan
        fields = '__all__'
        # замена стандартного сообщения об ошибке unique_together
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Данный vlan в этом комплексе занят!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # прописываем пустое значение вместо '-------' 
        self.fields['complex'].empty_label = 'Выберите комплекс...'
        # каждому полю формы прописываем класс 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'


class VlanUpdateForm(VlanForm):
    class Meta:
        model = Vlan
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Данный vlan в этом комплексе занят!",
            }
        }
