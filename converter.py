from classes.cl_users import Users
from classes.db_session import connectdb
import datetime

if __name__ == '__main__':
    con = connectdb('db\\database_J.db')
    us = Users(con)
    for user in us.data:
        # if len(user[8].strip()) > 0:
        #     ret = user[8]
        #     bd = datetime.date(int(ret[6:10:1]), int(ret[3:5:1]), int(ret[0:2:1]))
        #     print(user[0], bd)
        #     us.rec_update(user[0], {'birthday': bd})
        if len(user[9].strip()) > 0:
            ret = user[9].strip().replace('\n', '')
            us.rec_update(user[0], {'sertificate': ret})
    us.commit()
