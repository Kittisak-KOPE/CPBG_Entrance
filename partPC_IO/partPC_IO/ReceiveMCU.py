import serial
import time
class ReceiveMCU:
    def getValuMCU(self):
        SerialObj = serial.Serial('/dev/ttyACM0')
        SerialObj.timeout = 1
        time.sleep(1)

        # โค้ดเดิม
        # try:
        #     while True:
        #         ReceivedString = SerialObj.readline()
        #         print(ReceivedString)
        # except KeyboardInterrupt:
        #     pass

        # SerialObj.close()

        ReceivedString = SerialObj.readline()
        return ReceivedString




# # โค้ดเดิม
# import serial
# import time
# class ReceiveMCU:
#     def getValuMCU(self):
#         SerialObj = serial.Serial('/dev/ttyACM0')
#         SerialObj.timeout = 1
#         time.sleep(1)
#         try:
#             while True:
#                 ReceivedString = SerialObj.readline()
#                 print(ReceivedString)
#         except KeyboardInterrupt:
#             pass

#         SerialObj.close()