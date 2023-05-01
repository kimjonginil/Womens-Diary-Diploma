from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tests, QuizQuestion, QuizOption, QuizResult, QuizResultText


def TestsPage(request):
    tests = Tests.objects.all()

    context = {
        'tests': tests
    }

    return render(request, 'tests/tests.html', context)


def TestsDetail(request, pk):
    test = get_object_or_404(Tests, id=pk)

    context = {
        'test': test
    }

    return render(request, 'tests/tests-detail.html', context)


def ResultText(test_id, score, user):
    quiz_result_text = QuizResultText.objects.filter(test=test_id)
    for i in quiz_result_text:
        if score in i.score:
            EmailMessage(
                subject=f'Answer of the test: {i.test.title}',
                body=f'Your result: '
                     f'{i.text}',
                from_email='womenssdiary@gmail.com',
                to=[user.email]
            ).send()


def Quiz(request, pk):
    test = get_object_or_404(Tests, id=pk)

    if request.method == 'POST':
        # Handle quiz submission
        score = 0
        for question in QuizQuestion.objects.filter(test=test):
            selected_option_id = int(request.POST.get(str(f'question{question.id}')))
            selected_option = QuizOption.objects.get(id=selected_option_id)
            if question.is_reversed:
                score += selected_option.score
            else:
                score += selected_option.score
        result = QuizResult.objects.create(user=request.user, score=score, test=Tests.objects.get(id=pk))

        ResultText(test_id=pk, score=score, user=request.user)

        messages.success(request, 'We have sent your email the test results.')
        return redirect('tests')
    else:
        # Display quiz questions
        questions = QuizQuestion.objects.filter(test=test)

        context = {
            'questions': questions,
            'test': test
        }

        return render(request, 'tests/quiz.html', context)
