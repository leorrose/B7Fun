# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unnecessary-lambda
# pylint: disable=inconsistent-return-statements

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review


@login_required(login_url='/')
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_id = 0
            max_id = Review.objects.all().order_by('id').last()
            if max_id:
                review_id = max_id.id + 1
            Review.objects.create(review_content=form.cleaned_data.get('review_content'), sender_email=request.user.email,
                                  sender_user_name=request.user.user_name, rating=form.cleaned_data.get('rating'), id=review_id)
            return redirect('reviews:reviews_list')
    else:
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})


@login_required(login_url='/')
def reviews_list(request):
    reviews = Review.objects.all().order_by('-date')
    reviews_objects_list = list_with_rating_range(reviews)
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews_objects_list})


def list_with_rating_range(reviews):
    for review_item in reviews:
        review_item.rating = range(review_item.rating)
    return reviews
