"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from django.views.static import serve

from MxOnline.settings import MEDIA_ROOT
from users.views import LoginView,LogoutView,RegisterView
from users.views import IndexView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^$', IndexView.as_view(),name='index'),
    re_path(r'^login/$', LoginView.as_view(),name='login'),
    re_path(r'^logout/$', LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    re_path(r'active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    # 课程机构app相关url配置
    path("org/", include('organization.urls', namespace="org")),
    # 课程app相关url配置
    path("course/", include('courses.urls', namespace="course")),

    #个人信息
    path("users/", include('users.urls', namespace="users")),
    #静态文件
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_ROOT }),

    # 富文本相关url
    path('ueditor/',include('DjangoUeditor.urls' )),
]

# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'