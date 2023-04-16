from django.urls import path
from input.views import *

urlpatterns = [
    
    path('', reverse_text, name='reverse_text'),
    path('delete_text/<id>', delete_text, name='delete_text'),
    # path('display_texts', display_texts, name='display_texts')

]
