from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, resolve, reverse_lazy
from apps.core.models import ProblemMapping
from apps.core.views import LoginRequiredView
from django.views.generic.edit import UpdateView
from apps.core.models import Answer
from apps.student.forms import AnswerForm
from django.contrib import messages

class Update(LoginRequiredView, UpdateView):
    model = Answer
    fields = ['value','email', 'first_name', 'last_name']
    template_name = 'staff/users/update.jinja'
    success_url = reverse_lazy('student:problems_show')

class ProblemsIndex(LoginRequiredView):
    def get(self, request):
        problems = request.user.problems.all()
        return render(request, 'student/problems/index.jinja', {
            'problems': problems
        })

class ProblemsShow(LoginRequiredView):
    def get(self, request, problem_id):
        form = AnswerForm()
        problem = request.user.problems.get(pk=problem_id)
        request.session['problem_id'] = problem_id
        return render(request, 'student/problems/show.jinja', {
            'problem': problem,
            'form': form
        })

class AnswerUpdate(LoginRequiredView):
    def post(self, request):
        problem_id = request.session['problem_id']
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer(value=form.cleaned_data['value'], user_id=request.user.id,
                problem_id=request.session['problem_id'])
            answer.save()
            return redirect('student:problems_show', problem_id=problem_id)
        else:
            messages.add_message(request, messages.INFO, 'Answer is in invalid format')
            return redirect('student:problems_show', problem_id = problem_id)
