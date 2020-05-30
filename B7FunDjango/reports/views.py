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
            report_id = 0
            max_id = Reports.objects.all().order_by('id').last()
            if max_id:
                report_id = max_id.id + 1
            Reports.objects.create(content=form.cleaned_data.get('content'), sender_email=request.user.email,
                                   subject=form.cleaned_data.get('subject'), id=report_id)

            return redirect('feed:feed')
    form = ReportsForm()
    return render(request, 'reports/report.html', {'form': form})
