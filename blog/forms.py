# from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
# from .models import Blog, Comment
#
#
# class BlogForm(ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title', 'text', 'photo'] # 'category'
#         widgets = {
#             "title": TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Post title"
#             }),
#             # "text": Textarea(attrs={
#             #     "class": "form-control",
#             #     "placeholder": "Post full-text"
#             # }),
#             'photo': FileInput(attrs={
#                 'class': 'form-control',
#             }),
#             # 'author': Select(attrs={
#             #     'class': 'form-select'
#             # })
#             'category': Select(attrs={
#                 'class': 'form-select'
#             })
#         }
#
#
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body']
#
#         widgets = {
#             'body': Textarea(attrs={
#                 "rows": 3,
#                 "class": "form-control",
#                 "placeholder": "Write your comment ...",
#             })
#         }
