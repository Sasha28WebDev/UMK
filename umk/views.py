from django.shortcuts import render,get_object_or_404,get_list_or_404,get_object_or_404
from .models import Direction,Document,Institute
from django.http import FileResponse, Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.template.loader import render_to_string
from docxtpl import DocxTemplate
import weasyprint

import os
from io import BytesIO
from django.http import FileResponse

# Институт

class InstituteListView(ListView):
    model = Institute
    template_name = 'institute/institutes.html'

class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'institute/institute_detail.html'

class InstituteCreateView(CreateView): 
    model = Institute
    template_name = 'institute/institute_new.html'
    fields = ['name', 'info']

class InstituteUpdateView(UpdateView): 
    model = Institute
    template_name = 'institute/institute_edit.html'
    fields = ['name', 'info']

class InstituteDeleteView(DeleteView): 
    model =  Institute
    template_name = 'institute/institute_delete.html'
    success_url = reverse_lazy('umk:institutes')
'''
def get_institutes(request):
    institutes = Institute.objects.all()
    return render (request, 'institute/institutes.html',{'institutes': institutes})
'''
# Направления подготовки

class DirectionListView(ListView):
    model = Direction
    template_name = 'direction/directions.html'

class DirectionDetailView(DetailView):
    model = Direction
    template_name = 'direction/direction_detail.html'

class DirectionCreateView(CreateView): 
    model = Direction
    template_name = 'direction/direction_new.html'
    fields = ['name', 'code','standart_period','qualification','fgos','institute']
    #А в CreateView вместо атрибута fields используйте form_class для использования вашей формы. 

class DirectionUpdateView(UpdateView): 
    model = Direction
    template_name = 'direction/direction_edit.html'
    fields = ['name', 'info']

class DirectionDeleteView(DeleteView): 
    model =  Direction
    template_name = 'direction/direction_delete.html'
    success_url = reverse_lazy('umk:directions')

def get_directions(request):
    directions = Direction.objects.all()
    return render (request, 'direction/directions.html',{'directions': directions})

def get_document(request,file_id):
    try:
        file1 = get_object_or_404(Document,id = file_id)
        f = 'media/' + str(file1.document)
        return FileResponse(open(f,'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

