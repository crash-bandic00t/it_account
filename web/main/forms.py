from django import forms
from .models import Equipment

class EquipmentAddForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        desc_widget = {
            'class': 'form-control',
            'rows': 3
        }
        self.fields['equipment_type'].widget.attrs['class'] = 'form-select'
        self.fields['equipment_type'].empty_label = 'Выберите категорию'
        self.fields['rack'].empty_label = 'Выберите категорию'
        self.fields['rack'].widget.attrs['class'] = 'form-control'
        self.fields['place'].widget.attrs['class'] = 'form-control'