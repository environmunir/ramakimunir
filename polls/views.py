from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


#           Base
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


#           Detail
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


#           Results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#           Vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# for error link or blank page
def error_link(request, question_id):
    return HttpResponse("Sorry my love!, \n   You are searching a wrong link, please check your URL again.")
