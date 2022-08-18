import psycopg2
import psycopg2.extras

conn = None

urlImage_       = '01 34 56 12'
currentDate_    = 'dataImage/frame0.jpg'
uid_             = '2022-08-17 17:18:48'
value_all = (urlImage_, currentDate_, uid_)

try:
    with psycopg2.connect(
        host = 'localhost',
        dbname = 'sp_parking',
        user = 'postgres',
        password = 'postgres',
        port = 5432
    ) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS employee')
            create_script = '''
            CREATE TABLE IF NOT EXISTS parkingdata(
                card_id     varchar(40) PRIMARY KEY NOT NULL,
                data_cam    varchar(40) NOT NULL,
                data_date   varchar(40) NOT NULL
            )
            '''
            cur.execute(create_script)

            insert_script = 'INSERT INTO parkingdata (card_id, data_cam, data_date) VALUES (%s, %s, %s)'
            cur.execute(insert_script, value_all)
            
            # update_script = 'UPDATE parkingdata SET data_date = data_date + (data_date + "test")'
            # cur.execute(update_script)               
            
            # delete_script = 'DELETE FROM parkingdata WHERE card_id = %s'
            # delete_record = ('03 34 56 12',)
            # cur.execute(delete_script, delete_record)
            
            # cur.execute('SELECT * FROM parkingdata')
            # for record in cur.fetchall():
            #     print(record['data_cam'], record['data_date'])

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()