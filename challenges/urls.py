from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.january),
    # path("feb",views.feb)
    path("",views.index, name="index"),
    path("<int:month>",views.challenges_check_by_number),
    path("<str:month>",views.challenges_check, name="check")
]
