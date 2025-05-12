from django.urls import path

from .views import GlucoseLevelView

urlpatterns = [
    path("", GlucoseLevelView.as_view()),
    path("<str:user_id>/", GlucoseLevelView.as_view()),
]
