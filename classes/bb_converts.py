def date_us_ru(data):
    data = str(data)
    ret = ''
    if len(data) == 10:
        try:
            ret = f"{int(data[8:10:1]):02}.{int(data[5:7:1]):02}.{int(data[0:4:1]):04}"
        except ValueError:
            pass
            # print('error in date_us_ru(data)')
    return ret

def date_ru_us(data):
    tst = str(data)
    ret = '1900-01-01'
    if len(tst) > 0:
        try:
            if len(tst) == 4:
                tst = f"01.01.{int(tst):04}"
            elif 0 < len(tst) < 3:
                tst = f"01.01.20{int(tst):02}"
            ret = f"{int(tst[6:10:1]):04}-{int(tst[3:5:1]):02}-{int(tst[0:2:1]):02}"
        except ValueError:
            pass
            # print('error in date_ru_us(data)')
    return ret

def get_day_list(con):
    cur = con.cursor()
    sql = "select name from days order by id"
    res = cur.execute(sql).fetchall()
    return [s[0] for s in res]

def get_short_day_list(con):
    cur = con.cursor()
    sql = "select cname from days order by id"
    res = cur.execute(sql).fetchall()
    return [s[0] for s in res]

def get_time_list(con):
    cur = con.cursor()
    sql = "select name from times order by id"
    res = cur.execute(sql).fetchall()
    return [s[0].strip() for s in res]
    # spis = []
    # for i in range(20):
    #     spis.append(f'{8 + i // 2:02}:{i * 30 % 60:02} ')
    # return spis


def get_kab_list(con):
    cur = con.cursor()
    sql = "select name, color from kabs order by id"
    res = cur.execute(sql).fetchall()
    return [s[:2] for s in res]

    # return [['21', (85, 85, 255)],
    #         ['22', (255, 0, 0)],
    #         ['24', (255, 170, 0)],
    #         ['25', (255, 255, 0)],
    #         ['27', (196, 0, 127)],
    #         ['28', (0, 170, 0)]]



