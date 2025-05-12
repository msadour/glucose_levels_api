from django.urls import path

from .views import GlucoseLevelView

urlpatterns = [
    path("", GlucoseLevelView.as_view()),
    path("<int:user_id>/", GlucoseLevelView.as_view()),
]
