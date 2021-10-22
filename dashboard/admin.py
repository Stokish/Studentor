from django.contrib import admin
from .models import CourseKeywords, CourseDirection, Course

admin.site.register(CourseKeywords)
admin.site.register(CourseDirection)
admin.site.register(Course)
