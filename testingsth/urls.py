from django.contrib import admin
from django.urls import path
from .views import Home, BuildCabinet, BuildQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('/buildCabinet', BuildCabinet.as_view(), name="buildCabinet"),
    path('/buildQuestion', BuildQuestion.as_view(), name="buildQuestion")
]
