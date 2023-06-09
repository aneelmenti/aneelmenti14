"""
URL configuration for aneelmenti14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainbowapp.views import RainbowInput,RainbowInsert,RainbowDispaly,RainbowDeleteInput,RainbowDelete,RainbowUpdateInput,RainbowUpdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rainbowapp/',RainbowInput.as_view()),
    path('rainbowapp/insert',RainbowInsert.as_view()),
    path('rainbowapp/display',RainbowDispaly.as_view()),
    path('rainbowapp/deleteinput',RainbowDeleteInput.as_view()),
    path('rainbowapp/delete',RainbowDelete.as_view()),
    path('rainbowapp/updateinput',RainbowUpdateInput.as_view()),
    path('rainbowapp/update',RainbowUpdate.as_view()),

]
