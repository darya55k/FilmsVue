from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    # path('auth/logout', Logout.as_view()),



    path('films/<int:pk>', FilmListIdView.as_view()),
    path('films/all', FilmListView.as_view()),
    path('authorings/<int:pk>', AuthoringRetrieveView.as_view()),
    path('authorings/update/<int:pk>', AuthoringUpdateView.as_view()),
    path('authorings/all', AuthoringListView.as_view()),
    path('authorings/new', AuthoringCreateView.as_view()),
]