import socket
#إنشاء سوكيت للسيرفر
s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind((host,port))
print("Waiting for connection...")
#وضع السيرفر في حالة انتظار للاتصالات
s.listen(5)
#نعرف متغير هو رسالة بحالة سخان المياه
status="The Heater Is ON"
#نقوم باسقبال الاتصال
conn,addr = s.accept()
print('Got Connection from', addr)
while True:
	#نقوم بارسال الحالة
	conn.send(status.encode())
	#نستقبل الأمر
	msg=conn.recv(1024).decode()
	if msg=="off":
		status="Heater is turned off"
		conn.send(status.encode())
	elif msg=="let":
		conn.send("OK".encode())
	elif msg=="on":
		status="Heater is turned on"
		conn.send(status.encode())
	else:
		conn.send("error input".encode())
