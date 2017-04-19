"""
Django rich editors forms
"""
from django import forms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Reset, HTML, Div


class TinyMCEForm(forms.Form):
    content = forms.CharField(widget=TinyMCE())
    
    def __init__(self, *args, **kwargs):
        super(TinyMCEForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:tinymce', args=('django-tinymce',))
        
        self.helper.layout = Layout(
            HTML(_("<h4>Django-tinymce.</h4><p>&quot;Django-tinymce&quot; is a Django application that contains a widget to render a form field as a TinyMCE editor. It uses TinyMCE editor 3.5.11. Current version of TinyMCE editor is TinyMCE&nbsp;4.5.x. and you need only two scripts in HEAD section of HTML document <a href=\"{% url 'portfolio:tinymce' 'tinymce4' %}\">to convert</a> any your field in rich text editor.</p>")),
            'content',
            )

class TinyMCE4Form(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))

    def __init__(self, *args, **kwargs):
        super(TinyMCE4Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:tinymce', args=('tinymce4',))
        
        self.helper.layout = Layout(
            HTML(_("<h4>TinyMCE 4.</h4><p>Tiny MCE 4 is a platform independent web-based JavaScript HTML WYSIWYG editor. TinyMCE enables you to convert HTML textarea fields or other HTML elements to editor instances. Current version of TinyMCE editor is TinyMCE&nbsp;4.5.x. and you need only two scripts in HEAD section of HTML document to enable it.</p>")),
            'content',
            )


class DjWysiwygForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))

    def __init__(self, *args, **kwargs):
        super(DjWysiwygForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:tinymce', args=('wysiwig',))
        
        self.helper.layout = Layout(
            HTML(_("<h4>NicEdit.</h4><p>NicEdit is a Lightweight, Cross Platform, Inline Content Editor to allow easy editing of web site content on the fly in the browser.</p>")),
            'content',
            )

class CKEditorForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))

    def __init__(self, *args, **kwargs):
        super(CKEditorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('portfolio:tinymce', args=('ckeditor',))
        
        self.helper.layout = Layout(
            HTML(_("<h4>CKEditor.</h4><p>CKEditor is a browser-based WYSIWYG content editor. It brings to the web common word processor features found in desktop editing applications like Microsoft Word and OpenOffice. </p>")),
            'content',
            )
