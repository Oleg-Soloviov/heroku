from django.shortcuts import render
from .editors_forms import TinyMCEForm, TinyMCE4Form, DjWysiwygForm, CKEditorForm


def tinymceview(request, fields):
    if fields == 'django-tinymce':
        form = TinyMCEForm()
    elif fields == 'tinymce4':
        form = TinyMCE4Form()
    elif fields == 'wysiwyg':
        form = DjWysiwygForm()
    elif fields == 'ckeditor':
        form = CKEditorForm()
    return render(request, 'portfolio/editor_forms.html', {'form': form})
