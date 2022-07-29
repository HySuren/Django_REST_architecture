from django.urls import path
from .views import *

app_name = 'client'
urlpatterns = [
    path('api/v1/client', ClientCreate.as_view()),
    path('clientall/', ClientListView.as_view()),
    path('detail/<int:pk>/', ClientDetailView.as_view()),
    path('api/v1/newsletter', NewsletterCreate.as_view()),
    path('detail/newsletter/', NewsletterListView.as_view()),
    path('detail/put_newsletter/<int:pk>', NewsletterDitailView.as_view()),
    path('detail/message/', MessageListView.as_view()),
    path('api/v1/send_message/', SendMessageView.as_view()),
    path('detail/message/<int:pk>', MessageDetailView.as_view()),
]
