from email.policy import default
from urllib import request
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from django import forms
from .models import Equipment, Port, Rack

# форма добавления редактирования оборудования
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['rack', 'place', 'type', 'name', 'owner', 'desc', 'port_cnt']
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


class PortUpdateForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = ['category', 'type', 'vlan', 'active', 'dest', 'full_path', 'desc']
        widgets = {
            'dest': forms.TextInput(attrs={
                'readonly': '',
                'aria-label': 'destination',
                'aria-describedby': 'change_dest'
                })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию...'
        # каждому полю формы прописываем класс 'form-control'
        for field_name, field in self.fields.items():
            if field_name == 'active':
                pass
            else:
                field.widget.attrs['class'] = 'form-control'
    

    
class DestinationPortUpdateForm(forms.Form):
    rack = forms.ModelChoiceField(queryset=Rack.objects.all(), label='Стойка откуда', initial='R', required=False, empty_label='Выберите стойку...',   widget=forms.Select(attrs={'class':'form-control'}))
    equip = forms.ModelChoiceField(queryset=Equipment.objects.all(), label='Оборудование откуда', required=False, empty_label='Выберите оборудование...', widget=forms.Select(attrs={'class':'form-control'}))
    port = forms.ModelChoiceField(queryset=Port.objects.all(), label='Порт откуда', required=False, empty_label='Выберите порт...', widget=forms.Select(attrs={'class':'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equip'].queryset = Equipment.objects.none()
        self.fields['port'].queryset = Port.objects.none()
        # проверяем что в запросе есть equip, если есть, то выставляем queryset на фильтрованый,
        # чтобы не было ошибки заполнения поля. Так же делаем с port
        if self.data.get('equip'):
            equip_id = int(self.data.get('equip'))
            self.fields['equip'].queryset = Equipment.objects.filter(id=equip_id)
        if self.data.get('port'):
            port_id = int(self.data.get('port'))
            self.fields['port'].queryset = Port.objects.filter(id=port_id)
         

    def clean_port(self):
        port = self.cleaned_data['port']
        if port:
            if port.busy:
                raise ValidationError('Данный порт уже занят!')
        return port
