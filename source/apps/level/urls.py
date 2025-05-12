from django.urls import path

from .views import GlucoseLevelView

urlpatterns = [
    path("levels", GlucoseLevelView.as_view()),
    path("levels/<int:user_id>/", GlucoseLevelView.as_view()),
]
