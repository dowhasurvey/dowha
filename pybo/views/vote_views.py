from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user in question.voter.all():
        # 좋아요 취소
        question.voter.remove(request.user)
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user in answer.voter.all():
        # 좋아요 취소
        answer.voter.remove(request.user)
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)
