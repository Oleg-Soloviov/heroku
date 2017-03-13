from django import forms
import os
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, HTML
from crispy_forms.bootstrap import FormActions

MY_COLOR = (
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('Y', 'Yellow'),
)

# method="POST"
# enctype="multipart/form-data"

class TextInputFieldsForm(forms.Form):
    your_name = forms.CharField(label='CharField', max_length=100, required=False)
    my_duration = forms.DurationField(label='DurationField', help_text='DD HH:MM:SS.uuuuuu', required=False)
    ip = forms.GenericIPAddressField(label='GenericIPAddressField', required=False)
    my_regex = forms.RegexField(label='RegexField', regex='foo', help_text='with "foo" inside', required=False)
    my_slug = forms.SlugField(label='SlugField', help_text='only letters, numbers, underscores, and hyphens', required=False)
    my_time = forms.TimeField(label='TimeField', help_text='14:30:59 or 14:30', required=False)
    my_uuid = forms.UUIDField(label='UUIDField', help_text='A UUID object: 64e5e068-eaf7-4009-84f5-72bd21963032', required=False)
    def __init__(self, *args, **kwargs):
        super(TextInputFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-allgjangofields'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'textinput_form'
        
        self.helper.layout = Layout(
            HTML("<p>These Django fields use <strong>TextInput</strong> as a default widget, so browsers will not apply their own validation on these fields. Try to input the wrong value and focus another field - browser validation will not warn you  about an error. Then try to submit the form and you get a Django validation error.</p>"),
            'your_name',
            'my_slug',
            'my_time',
            'my_uuid',
            'ip',
            'my_duration',
            FormActions(
                Submit('submit', 'Submit', css_class='button white'),
                Reset('reset', 'Reset')
            )
        )


class AllDjangoFieldsForm(forms.Form):
    my_url = forms.URLField(label='URLField', min_length=3, help_text='Validates that the given value is a valid URL', required=False)
    my_email = forms.EmailField(label='EmailField', min_length=6, required=False)
    integer = forms.IntegerField(label='IntegerField', localize=False, max_value=100, min_value=10, required=False)
    my_float = forms.FloatField(label='FloatField', localize=False, required=False)
    
    happiness = forms.BooleanField(label='BooleanField', required=False)
    color = forms.ChoiceField(label='ChoiceField', choices=MY_COLOR, required=False)
    colors = forms.MultipleChoiceField(label='MultipleChoiceField', choices=MY_COLOR, required=False)
    my_date = forms.DateField(label='DateField', help_text='YYYY-MM-DD', required=False)
    my_datetime = forms.DateTimeField(label='DateTimeField', help_text='2006-10-25 14:30:59', required=False)
    my_decimal = forms.DecimalField(label='DecimalField', max_digits=6, decimal_places=2, help_text='xxxx.xx', localize=False, required=False)
    
    my_file = forms.FileField(label='FileField', required=False)
    choose_file = forms.FilePathField(label='FilePathField', path=os.path.abspath('static/file_choice/'), required=False)
    my_image = forms.ImageField(label='ImageField', required=False)
    null_boolean = forms.NullBooleanField(label='NullBooleanField', required=False)
    
    
    def __init__(self, *args, **kwargs):
        super(AllDjangoFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-allgjangofields'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'django_forms'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Reset('reset', 'Reset'))
    
#    my_coerce = models.TypedChoiceField(label='TypedChoiceField', coerce= , empty_value=)
#    multi_coerce = models.TypedMultipleChoiceField(label='TypedMultipleChoiceField', coerce= , empty_value=)
