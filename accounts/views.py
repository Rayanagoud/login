# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from .models import CustomUser, QuizResult,QuizQuestion, QuizSession
from logzero import logger
import csv 
from django.http import HttpResponse
from django.contrib import messages


def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Set email as the username
            user.save()
            login(request, user)
            return redirect('reg_success')  # Replace 'dashboard' with your desired login success URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)            
        except CustomUser.DoesNotExist:
            logger.info("User %s does not exist")
            return redirect('login') 
        if user.password==password:
            # Password is correct, authenticate the user
            # You can set a session variable to indicate the user is logged in
            # Redirect or perform further actions here
            logger.info("Authentication successful")

            # You can set a session variable to indicate the user is logged in
            login(request, user)

            # Set a session timeout (1 minutes)
            timeout_minutes = 1
            request.session.set_expiry(60 * timeout_minutes)
            return redirect('profile') 
        
    logger.info("invalid username or password")

    # For GET requests, render the login form
    return render(request, 'login.html')

@login_required
def profile_view(request):
    # Add code to display the dashboard or profile page
    user = request.user
    return render(request, 'profile.html',{"fname": user.fname, "password": user.password}) 


# Create your views here.
@login_required
def success_reg(request):
    user = request.user
    # Add code to display the dashboard or profile page
    return render(request, 'register_successful.html') 

@login_required
def update_profile(request):
    if request.method == 'POST':
        # Get the form data
        job_role = request.POST.get('job_role')
        years_of_experience = request.POST.get('years_of_experience')

        # Get the currently logged-in user
        user = request.user

        # Create or update the user's profile data in the database
        quiz_result,created  = QuizResult.objects.get_or_create(username=user.email)
        quiz_result.job_role = job_role
        quiz_result.years_of_experience = years_of_experience
        quiz_result.save()

        # Redirect to a success page or any other appropriate page
        return render(request, 'start_quiz.html',{'profile_update':True}) # Change 'success_page' to the URL name of your success page

    # Render the form page for GET requests
    return render(request, 'profile.html',{'profile_update':False})


@login_required
def quiz(request):
    return render(request, 'quiz.html',{'profile_update':True})


@login_required
def load_questions_from_csv(request):
    if request.method == "POST":
        # Open and read the CSV file
        with open(r'D:\Django\Quiz\login\mcq_questions.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            # Create QuizQuestion objects and save them to the database
            for row in csv_reader:
                question, option1, option2, option3, option4, answer, marks, _ = row
                question_obj = QuizQuestion(
                    question=question,
                    option1=option1,
                    option2=option2,
                    option3=option3,
                    option4=option4,
                    answer=answer,
                    marks=int(marks),
                )
                question_obj.save()
                logger.info(question_obj.question)
        # Redirect to the first question
        return redirect('show_question', question_id=108)

    return HttpResponse("Invalid Request")


@login_required
def show_question(request, question_id):
    print("hi")
    question = get_object_or_404(QuizQuestion, id=question_id)
    next_question_id = question_id + 1
    return render(request, 'question.html', {'question': question,'next_question_id': next_question_id})


@login_required
def submit_answer(request, question_id):
    question = get_object_or_404(QuizQuestion, id=question_id)
    user_answer = request.POST.get('user_answer')

    if user_answer == question.answer:
        question.correct = True
        question.save()
        print("yes")
        messages.success(request, "Correct!")
    else:
        print("no")
        messages.error(request, "Incorrect.")

    if question.id < QuizQuestion.objects.count():
        next_question_id = question.id + 1
        return redirect('show_question', question_id=next_question_id)
    else:
        return redirect('quiz_results')