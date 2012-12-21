#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
#
# This module provides template tags for the current template name, the
# corresponding CSS file, and the corresponding JS file.
#
from inspect import stack
from os.path import splitext

from django.template.base import Library


register = Library()


def stack_value(name, default=None):
    """Returns the value of the given name in the call stack."""
    for item in stack():
        frame = item[0]
        if name in frame.f_locals:
            return frame.f_locals[name]
    return default


@register.simple_tag
def template_name(default='index'):
    """Returns the name of the current template."""
    # This is very implementation specific, and might break in the future if the
    # django template parser changes.  But for now, it's quick, clean, and easy.
    return stack_value('template_name', default)


@register.simple_tag
def css_name(default='index'):
    """Returns the name of the CSS asset for the current template."""
    name = splitext(template_name(default))[0]
    return '{}.css'.format(name)


@register.simple_tag
def js_name(default='index'):
    """Returns the name of the JS asset for the current template."""
    name = splitext(template_name(default))[0]
    return '{}.js'.format(name)
