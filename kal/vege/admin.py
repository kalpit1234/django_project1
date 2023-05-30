from django.contrib import admin
from django.db.models import Sum
# Register your models here.
from .models import*
class ReciepeAdmin(admin.ModelAdmin):
    list_display=['reciepe_name','reciepe_description']  
admin.site.register(Reciepe,ReciepeAdmin)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
class SubjectmarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']  
admin.site.register(Subjectmarks,SubjectmarksAdmin)
class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_ranks','date_of_report_card','total_marks']
    def total_marks(self,obj):
        subject_marks=Subjectmarks.objects.filter(student=obj.student)
        print(subject_marks.aggregate(marks=Sum('marks')))
        
        return 0

admin.site.register(ReportCard,ReportCardAdmin)