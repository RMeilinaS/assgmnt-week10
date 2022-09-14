from temperatur import temp_chk
from sendUbidots import sendData

suhu = temp_chk()
sendData(suhu)
