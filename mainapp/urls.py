from django.urls import path

from .views import *
urlpatterns = [
    path("SchoolAPIView/",SchoolAPI.as_view() ),
    path("StudentAPIView/",StudentAPI.as_view() ),
    path("SchoolUpdateAndDeleteAPI/<int:id>",SchoolUpdateAndDeleteAPI.as_view() ),
    path("StudentUpdateAndDeleteAPI/<int:id>",StudentUpdateAndDeleteAPI.as_view() ),
    path("SpecificSchoolAPI/<int:id>",SpecificSchoolAPI.as_view() ),
    path("SpecificStudentAPI/<int:id>",SpecificStudentAPI.as_view() ),
    path("SearchAPI/",SearchAPI.as_view() ),
    
]