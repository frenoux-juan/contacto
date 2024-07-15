from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
    
    # Validación del campo 'name'
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Este campo es requerido.")
        return name

    # Validación del campo 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Este campo es requerido.")
        if "@" not in email or "." not in email:
            raise forms.ValidationError("Ingrese una dirección de correo válida.")
        return email

    # Validación del campo 'phone_number'
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Este campo es requerido.")
        if not phone_number.isdigit():
            raise forms.ValidationError("El número de teléfono solo debe contener dígitos.")
        if len(phone_number) != 10:  # Suponiendo que el número de teléfono debe tener 10 dígitos
            raise forms.ValidationError("El número de teléfono debe tener 10 dígitos.")
        return phone_number

    # Validación del campo 'message'
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Este campo es requerido.")
        if len(message) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return message

    def clean(self):
        cleaned_data = super().clean()
        # Puedes agregar validaciones adicionales a nivel de formulario aquí si es necesario
        return cleaned_data


