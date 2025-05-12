from django.urls import path

from .views import GlucoseLevelView

urlpatterns = [
    path("", GlucoseLevelView.as_view()),
    path("user_id/<str:user_id>/", GlucoseLevelView.as_view()),
    path("id/<str:id>/", GlucoseLevelView.as_view()),
]
