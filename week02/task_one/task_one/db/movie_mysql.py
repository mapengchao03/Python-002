# 实际使用数据库
import pymysql


class ConnDB(object):

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '12345678'
        self.db = 'geek_python'
        self.charset = 'utf8mb4'

    # 新增单行数据，需要传入表名
    def run(self, table_name, values):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )

        cur = conn.cursor()

        try:

            sql = 'INSERT INTO ' + table_name + '(movie_name, movie_type, movie_time)' + ' values(%s, %s, %s)'
            cur.execute(sql, values)
            cur.close()
            conn.commit()

        except:
            conn.rollback()
        conn.close()

#
# if __name__ == '__main__':
#
#     db = ConnDB()
#     values = (4,4,4)
#     db.run('geek_python', values)
