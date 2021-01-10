from django.db import models
from user.models import *
# Create your models here.
# 歌手信息表singer
class Singer(models.Model):

    singer_id = models.AutoField('序号', primary_key=True)
    singer_name = models.CharField('姓名', max_length=45)
    singer_type = models.CharField('类型', max_length=45)
    singer_masterwork = models.CharField('代表作', max_length=45)
    singer_sex = models.CharField('性别', max_length=45)
    song_nums = models.CharField('歌曲数', max_length=45)
    singer_img = models.CharField('照片', max_length=45)
    singer_information = models.CharField('简介', max_length=1000)
    # plays_total = models.CharField('总播放量', max_length=45)
    
    def __str__(self):
        return self.singer_name
    
    class Meta:
        
        # 设置Admin界面的显示内容
        verbose_name = '歌手信息'
        verbose_name_plural = '歌手信息'

# 歌手动态表singerDynamic
class SingerDynamic(models.Model):
   
    dynamic_id = models.AutoField('序号', primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, verbose_name='姓名')
    singer_plays = models.IntegerField('播放次数')
    singer_search = models.IntegerField('搜索次数')
    singer_down = models.IntegerField('下载次数')

    class Meta:
       
        # 设置Admin界面的显示内容
        verbose_name = '歌手动态'
        verbose_name_plural = '歌手动态'

# 用户关注歌手表singerfollow
class FollowStatus(models.Model):
   
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户ID')
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, verbose_name='歌手ID')
    follow_time = models.CharField('关注时间', max_length=50, null=True, blank=True)
       
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '关注状态'
        verbose_name_plural = '关注状态'
# # 关注反映       
# class FollowRelation(models.Model):
#     followed = models.CharField(max_length=128, blank=True, null=True)
#     following = models.CharField(max_length=128, blank=True, null=True)
#     follow_time = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):
#         return self.followed, '<<<', self.following