"""
URL configuration for config project.

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

from django.contrib import admin
from django.urls import path
from config.views import main, burger_list, APImap

#views.py에 작성한 main 함수를 가져오기
#burger_list 함수를 추가적으로 import


urlpatterns = [
    path("admin/", admin.site.urls),
    # 경로를 지정하지 않으면 main 직원을 호출한다
    path("", main), #공백(아무것도 입력하지 않은 경로)과 main 함수를 연결
    # 'burgers' 경로로 접근하면 burger_list라는 직원을 호출한다.
    path("burgers/", burger_list),
    # 'mapAPI' 경로로 접근하면 APImap라는 직원을 호출한다.
    path("APImap/", APImap),
]
