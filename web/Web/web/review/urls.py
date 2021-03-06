from django.urls import path

from web.review import views

app_name = "review"

urlpatterns = [
    path('', views.ReviewHomePageView.as_view(),
         name='main'),

    # Ajax views
    path('get_docs/', views.DocAJAXView.as_view(),
         name='get_docs'),
]
