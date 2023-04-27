from django.shortcuts import render, get_object_or_404, redirect
from .models import Tests, QuizQuestion, QuizOption, QuizResult


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


def quiz(request, pk):
    test = get_object_or_404(Tests, id=pk)

    if request.method == 'POST':
        # Handle quiz submission
        score = 0
        for question in QuizQuestion.objects.filter(test=test):
            selected_option_id = int(request.POST.get(str(question.id)))
            selected_option = QuizOption.objects.get(id=selected_option_id)
            if question.is_reversed:
                score += selected_option.score
            else:
                score += selected_option.score
        result = QuizResult.objects.create(user=request.user, score=score, test=Tests.objects.get(id=1))
        return redirect('quiz_result', result_id=result.id)
    else:
        # Display quiz questions
        questions = QuizQuestion.objects.filter(test=test)

        context = {
            'questions': questions,
            'test': test
        }

        return render(request, 'tests/quiz.html', context)


def quiz_result(request, result_id):
    result = QuizResult.objects.get(id=result_id)
    return render(request, 'tests/quiz_result.html', {'result': result})
