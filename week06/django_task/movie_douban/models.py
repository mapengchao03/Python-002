from django.db import models

# Create your models here.


class MovieShortComments(models.Model):
    short_comment = models.TextField('短评', max_length=5000, blank=True, null=True)
    star = models.CharField('星级', max_length=3)
    comment_time = models.CharField('评论时间', max_length=50)

    class Meta:
        verbose_name = '短评数据'
        verbose_name_plural = '电影短评数据列表'
        db_table = "movie_short_comments"
