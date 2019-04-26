# users/adminx.py

import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
	# 开启主题功能
	enable_themes = True
	use_bootswatch = True

# 全局修改，固定写法
class GlobalSettings(object):
	# 修改title
	site_title = 'Django Xadmin'
	# 修改footer
	site_footer = '我的公司'
	# 收起菜单
	menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
	# 显示的列
	list_display = ['code','email','send_type','send_time']
	# 搜索的字段
	search_fields = ['code','email','send_type']
	# 过滤
	list_filter = ['code','email','send_type','send_time']
	#icon
	model_icon = 'fa fa-user'
	

class BannerAdmin(object):
	list_display = ['title','image','url','index','add_time']
	search_fields = ['title','image','url']
	list_filter = ['title','image','url','index','add_time']

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)