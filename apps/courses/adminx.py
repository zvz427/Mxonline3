# users/adminx.py

import xadmin

from .models import Course,Lesson,Video,CourseResource,BannerCourse


class LessonInline(object):
	model = Lesson
	extra = 0

class CourseAdmin(object):
	# 显示的列
	list_display = ['name','desc','detail','degree','learn_times','students','get_zj_nums','go_to']
	# 搜索的字段
	search_fields = ['name', 'desc', 'detail', 'degree', 'students']
	# 过滤
	list_filter = ['name','desc','detail','degree','learn_times','students']
	#默认排序
	ordering = ['-click_nums']
	#只读字段
	readonly_fields = ['name']
	#隐藏字段
	exclude = ['fav_nums']
	#列表页可以直接编辑
	list_editable = ['degree','desc']
	refresh_times = [3,5]				#自动刷新（里面是秒数范围）
	#配置章节
	inlines = [LessonInline]
	#配置富文本
	style_fields = {"detail": "ueditor"}

	def queryset(self):
		# 重载queryset方法，来过滤出我们想要的数据的
		qs = super(CourseAdmin, self).queryset()
		# 只显示is_banner=True的课程
		qs = qs.filter(is_banner=False)
		return qs

	def save_models(self):
		# 在保存课程的时候统计课程机构的课程数
		# obj实际是一个course对象
		obj = self.new_obj
		# 如果这里不保存，新增课程，统计的课程数会少一个
		obj.save()
		# 确定课程的课程机构存在。
		if obj.course_org is not None:
			#找到添加的课程的课程机构
			course_org = obj.course_org
			#课程机构的课程数量等于添加课程后的数量
			course_org.course_nums = Course.objects.filter(course_org=course_org).count()
			course_org.save()

class BannerCourseAdmin(object):
	# 显示的列
	list_display = ['name','desc','detail','degree','learn_times','students']
	# 搜索的字段
	search_fields = ['name', 'desc', 'detail', 'degree', 'students']
	# 过滤
	list_filter = ['name','desc','detail','degree','learn_times','students']
	#默认排序
	ordering = ['-click_nums']
	#只读字段
	readonly_fields = ['name']
	#隐藏字段
	exclude = ['fav_nums']
	#配置章节
	inlines = [LessonInline]

	def queryset(self):
		#重载queryset方法，来过滤出我们想要的数据的
		qs = super(BannerCourseAdmin, self).queryset()
		#只显示is_banner=True的课程
		qs = qs.filter(is_banner=True)
		return qs

class LessonAdmin(object):
	list_display = ['course', 'name', 'add_time']
	search_fields = ['course', 'name']
	#这里course__name是根据课程名称过滤
	list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
	list_display = ['lesson', 'name', 'add_time']
	search_fields = ['lesson', 'name']
	list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
	list_display = ['course', 'name', 'download', 'add_time']
	search_fields = ['course', 'name', 'download']
	list_filter = ['course__name', 'name', 'download', 'add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)