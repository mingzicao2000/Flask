import pymysql


def select(sql):
    conn = pymysql.connect(host='localhost', user='root', password='teamproject', port=3306, db='test_schema')
    cur = conn.cursor()
    # build connection to database, user, password and database might be different

    cur.execute(sql) # perform the query
    u = cur.fetchall()

    cur.close()
    conn.close()
    return u # return a list


def insert(table, dic):
    conn = pymysql.connect(host='localhost', user='root', password='teamproject', port=3306, db='test_schema')
    cur = conn.cursor()
    if table == 'user':
        sql = "INSERT INTO user(user_name,first_name,last_name,user_Email,user_phone,account_type,user_password,user_question,user_answer,verified) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "#check if the database column name is different
        rows = cur.execute(sql,(dic["username"],dic["first_name"],dic["last_name"],dic["user_email"],dic["user_phone"],dic["account_type"],dic["user_password"],dic["user_question"],dic["user_answer"],dic["verified"]))

        # rows = cur.executemany(sql, values) # if more than one row

        conn.commit()
        cur.close()
        conn.close()


def update(table,query,limit,col,new_value):
    conn = pymysql.connect(host='localhost', user='root', password='teamproject', port=3306, db='test_schema')
    cur = conn.cursor()
    sql = "update "+table+" set "+col+"= %s"+" where "+query+"= %s"
    rows = cur.execute(sql,(new_value,limit))
    conn.commit()
    cur.close()
    conn.close()