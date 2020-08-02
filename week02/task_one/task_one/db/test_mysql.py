# 这是仅仅只是测试链接数据库
import pymysql

dbinfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '12345678',
    'db': 'geek_python'
}

sql_select = ['select 1', 'select VERSION()']

result = []


class ConnDB(object):
    def __init__(self, dbInfo, sql_select):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbinfo['db']
        self.sql_select = sql_select

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        cur = conn.cursor()

        try:
            for command in self.sql_select:
                cur.execute(command)
                result.append(cur.fetchone())
            cur.close()
            conn.commit()

        except:
            conn.rollback()
        conn.close()


if __name__ == '__main__':

    db = ConnDB(dbinfo, sql_select)
    db.run()
    print(result)
