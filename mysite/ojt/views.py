import json
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
#from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from .papago import papago
from .sens import sens

def index(request):
    """

    ojt 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
#    return HttpResponse("Hello, HUG Page")
    return render(request, 'ojt/question_list.html', context)

def detail(request, question_id):
    """

    ojt 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'ojt/question_detail.html', context)

def answer_create(request, question_id):
    """

    ojt 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('ojt:detail', question_id=question.id)

#def question_create(request):
#    """
#    ojt  질문등록
#    """

#    if request.method == 'POST':
#        form = QustionForm(request.POST)
#        if form.is_valid():
#            question = form.save(commit=False)
#            question.create_date = timezone.now()
#            question.save()s
#            return redirect('ojt:index')
#    else:
#        form = QuestionForm()
#    context = {'form':form}
#    return render(request, 'ojt/question_form.html', context)   

#    form = QuestionForm()
#    return render(request, 'ojt/question_form.html', {'form':form})

def question_create(request):
    """
    ojt 질문등록
    """
    if request.method == 'POST':
#       form = papago(QuestionForm(request.POST))
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.subject = papago(question.subject)
            question.content = papago(question.content)
            sens(question.subject)
            question.save()
            return redirect('ojt:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'ojt/question_form.html', context)    


def question_modify(request, question_id):
    """
    ojt 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
      
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('ojt:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'ojt/question_form.html', context)

def question_delete(request, question_id):
    """
    ojt 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('ojt:index')

def answer_modify(request, answer_id):
    """
    ojt 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            return redirect('ojt:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'ojt/answer_form.html', context)

def answer_delete(request, answer_id):
    """
    ojt 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('ojt:detail', question_id=answer.question.id)
