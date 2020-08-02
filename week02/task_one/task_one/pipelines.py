# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from week02.task_one.task_one.db.movie_mysql import ConnDB


class TaskOnePipeline(object):

    def process_item(self, item, spider):

        connect_db = ConnDB()

        movie_name = item['movie_name']

        movie_type = item['movie_type']

        movie_time = item['movie_time']

        values = (movie_name, movie_type, movie_time)

        connect_db.run('geek_python', values)

        return item
