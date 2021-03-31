#подключаем библиотеки
import socket
import threading

def accept_client():
    #бесконечный цикл с прослушиванием клиентов
    while True:
        #принимаем запрос на подключение
        cli_sock, cli_add = ser_sock.accept()
        #добавляем новое соединение
        CONNECTION_LIST.append(cli_sock)
        #поднимаем новый поток под каждое соединение
        thread_client = threading.Thread(target = broadcast_usr, args=[cli_sock])
        thread_client.start()
        print(f'{cli_sock.getsockname()} enter in chat')


def broadcast_usr(cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                b_usr(cli_sock, data)
        except Exception as x:
            print(x)
            break

#бродкастим сообщение(отсылаем всем) 
def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        client.send(msg)

#массив соединений
CONNECTION_LIST = []

# socket
ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
HOST = '127.0.0.1'
PORT = 65432
#поднимаем 
ser_sock.bind((HOST, PORT))

# listen
ser_sock.listen(1)
print('Chat server started on port : ' + str(PORT))

#запускаем поток с прослушиванием коннектов
thread_ac = threading.Thread(target = accept_client)
thread_ac.start()