from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
class VideoView(TemplateView):
    template_name = 'video.html'
class usuarioView(TemplateView):
    template_name = 'usuario.html'
