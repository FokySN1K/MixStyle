import multiprocessing
from threading import Thread, Lock
from multiprocessing import Process, Lock
import openpyxl 
import pandas as pd


from admin import admin
from consumer import consumer


###################
#   admin - запускает свой тг-бот, с помошью которого осуществляется
#   выгрузка/загрузка информации из БД для администратора
#
#
#
##########


###################
#   consumer - запускает свой тг-бот, с помошью которого осуществляется
#   выгрузка/загрузка информации из БД для покупателя.
#   К тому же становяться доступны функции заказа, просмотра каталога и прочего
#
#
##########




if __name__ == '__main__':


    print(1234)



    try:
        # создаем разделяемую pipe, в которой будем принимать
        # различные команды от оболочки admin (и читать их с помощью созданного
        # потока в consumer)

        # 1 - отправить сообщение всем пользователям о смене ассортимента
        # 2 -
        # 3 -
        # 4 -
        # 5 -
        # ...
        #
        # команды будут дописываться

        connect1, connect2 = multiprocessing.Pipe(duplex=True)




        # создаем mutex для параллельной работы процессов c БД
        mutex = multiprocessing.Lock()


        # создаем два процессы для работы
        admin = Process(target=admin.main, args=(mutex, connect1, ), daemon=False)
        consumer = Process(target=consumer.main, args=(mutex, connect2, ),  daemon=False)





        #запускаем процессы
        admin.start()
        consumer.start()



    except:
        print("False")










if __name__ == '__main__':
    pass