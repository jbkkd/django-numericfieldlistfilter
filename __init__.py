from django.contrib.admin import FieldListFilter
from django.db import models

from .filters import NumericFieldListFilter

FieldListFilter.register(lambda f: isinstance(f, (models.IntegerField, models.FloatField, models.DecimalField)),
                         NumericFieldListFilter, True)
