from django import forms
import os

MY_COLOR = (
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('Y', 'Yellow'),
)

# method="POST"
# enctype="multipart/form-data"

class BootstrapForm(forms.Form):
    your_name = forms.CharField(label='CharField', max_length=100)
    happiness = forms.BoolleanField(label='BooleanField')
    color = models.ChoiceField(label='ChoiceField', choices=MY_COLOR)
    colors = models.MultipleChoiceField(label='MultipleChoiceField', choices=MY_COLOR)
    my_date = models.DateField(label='DateField', help_text='YYYY-MM-DD')
    my_datetime = models.DateTimeField(label='DateTimeField', help_text='2006-10-25 14:30:59')
    my_decimal = models.DecimalField(label='DecimalField', max_digits=6, decimal_places='2', help_text='xxxx.xx', localize=False)
    my_duration = models.DurationField(label='DurationField', help_text='DD HH:MM:SS.uuuuuu')
    my_email = models.EmailField(label='EmailField', min_length=6)
    my_file = models.FileField(label='FileField')
    choose_file = models.FilePathField(label='FilePathField', path=os.path.abspath('static/file_choice'))
    my_float = models.FloatField(label='FloatField', localize=False)
    my_image = models.ImageField(label='ImageField')
    integer = models.IntegerField(label='IntegerField', localize=False, max_value=100, min_value=10)
    ip = models.GenericIPAddressField(label='GenericIPAddressField')
    null_boolean = models.NullBooleanField(label='NullBooleanField' )
    my_regex = models.RegexField(label='RegexField', help_text='with "foo" inside')
    my_slug = models.SlugField(label='SlugField', help_text='only letters, numbers, underscores, and hyphens')
    my_time = models.TimeField(label='TimeField', help_text='14:30:59 or 14:30')
    my_url = models.URLField(label='URLField', min_length=3, help_text='Validates that the given value is a valid URL')
    
    
#    my_coerce = models.TypedChoiceField(label='TypedChoiceField', coerce= , empty_value=)
#    multi_coerce = models.TypedMultipleChoiceField(label='TypedMultipleChoiceField', coerce= , empty_value=)
