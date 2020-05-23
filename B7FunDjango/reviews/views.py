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
            id = Review.objects.count() + 1
            review = Review.objects.create(review_content=form.cleaned_data.get('review_content'),
                                           sender_email=request.user.email,
                                           sender_user_name=request.user.user_name,
                                           rating=form.cleaned_data.get('rating'),
                                           id=id)
            print(review.review_content)
            print(type(review.rating))
            return redirect('reviews:reviews_list')
    else:
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})


def reviews_list(request):
    reviews = Review.objects.all().order_by('-date')
    reviews_list = list_with_rating_range(reviews)
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews_list})


def list_with_rating_range(reviews):
    for review in reviews:
        review.rating = range(review.rating)
    return reviews
