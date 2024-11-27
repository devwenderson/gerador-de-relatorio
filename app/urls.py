from django.urls import path, include
from django.contrib.auth.views import LoginView

from app.views.main import ( 
    index, 
    get_report, 
    logout_view,
)

from app.routes import work, location 


urlpatterns = [
    path('', index, name='index'),
    path('orcamento/', get_report, name='get-report'),
    
    #Autenticação
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", logout_view, name="logout"),

    # Obras
    path("obras/", include(work)),
    # location
    path("locais/", include(location)),
]