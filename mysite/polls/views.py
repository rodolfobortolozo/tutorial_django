from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

#Index
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question': latest_question_list,}
    # return HttpResponse(template.render(context, request))
    context = {'latest_question': latest_question_list}
    return render(request, 'polls/index.html', context)

#Detalhes
def detail(request, questionId):
    # try:
    #     question = Question.objects.get(pk=questionId)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk = questionId)
    return render(request, 'polls/detail.html', {'question': question})

#Resultados
def results(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/results.html', {'question': question})

#Votação
def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    
    try:
        selected_choice  = question.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))