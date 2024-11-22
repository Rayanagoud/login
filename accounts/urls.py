# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'), 
    path('start_quiz.html/', views.update_profile, name='start_quiz'),
    path('reg_success/', views.success_reg, name='reg_success'),
    path('quiz/', views.quiz, name='quiz'),
    path('load-questions/', views.load_questions_from_csv, name='load_questions_from_csv'),
    path('show_question/<int:question_id>/', views.show_question, name='show_question'),
    # path('submit-answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
    # path('quiz-results/', views.quiz_results, name='quiz_results'),
    
    # path('quiz', views.quiz, 'quiz')
      
    # Add more URL patterns as needed
]

