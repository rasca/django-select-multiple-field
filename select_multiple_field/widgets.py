# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets
from django.utils.safestring import mark_safe

try:
    from django.forms.utils import flatatt
except ImportError:
    from django.forms.util import flatatt

try:
    from django.utils.html import format_html
except ImportError:
    def format_html(format_string, *args, **kwargs):
        return format_string.format(*args, **kwargs)


HTML_ATTR_CLASS = 'select-multiple-field'


class SelectMultipleField(widgets.SelectMultiple):
    """Multiple select widget ready for jQuery multiselect.js"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = HTML_ATTR_CLASS
