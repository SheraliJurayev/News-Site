from django.urls import path 
from .views import news_list , news_detail , HomePageView , ContactPageView , viewPage404 


urlpatterns = [
    path('', HomePageView.as_view(), name='index_page'),
    path('all/', news_list, name='all_news_list'),
    path('news/<slug:news>/' , news_detail  ,  name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('error/', viewPage404, name='error_page'),
]

