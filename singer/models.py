from django.db import models

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
    # plays_total = models.CharField('总播放量', max_length=45)
    
    def __str__(self):
        return self.singer_name
    
    class Meta:
        
        # 设置Admin界面的显示内容
        verbose_name = '歌手信息'
        verbose_name_plural = '歌手信息'

# 歌手动态singerDynamic
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