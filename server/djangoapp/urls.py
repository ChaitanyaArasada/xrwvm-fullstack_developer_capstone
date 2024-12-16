from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path(route='register', view=views.registration, name='register'),

    # Path for login
    path(route='login', view=views.login_user, name='login'),

    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Path for dealer reviews view
    path(route='dealer/<int:dealer_id>/reviews', view=views.get_dealer_reviews, name='dealer_reviews'),

    # Path for add a review view
    path(route='dealer/<int:dealer_id>/add_review', view=views.add_review, name='add_review'),

    # Path for dealership list
    path(route='dealerships', view=views.get_dealerships, name='dealerships'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
