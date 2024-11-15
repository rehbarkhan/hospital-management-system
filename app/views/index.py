from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app/index.html', {})