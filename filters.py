from django.contrib.admin import FieldListFilter
from django.db import models
from django.utils.translation import ugettext_lazy as _


class NumericFieldListFilter(FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.template = 'admin/numericfieldlistfilter.html'
        self.lookup_kwarg = '%s__lte' % field_path
        self.lookup_kwarg2 = '%s__gte' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)
        self.lookup_val2 = request.GET.get(self.lookup_kwarg2)
        super(NumericFieldListFilter, self).__init__(field,
            request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg2]

    def choices(self, cl):
        for lookup, title in (
                (None, _('All')),
                ('1', _('OMER')),
                ('0', _('No'))):
            yield {
                'selected': self.lookup_val == lookup and not self.lookup_val2,
                'query_string': cl.get_query_string({
                    self.lookup_kwarg: lookup,
                }, [self.lookup_kwarg2]),
                'display': title,
            }
        if isinstance(self.field, models.NullBooleanField):
            yield {
                'selected': self.lookup_val2 == 'True',
                'query_string': cl.get_query_string({
                    self.lookup_kwarg2: 'True',
                }, [self.lookup_kwarg]),
                'display': _('Unknown'),
            }