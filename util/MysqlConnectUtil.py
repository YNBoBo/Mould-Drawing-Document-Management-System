import pymysql

from entity.Mould import mould

cnx = None


def connect_to_mysql():
    global cnx
    config = {
        'host': 'localhost',
        'database': 'wdf',
        'user': 'root',
        'password': 'admin'
    }
    try:
        cnx = pymysql.connect(**config)
        print("成功连接到 MySQL 数据库")
    except pymysql.MySQLError as err:
        print(f"连接 MySQL 数据库时出错: {err}")


def query_data(query):
    cursor = cnx.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchone();
    except pymysql.MySQLError as err:
        print(f"查询数据时出错: {err}")
    finally:
        cursor.close()


def insert_data(insert_query):
    cursor = cnx.cursor()
    try:
        cursor.execute(insert_query)
        cnx.commit()
        print("数据插入成功")
    except pymysql.MySQLError as err:
        print(f"插入数据时出错: {err}")
    finally:
        cursor.close()


def main():
    connect_to_mysql()
    if cnx:
        query_result = query_data("select * from mould")
        mould_test = mould(*query_result)
        mould_test.display_info()
        print(query_result)


if __name__ == "__main__":
    main()
