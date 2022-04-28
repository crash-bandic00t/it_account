from django.core.exceptions import ValidationError

from django import forms
from ..models import Equipment, Port, Rack, Vlan


class PortUpdateForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = ['type', 'vlan', 'active', 'dest', 'full_path', 'desc']
        # делаем поле назначения не редактируемым, чтобы пользователь воспользовался
        # зависимыми dropdown для правильного выбора порта назначения
        widgets = {
            'dest': forms.TextInput(attrs={
                'readonly': '',
                'aria-label': 'destination',
                'aria-describedby': 'change_dest'
                })
        }

    def __init__(self, *args, **kwargs):
        # вытаскиваем из квагров id комплекса
        self.complex_id = kwargs.pop('complex_id')
        super().__init__(*args, **kwargs)
        # фильтруем queryset для отображения vlan только комплекса, к которому принадлежит оборудование
        self.fields['vlan'].queryset = Vlan.objects.filter(complex_id=self.complex_id)
        self.fields['vlan'].widget.attrs['style'] = 'display: none;'
        # каждому полю формы прописываем класс 'form-control'
        for field_name, field in self.fields.items():
            if field_name == 'active':
                pass
            else:
                field.widget.attrs['class'] = 'form-control'
    

# форма зависимых полей для выбора нужного порта    
class DestinationPortUpdateForm(forms.Form):
    rack = forms.ModelChoiceField(queryset=Rack.objects.all(), label='Стойка откуда', initial='R', required=False, empty_label='Выберите стойку...',   widget=forms.Select(attrs={'class':'form-control'}))
    equip = forms.ModelChoiceField(queryset=Equipment.objects.all(), label='Оборудование откуда', required=False, empty_label='Выберите оборудование...', widget=forms.Select(attrs={'class':'form-control'}))
    port = forms.ModelChoiceField(queryset=Port.objects.all(), label='Порт откуда', required=False, empty_label='Выберите порт...', widget=forms.Select(attrs={'class':'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equip'].queryset = Equipment.objects.none()
        self.fields['port'].queryset = Port.objects.none()
        # проверяем что в запросе есть equip. если есть, то меняем queryset вместо пустого на фильтрованый,
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
