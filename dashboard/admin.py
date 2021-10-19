from django.contrib import admin
from .models import courseKeywords, courseDirection, courses

admin.site.register(courseKeywords)
admin.site.register(courseDirection)
admin.site.register(courses)
