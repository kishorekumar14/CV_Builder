from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'), 
    path('form/', views.form),
    path('personaldetails/',views.personal),
    path('resume/',views.resume),
    path('updateform/',views.updateform),
    path('pdfresume/',views.pdf_resume),
]