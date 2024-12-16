from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)
# Create a `login_request` view to handle sign-in requests
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')

    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}
    
    if user is not None:
        # If user is valid, call login method to log in the current user
        login(request, user)
        response_data["status"] = "Authenticated"
    else:
        response_data["status"] = "Failed"

    return JsonResponse(response_data)

# Create a `logout_request` view to handle sign-out requests
@csrf_exempt
def logout_request(request):
    if request.method == "POST":
        # Get the username before logging out
        username = request.user.username if request.user.is_authenticated else ""
        
        # Log the user out
        logout(request)
        
        # Prepare the response
        data = {"userName": username, "status": "Logged out"}
        return JsonResponse(data)

# Create a `registration` view to handle sign-up requests
@csrf_exempt
def registration(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "Failed", "message": "Username already exists"})
        
        User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"status": "Success", "message": "User registered successfully"})

# Placeholder views for dealership functionalities

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    # Logic to fetch dealerships
    return HttpResponse("List of dealerships")

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    # Logic to fetch dealer reviews
    return HttpResponse(f"Reviews for dealer {dealer_id}")

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    # Logic to fetch dealer details
    return HttpResponse(f"Details for dealer {dealer_id}")

# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Logic to add review
        return JsonResponse({"status": "Review added"})
