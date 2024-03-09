# coding=utf-8
from __future__ import division, print_function, unicode_literals

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList


class CalculateTotals(ChangeList):
    def get_results(self, *args, **kwargs):
        super(CalculateTotals, self).get_results(*args, **kwargs)
        if hasattr(self.model_admin, 'list_totals'):
            self.aggregations = []
            self.total_aggregations = []
            list_totals_dict = dict(self.model_admin.list_totals)
            list_totals = self.model_admin.list_totals
            for field in self.list_display:
                if field in list_totals_dict:
                    summary=""
                    total_summary=""
                    for total_list_field in list_totals:
                        if total_list_field[0] == field:
                            summary+=f"{total_list_field[1].__name__}={self.result_list.aggregate(agg=total_list_field[1](total_list_field[0]))['agg']}\n"
                            total_summary+=f"{total_list_field[1].__name__}={self.queryset.aggregate(agg=total_list_field[1](total_list_field[0]))['agg']}\n"
                    
                    self.aggregations.append(
                        summary
                        )
                    self.total_aggregations.append(
                        total_summary 
                    )
                else:
                    self.aggregations.append('')
                    self.total_aggregations.append('')
            self.aggregations[0]='Page'
            self.total_aggregations[0]='Total'


class ModelAdminTotals(admin.ModelAdmin):
    change_list_template = 'admin_column_totals/change_list_totals.html'

    def get_changelist(self, request, **kwargs):
        return CalculateTotals
