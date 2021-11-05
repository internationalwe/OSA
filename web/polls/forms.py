from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('drink_count', 'drink_amount', 'smoke_yn', 'smoke_amount', 'exercise_count',
                  'height', 'weight', 'family_stroke', 'family_highBlood', 'family_diabetes', 'family_etc')
