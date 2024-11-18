from django.contrib import admin
from .models import Student, Test, Result  # ≤мпортуЇмо вс≥ ваш≥ модел≥

# –еЇструЇмо модел≥ в адм≥н панел≥
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Result, ResultAdmin)
