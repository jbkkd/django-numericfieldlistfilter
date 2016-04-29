from django import forms
from django.contrib.admin import ModelAdmin
from django.contrib.admin.templatetags.admin_static import static


class NumericModelAdmin(ModelAdmin):
    @property
    def media(self):
        media = super(NumericModelAdmin, self).media
        js = media._js
        js.append(static('admin/js/admin/NumericFieldListFilter.js'))
        return forms.Media(js=js)
