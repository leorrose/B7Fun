# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unnecessary-lambda

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ReportsForm
from .models import Reports


@login_required(login_url='/')
def report(request):
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            Reports.objects.create(content=form.cleaned_data.get('content'), sender_email=request.user.email,
                                   subject=form.cleaned_data.get('subject'))

            return redirect('feed:feed')
    form = ReportsForm()
    return render(request, 'reports/report.html', {'form': form})
