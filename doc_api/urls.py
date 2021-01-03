
from django.urls import path,include
from .views import *
app_name = 'doc_api'


urlpatterns = [
    path('list_of_proof_categories/',ListOfCategoriesView.as_view()),
    path('list_of_proof/<str:state>',ListOfProofsView.as_view()),
    path('process_of_proof/<str:pk>',ProofDetailAPIView.as_view()),
    path('feedback/',FeedbackAPIView.as_view()),

    path('search_proof/',ProofSearchAPIView.as_view()),
]