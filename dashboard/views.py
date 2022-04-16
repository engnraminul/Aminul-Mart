from django.shortcuts import render
from django.views.generic import TemplateView

class DashboardIndex (TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/index.html')
