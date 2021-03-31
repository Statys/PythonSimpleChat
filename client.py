#подключаем библиотеки
import socket
import threading

#создаём сокет
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#подключаемся к серверу
client.connect(("127.0.0.1", 65432))

def send(name):
    #бесконечный цикл ожидающий ввода пользователя
    #и отправляющий данные на сервер
    while True:
        msg = input()
        data = name + '>' + msg
        #выполняем код внутри блока обработки исключений для игнорирования ошибок(правильно - корректно обрабатывать ошибки, не делайте так)
        try:
            client.send(data.encode("utf-8"))
        except Exception as x:
            print(x)
            break

def receive():
    #бесконечный цикл слушающий сервер
    while True:
        try:
            data = client.recv(1024)
            print('\n' + str(data.decode("utf-8")))
        except Exception as x:
            print(x)
            break

print('Enter your name:')
#вводим отображаемое имя пользователя
name = input()

#создаём поток для отсылки данных
thread_send = threading.Thread(target = send,args=[name])
thread_send.start()
#создаём поток для получения данных
thread_receive = threading.Thread(target = receive)
thread_receive.start()