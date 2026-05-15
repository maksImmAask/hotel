from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Booking, Room, RoomImage
from .models import Hotel

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['check_in', 'check_out']

        widgets = {

            'check_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'check_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = '__all__'

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'capacity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'room_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class RoomImageForm(forms.ModelForm):

    class Meta:
        model = RoomImage
        fields = ['room', 'image']

        widgets = {

            'room': forms.Select(attrs={
                'class': 'form-select'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = '__all__'

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }