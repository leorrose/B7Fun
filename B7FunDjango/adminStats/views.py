# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import User, Logins

@login_required(login_url='/')
def show_stats(request, year=datetime.now().year):
    if not request.user.is_admin:
        return redirect('feed:feed')
    graph_sign_up_title = "number of sign up`s to the system in year " + str(year) + " by month"
    graph_sign_in_title = "number of sign in`s to the system in year " + str(year) + " by month"

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sign_ups = []

    # get sign in counts by month of that year
    sign_ups_users = User.objects.all()
    sign_ups_users_by_year = [user for user in sign_ups_users if int(user.date_joined.strftime('%Y')) == year]
    sign_ups_users_months = [int(user.date_joined.strftime('%m')) for user in sign_ups_users_by_year]
    sign_ups = [sign_ups_users_months.count(i) for i in range(1, 13)]

    # get sign in counts by month of that year
    sign_in_users = Logins.objects.all()
    sign_in_users_months = [user.login_month for user in sign_in_users if user.login_year == year]
    sign_ins = [sign_in_users_months.count(i) for i in range(1, 13)]

    return render(request, 'adminStats/show_statistics.html', {'labels':months, 'sign_ups': sign_ups,
                                                               'graph_sign_up_title': graph_sign_up_title,
                                                               'sign_ins': sign_ins, 'graph_sign_in_title':graph_sign_in_title})
