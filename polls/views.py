from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    #render함수는 템플릿 파일에 context 변수를 적용하여 사용자에게 보여줄 index.html을 만들고
    #이를 담아서 HttpResponse 객체를 반환, 즉 index 뷰함수는 HttpResponse 객체를 반환

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question':question
    })

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except  (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message':"You didn't have a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(p.id,)))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {
        'question':question,
    })
