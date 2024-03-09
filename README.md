Django Admin Column Totals
Module to show totals in Django Admin List.

Installation<br>
<code>python -m venv venv</code><br>
<code>source bin/activate</code>

pip install git+https://github.com/legend-king/django-admin-column-totals/

Usage


In settings.py

INSTALLED_APPS = [

    'admin_column_totals',
    
]

In admin.py:

```
from admin_column_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Avg, Min, Max, Count
from .models import TestModel

@admin.register(TestModel)
class TestModelAdmin(ModelAdminTotals):
    list_display = ['name', 'value']
    list_totals = [('value', Sum), ('value', Min), ('value', Avg), ('value', Max), ('value', Count)]
```
![image](https://github.com/legend-king/django-admin-column-totals/assets/72150465/1db74e64-79bc-422d-89c8-6c193733b5e9)


Make sure to at least have the columns of list_totals in list_display.
