from django.db import models

# Create your models here.

# 留言板的数据库表单
# 李张岩
# 2021年1月4日21:45:23


class Message(models.Model):

    message_id = models.AutoField('留言序号', primary_key=True)
    message_text = models.TextField('留言内容', max_length=1000, null=True, blank=True)
    message_user = models.CharField('留言用户', max_length=20, null=True, blank=True)
    message_date = models.CharField('日期', max_length=50, null=True, blank=True)
    message_like = models.IntegerField('点赞数', default=0)

    def __str__(self):
        return str(self.message_id)

    class Meta:
        # 设置后台Admin界面显示的内容
        verbose_name = '网站留言'
        verbose_name_plural = '网站留言'


