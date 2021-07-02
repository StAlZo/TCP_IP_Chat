import socket
import time
from config import ADDR, FORMAT, DISCONNECT_MESSAGE


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def receive(client):
    mes = client.recv(16)
    print(f'{mes.decode()}')


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect()
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)
        receive(connection)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()