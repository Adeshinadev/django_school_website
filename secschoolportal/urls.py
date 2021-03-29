"""keys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import TemplateView
from secschoolportal import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('key.urls')),

    # path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('', include('contents.urls'), name='homepage'),
    path('Request_info', include('Request_info.urls'), name='Request_info'),
    path('admission_portal/', include('admission_portal.urls')),
    path('accounts/', include('account.urls')),
    path('student_Datasss/', include('student_Datasss.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('payment/', include('payment.urls')),
]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)