from django import forms

from .models import Tasks, Category

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category 
        fields = ('name', 'description')


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Tasks 
        fields = ('name', 'description', 'end_date', 'end_date', 'priority', 'category', 'status')
