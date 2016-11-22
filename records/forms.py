# -*- coding: utf-8 -*-

from django import forms
from records.models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        # fields = ('fullname', 'birthdate', 'address', 'phone', 'email', 'comment')
        exclude = ('user',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['birthdate'].widget.attrs['class'] = 'form-control datepicker'
        self.fields['birthdate'].widget.attrs['placeholder'] = u'дд.мм.гггг'

    def save(self, commit=True):
        obj = super(BookForm, self).save(commit=False)
        obj.fullname = self.cleaned_data['fullname']
        obj.birthdate = self.cleaned_data['birthdate']
        obj.address = self.cleaned_data['address']
        obj.phone = self.cleaned_data['phone']
        obj.email = self.cleaned_data['email']
        obj.comment = self.cleaned_data['comment']
        obj.user = self.user

        if commit:
            obj.save()
        return obj
