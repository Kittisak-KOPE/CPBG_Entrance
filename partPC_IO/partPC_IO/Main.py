import serial
import time
import cv2
import datetime
from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util

from db_pq import databasepq

count = 0

def MCU():
    SerialObj = serial.Serial('/dev/ttyACM0')
    SerialObj.timeout = 1
    time.sleep(1)
    try:
        while True:
            ReceivedString = SerialObj.readline()
            # print(ReceivedString)
            return ReceivedString
    except KeyboardInterrupt:
        pass

    SerialObj.close()

def Camera(count):
    vidcap = cv2.VideoCapture(0)    #'rtsp://admin:Sp_123456@192.168.50.145:554'
    _, image = vidcap.read()
    urlImage = f'dataImage/frame{count}.jpg'
    cv2.imwrite(urlImage, image)
    # print(urlImage)
    currentDate = datetime.datetime.now()
    currentDate = (str(currentDate.strftime("%Y-%m-%d %H:%M:%S")))
    # time.sleep(3)
    return urlImage, currentDate

def Cardreader():
    WAIT_FOR_SECONDS = 30

    card_type = AnyCardType()
    request = CardRequest(timeout=WAIT_FOR_SECONDS, cardType=card_type)
    service = None
    try:
        service = request.waitforcard()
    except CardRequestTimeoutException:
        print("ERROR: No card detected")
        exit(-1)
    conn = service.connection
    conn.connect()

    get_uid = util.toBytes("FF CA 00 00 00")
    # print("ATR = {}".format(util.toHexString(conn.getATR())))----------------------------------
    data, sw1, sw2 = conn.transmit(get_uid)
    uid = util.toHexString(data)
    # status = util.toHexString([sw1, sw2])
    # print("UID = {}\tstatus = {}".format(uid, status))-------------------------------------------
    # print(uid)
    return uid

def toDB(uid_, urlImage_, currentDate_):
    db = databasepq(
        host = 'localhost',
        database = 'sp_parking',
        user = 'postgres',
        password = 'postgres',
        port = 5432
    )
    # db.query('DROP TABLE IF EXISTS parkingdata')

    # create_script = '''
    #             CREATE TABLE IF NOT EXISTS parkingdata(
    #                 id          serial PRIMARY KEY,
    #                 card_id     varchar(40) NOT NULL,
    #                 data_cam    varchar(40) NOT NULL,
    #                 data_date   varchar(40) NOT NULL
    #             )
    #             '''

    # db.query(create_script)

    insert_script = f"INSERT INTO parkingdata (card_id, data_cam, data_date) VALUES ('{uid_}', '{urlImage_}', '{currentDate_}')"
    # print(insert_script)
    db.query(insert_script)
    print("done")
    db.close()

try:
    while True:
        trigerSwitch = MCU()
        x = b'1\r\n'
        if(trigerSwitch == x):
            uid = Cardreader()
            urlImage, currentDate = Camera(count)
            toDB(uid, urlImage, currentDate)
            count += 1

except KeyboardInterrupt:
    pass
