import csv
import openpyxl
from django.http import HttpResponse
from django.db import models


def export_data(queryset, file_format):
    if file_format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        fields = [field.name for field in queryset.model._meta.fields]

        writer = csv.writer(response)
        writer.writerow(fields)

        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in fields])

    elif file_format == 'xlsx':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="export.xlsx"'

        fields = [field.name for field in queryset.model._meta.fields]

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Export'
        ws.append(fields)

        for obj in queryset:
            row = [getattr(obj, field) for field in fields]
            ws.append(row)

        wb.save(response)

    return response
