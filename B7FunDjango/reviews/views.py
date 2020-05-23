# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unnecessary-lambda

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review


@login_required(login_url='/')
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(review_content=form.cleaned_data.get('review_content'),
                                           sender_email=request.user.email,
                                           sender_user_name=request.user.user_name,
                                           rating=form.cleaned_data.get('rating'))
            print(review.review_content)
            review.save()
            redirect('feed:feed')
    else:
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})


