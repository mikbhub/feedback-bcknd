from django import forms
from . models import Feedback
from django.utils.translation import ugettext_lazy as _


#TODO: rewrite form as forms.form without refering to any model as a
#  fix for validation: email is being validatet as customer instance.
class FeedbackForm(forms.Form):

    name = forms.CharField(max_length=128)
    customer = forms.EmailField()
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    

# class FeedbackForm(forms.ModelForm):

#     # customer = forms.EmailField()

#     class Meta:
#         model = Feedback
#         fields = (
#             'title',
#             'description',
#             'customer',
#         )

#         labels = {
#             'customer': _('Your email'),
#         }

#         help_texts = {
#             'description': _('Please describe your problem.'),
#         }

#         # widgets = {
#         #     'customer': forms.EmailInput(),
#         # }
