"""
URL configuration for kal project.

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
from vege.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
   path('recieps/',recieps,name="recieps"),
   path("Delete_recieps/<id>/",Delete_recieps,name="Delete_recieps"), ## Delete_recieps/<id>/ is a dynamic url    
   path("update_recieps/<id>/",update_recieps,name="update_recieps"),## update_recieps/<id>/ is a dynamic url  
    path("login_page/",login_page,name="login_page"),
    path("logout_page/",logout_page,name="logout_page"),
    path("register_page/",register_page,name="register_page"),
    path('student/',get_students,name="get_students"),
      path("check_themarks/<student_id>/",see_marks,name="see_marks"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
