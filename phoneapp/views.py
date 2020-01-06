from django.shortcuts import render
from .models import Bb
from .models import Rubric

from django.views.generic.edit import CreateView
from .forms import BbForm

from django.urls import reverse_lazy

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'phoneapp/index.html', context={'bbs': bbs, 'rubrics': rubrics})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'phoneapp/by_rubric.html', context)

#Форма для модели
class BbCreateView(CreateView):
    template_name = 'phoneapp/create.html'
    form_class = BbForm  #класс формы связанный с моделью
    success_url = reverse_lazy('index')  # перенаправление на главную страницу

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


