"""
Django fields forms
"""

import os

from django import forms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, HTML, Div
from crispy_forms.bootstrap import FormActions, PrependedText, InlineCheckboxes, InlineRadios

MY_COLOR = (
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('Y', 'Yellow'),
)


class TextInputFieldsForm(forms.Form):
    """
    These fields Django renders as: input type='text'.
    """
    your_name = forms.CharField(label='CharField', required=False)
    ip = forms.GenericIPAddressField(label='GenericIPAddressField', required=False)
    my_regex = forms.RegexField(label='RegexField', regex='foo', required=False)
    my_slug = forms.SlugField(label='SlugField', required=False)
    my_uuid = forms.UUIDField(label='UUIDField', required=False)
    
    def __init__(self, *args, **kwargs):
        super(TextInputFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:django_forms', args=('text-input',))
        
        self.helper.layout = Layout(
            HTML(_("<h4><em>TextInput based fields.</em></h4><p>These Django fields use <strong>TextInput</strong> as a default widget, so only <em>required</em>, <em>max_length</em> and <em>min_length</em> properties are validated by browsers. Try to input the wrong value and submit the form - browser validation will not warn you  about an error and you will get a Django validation error.</p><div class='panel panel-info'><div class='panel-body'>All <a href='{% url 'portfolio:django_forms' 'date-time-fields' %}'>time and date</a> Django fields use text inputs.</div></div>")),
            PrependedText('your_name', 'CharField', placeholder=_("any char or sign")),
            PrependedText('my_slug', 'SlugField', placeholder=_("only letters, numbers, underscores, and hyphens")),
            PrependedText('ip', 'GenericIPAddressField', placeholder="127.0.0.1"),
            PrependedText('my_regex', 'RegexField', placeholder=_("string with \"foo\" substring")),
            PrependedText('my_uuid', 'UUIDField', placeholder="64e5e068-eaf7-4009-84f5-72bd21963032"),

            FormActions(
                Submit('submit', _('Submit'), css_class='button white'),
                Reset('reset', _('Reset'))
            )
        )


class TextBasedInputFieldsForm(forms.Form):
    """
    These fields Django renders using url, email and number HTML5 input types.
    """
    my_url = forms.URLField(min_length=3, required=False)
    my_email = forms.EmailField(label='EmailField', min_length=6, required=False)
    integer = forms.IntegerField(label='IntegerField', localize=False, max_value=100, min_value=10, required=True)
    my_float = forms.FloatField(label='FloatField', localize=False, min_value=1.44, max_value=3.14, required=False)
    my_decimal = forms.DecimalField(label='DecimalField', max_digits=6, decimal_places=2, localize=False, required=False)
    
    def __init__(self, *args, **kwargs):
        super(TextBasedInputFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:django_forms', args=('html5-input-types',))
        self.helper.form_show_labels = False
        
        self.helper.layout = Layout(
            HTML(_("<h4><em>HTML5 input types.</em></h4><p>&quot;If your form includes an URLField, an EmailField or any integer field type, Django will use the url, email and number HTML5 input types. By default, browsers may apply their own validation on these fields, which may be stricter than Django’s validation. If you would like to disable this behavior, set the <strong>novalidate</strong> attribute on the form tag, or specify a different widget on the field, like TextInput&quot; (<a href='https://docs.djangoproject.com/en/1.10/topics/forms/#working-with-forms' target='_blank'>Django Documentation <span class='glyphicon glyphicon-new-window' aria-hidden='true'></span></a>)</p><p>Browsers apply their own validation on these fields. For any integer field <strong>Field.localize</strong> must be <strong>False</strong>. Try to input the wrong value and submit the form - browser validation will warn you about an error in the first wrong field.</p>")),
            PrependedText('my_url', 'URLField', placeholder=_("valid URL")),
            PrependedText('my_email', 'EmailField', placeholder=_("valid Email")),
            PrependedText('integer', 'IntegerField', placeholder=_("integer between 10 and 100 - required")),
            PrependedText('my_float', 'FloatField', placeholder=_("float between 1.44 and 3.14")),
            PrependedText('my_decimal', 'DecimalField', placeholder=_("digits: 6, decimal places: 2 == 1234.56")),
            FormActions(
                Submit('submit', _('Submit'), css_class='button white'),
                Reset('reset', _('Reset'))
            )
        )


class ChoiceDjangoFieldsForm(forms.Form):
    happiness = forms.BooleanField(label='BooleanField', required=False)
    color = forms.ChoiceField(label='ChoiceField', choices=MY_COLOR, required=False)
    color_radio = forms.ChoiceField(label='ChoiceField as radio buttons', choices=MY_COLOR, required=False)
    colors = forms.MultipleChoiceField(label='MultipleChoiceField', help_text="hold \"CTL\" button to choose more than 1 item", choices=MY_COLOR, required=False)
    colors_checks = forms.MultipleChoiceField(label='MultipleChoiceField as check boxes', choices=MY_COLOR, required=False)
    null_boolean = forms.NullBooleanField(label='NullBooleanField', required=False)
    my_file = forms.FileField(label='FileField', required=False)
    my_image = forms.ImageField(label='ImageField', required=False)
    choose_file = forms.FilePathField(label='FilePathField', path=os.path.join(settings.STATIC_ROOT, 'file_choice'), required=False)

    def __init__(self, *args, **kwargs):
        super(ChoiceDjangoFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:django_forms', args=('choice-fields',))
        self.helper.form_show_labels = True
        
        self.helper.layout = Layout(
            HTML(_("<h4><em>Boolean and Choice fields.</em></h4><p>These Django fields let you make a choice. If you want to include a boolean in your form that can be either <strong>True</strong> or <strong>False</strong> (e.g. a checked or unchecked checkbox), you must remember to pass in <strong>required=False</strong> when creating the <strong>BooleanField</strong>.</p>")),
            'happiness',
            HTML("<hr />"),
            'color',
            HTML("<hr />"),
            InlineRadios('color_radio'),
            HTML("<hr />"),
            'colors',
            HTML("<hr />"),
            InlineCheckboxes('colors_checks'),
            HTML("<hr />"),
            'my_file',
            HTML("<hr />"),
            'my_image',
            HTML("<hr />"),
            'choose_file',
            HTML("<hr />"),
            FormActions(
                Submit('submit', _('Submit'), css_class='button white'),
                Reset('reset', _('Reset'))
            )
        )


class DateTimeDjangoFieldsForm(forms.Form):
    my_date = forms.DateField(label='DateField', required=False)
    my_datetime = forms.DateTimeField(label='DateTimeField', required=False)
    my_time = forms.TimeField(label='TimeField', required=False)
    my_duration = forms.DurationField(label='DurationField', help_text=_('a string which can be converted into a timedelta: DD HH:MM:SS'), required=False)

    def __init__(self, *args, **kwargs):
        super(DateTimeDjangoFieldsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:django_forms', args=('date-time-fields',))
        self.helper.form_show_labels = False
        
        self.helper.layout = Layout(
            HTML(_("<h4><em>Time and Date Django fields.</em></h4><p>Django uses <strong>TextInput</strong> as a default widget for date and time fields, so only <em>required</em>, <em>max_length</em> and <em>min_length</em> properties are validated by browsers. Try to input the wrong value and submit the form&nbsp;-&nbsp;browser validation will not warn you  about an error and you will get a Django validation error.</p><p>Each field accepts <strong>format</strong> optional argument. If no format argument is provided the first format found in DATE(TIME)_INPUT_FORMATS settings will be used.</p>")),
            PrependedText('my_time', 'TimeField', placeholder=_("14:30:59 or 14:30")),
            PrependedText('my_datetime', 'DateTimeField', placeholder=_("2006-10-25 14:30:59 (YYYY-MM-DD HH:MM:SS)")),
            PrependedText('my_date', 'DateField', placeholder=_("2017-03-19 (YYYY-MM-DD)")),
            PrependedText('my_duration', 'DurationField', placeholder="1 12:32:44"),
            FormActions(
                Submit('submit', _('Submit'), css_class='button white'),
                Reset('reset', _('Reset'))
            )
        )

#    my_coerce = models.TypedChoiceField(label='TypedChoiceField', coerce= , empty_value=)
#    multi_coerce = models.TypedMultipleChoiceField(label='TypedMultipleChoiceField', coerce= , empty_value=)
