from django.urls import path 
from .views import news_list , news_detail , HomePageView , ContactPageView , viewPage404 , LocalNewsView, \
      ForeignNewsView, TechnologyNewsView, SportNewsView , NewsDeleteView , NewsUpdateView  , NewsCreateView , admin_page_view


urlpatterns = [
    path('', HomePageView.as_view(), name='index_page'),
    path('all/', news_list, name='all_news_list'),
    path('news/create/' , NewsCreateView.as_view(), name='news_create') , 
    path('news/<slug:news>/' , news_detail  ,  name='news_detail_page'),
    path('news/<slug>/edit/' , NewsUpdateView.as_view(), name='news_update') , 
    path('news/<slug>/delete/' , NewsDeleteView.as_view(), name='news_delete') , 
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('error/', viewPage404, name='error_page'),
    path('local/',LocalNewsView.as_view(), name='local_news_page'), 
    path('foreign/',ForeignNewsView.as_view(), name='foreign_news_page'),
    path('technology/',TechnologyNewsView.as_view(), name='technology_news_page'),
    path("sport/",SportNewsView.as_view(), name='sport_news_page'),
    path('adminpage/' , admin_page_view , name= "admin_page" ) , 
    
]

