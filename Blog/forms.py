from django import forms
from . models import post,Comment

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title','author','body')
#         widgets = {

#             'title': forms.TextInput(attrs={'class':'form-control'}),
#             'author': forms.Select(attrs={'class':'form-control'}),
#             'body': forms.Textarea(attrs={'class':'form-control'}),
            
#         }


class EditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','description','image', 'date')
        widgets = {

            'title': forms.TextInput(attrs={'class':'form-control'}),
            
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs = {'class':'form-control'})
            
        }

