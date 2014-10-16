from __future__ import absolute_import

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from . import models
import datetime

from django.core.exceptions import ValidationError
from django.utils.timezone import utc


class EstateListForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = models.EstateList

    def __init__(self, *args, **kwargs):
        super(TalkListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            ButtonHolder(
                Submit('create', 'Create', css_class='btn-primary')
            )
        )

'''
class EstateForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'address', 'text', 'contact_info', 'neigh')
        model = models.Estate

    def __init__(self, *args, **kwargs):
        super(TalkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'address',
            'text',
            'contact_info',
            'neigh',
            ButtonHolder(
                Submit('add', 'Add', css_class='btn-primary')
            )
        )
'''
