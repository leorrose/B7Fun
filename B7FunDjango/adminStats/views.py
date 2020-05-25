from django.shortcuts import render
from datetime import datetime
from accounts.models import User


def show_stats(request, year):
    graph_sign_up_title = "number of sign up`s to the system in year " + str(year) + " by month"

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sign_ups = []

    # get sign in counts by month of that year
    sign_in_users = User.objects.all()
    sign_in_users_by_year = [user for user in sign_in_users if int(user.date_joined.strftime('%Y')) == year]
    sign_in_users_months = [int(user.date_joined.strftime('%m')) for user in sign_in_users_by_year]
    sign_ups = [sign_in_users_months.count(i) for i in range(1, 13)]
    print(sign_ups)

    return render(request, 'adminStats/show_statistics.html', {'labels':months, 'sign_ups': sign_ups,
                                                               'graph_sign_up_title': graph_sign_up_title})
