from django.contrib import admin
from .models import (AccountNumber,Employees, Origin,Months,Counterparty,
                    RawMaterial,ProductName,Table)

class AccounNumberAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    ordering = ['id']
admin.site.register(AccountNumber,AccounNumberAdmin)

admin.site.register(Employees)
admin.site.register(Origin)
admin.site.register(Months)
admin.site.register(Counterparty)
admin.site.register(RawMaterial)
admin.site.register(ProductName)
admin.site.register(Table)

