from django.urls import path,include
from core.views import HomeView,ChangeView,StudentView
from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register(r'student', StudentView)



urlpatterns=[
    path('home/',HomeView.as_view()),
    path('change/<int:user_id>',ChangeView.as_view()),
    path('', include(router.urls)),
    
]