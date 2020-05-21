from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='index'),
    path('material-act', views.material_act_form, name="material_act_form"),
    path('material-act/<int:act_id>', views.material_act_form_details, name="material_act_form_details"),
    path('material-act/<int:act_id>/pdf', views.material_act_form_details_pdf, name="material_act_form_details_pdf"),
    path('material-act/<int:act_id>/materials', views.material_form, name="material_form"),
]
