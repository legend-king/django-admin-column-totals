Django Admin Column Totals
Module to show totals in Django Admin List.

Installation
virtualenv .
source bin/activate
Or
pip install git+https://github.com/douwevandermeij/admin-totals.git
Usage
In settings.py

INSTALLED_APPS = [
    'admin_column_totals',
]
In admin.py:

from admin_column_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Avg, Min, Max, Count
from .models import TestModel

@admin.register(TestModel)
class TestModelAdmin(ModelAdminTotals):
    list_display = ['name', 'value']
    list_totals = [('value', Sum), ('value', Min), ('value', Avg), ('value', Max), ('value', Count)]
Make sure to at least have the columns of list_totals in list_display.
