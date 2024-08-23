from multiprocessing import Process, Lock, Pipe
from DataBase import config
from DataBase import models




#подключаемся к сессии (у двух процессов одна и та же сессия)
session = config.session

# объявляем классы для работы
Product = models.Product
Order = models.Order
Consumer = models.Consumer
Size = models.Size
Color = models.Color
Category = models.Category
Country = models.Country
















#mutex блокирует доступ к БД
def main(mutex: Lock, connect_with_consumer_send: Pipe):


    with mutex:
        pass

    with session as db:
        models.create_tables()
        pass

    #while True:

        #try:
            #connect_with_consumer_send.send("Hello from admin")

        #except:
            #print("Break")
            #break