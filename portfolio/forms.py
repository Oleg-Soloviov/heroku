from django import forms
import os
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, HTML
from crispy_forms.bootstrap import FormActions, PrependedText

MY_COLOR = (
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('Y', 'Yellow'),
)

# method="POST"
# enctype="multipart/form-data"

class TextInputFieldsForm(forms.Form):
    """
    These fields Django renders as: input type='text'.
    """
    your_name = forms.CharField(label='CharField', max_length=100, required=False)
    my_duration = forms.DurationField(label='DurationField', help_text=' a string which can be converted into a timedelta: DD HH:MM:SS', required=False)
    ip = forms.GenericIPAddressField(label='GenericIPAddressField', required=False)
    my_regex = forms.RegexField(label='RegexField', regex='foo', required=False)
    my_slug = forms.SlugField(label='SlugField', required=False)
    my_time = forms.TimeField(label='TimeField', required=False)
    my_uuid = forms.UUIDField(label='UUIDField', required=False)
    
    def __init__(self, *args, **kwargs):
        super(TextInputFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = 'textinput_form'
        
        self.helper.layout = Layout(
            PrependedText('your_name', 'CharField'),
            PrependedText('my_slug', 'SlugField', placeholder="only letters, numbers, underscores, and hyphens"),
            PrependedText('my_time', 'TimeField', placeholder="14:30:59 or 14:30"),
            PrependedText('ip', 'GenericIPAddressField', placeholder="127.0.0.1"),
            PrependedText('my_regex', 'RegexField', placeholder="with 'foo' inside"),
            PrependedText('my_uuid', 'UUIDField', placeholder="64e5e068-eaf7-4009-84f5-72bd21963032"),
            PrependedText('my_duration', 'DurationField', placeholder="1 12:32:44"),
            
            FormActions(
                Submit('submit', 'Submit', css_class='button white'),
                Reset('reset', 'Reset')
            )
        )


class TextBasedInputFieldsForm(forms.Form):
    """
    These fields Django renders using url, email and number HTML5 input types.
    """
    my_url = forms.URLField(min_length=3, required=False)
    my_email = forms.EmailField(label='EmailField', min_length=6, required=False)
    integer = forms.IntegerField(label='IntegerField', localize=False, max_value=100, min_value=10, required=False)
    my_float = forms.FloatField(label='FloatField', localize=False, min_value=1.44, max_value=3.14, required=False)
    my_decimal = forms.DecimalField(label='DecimalField', max_digits=6, decimal_places=2, localize=False, required=False)
    
    def __init__(self, *args, **kwargs):
        super(TextBasedInputFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'textinput_form'
        self.helper.form_show_labels = False
        
        self.helper.layout = Layout(
            PrependedText('my_url', 'URLField', placeholder="valid URL"),
            PrependedText('my_email', 'EmailField', placeholder="valid Email"),
            PrependedText('integer', 'IntegerField', placeholder="integer between 10 and 100"),
            PrependedText('my_float', 'FloatField', placeholder="float between 1.44 and 3.14"),
            PrependedText('my_decimal', 'DecimalField', placeholder="digits: 6, decimal places: 2 == 1234.56"),
            FormActions(
                Submit('submit', 'Submit', css_class='button white'),
                Reset('reset', 'Reset')
            )
        )


class AllDjangoFieldsForm(forms.Form):
    happiness = forms.BooleanField(label='BooleanField', required=False)
    color = forms.ChoiceField(label='ChoiceField', choices=MY_COLOR, required=False)
    colors = forms.MultipleChoiceField(label='MultipleChoiceField', choices=MY_COLOR, required=False)
    my_date = forms.DateField(label='DateField', help_text='YYYY-MM-DD', required=False)
    my_datetime = forms.DateTimeField(label='DateTimeField', help_text='2006-10-25 14:30:59', required=False)

    
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
