from django.urls import path

from dashboard.views import HomepageView

app_name = 'dashboard'

urlpatterns = [
    path('', HomepageView.as_view(), name='dashboard'),
]