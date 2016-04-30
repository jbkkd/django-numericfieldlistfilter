from django.contrib.admin import FieldListFilter


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
        return []
