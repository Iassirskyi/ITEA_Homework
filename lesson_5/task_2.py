import requests
from threading import Thread

link_list = ['https://i2.rozetka.ua/goods/16896139/rowenta_x-pert_160_rh7237wob_images_16896139884.jpg',
             'https://i2.rozetka.ua/goods/15582525/xiaomi_deerma_vc20_images_15582525113.jpg',
             'https://i8.rozetka.ua/goods/17155396/125575600_images_17155396343.jpg',
             'https://i8.rozetka.ua/goods/17106355/189870703_images_17106355960.jpg',
             'https://i2.rozetka.ua/goods/17106356/189870703_images_17106356884.jpg',
             'https://i1.rozetka.ua/goods/16819910/mygarden_4744201011668_images_16819910619.jpg',
             'https://i2.rozetka.ua/goods/15997626/167102384_images_15997626821.jpg',
             'https://i1.rozetka.ua/goods/1786706/my_garden_211_4_1200_images_1786706868.jpg',
             'https://i1.rozetka.ua/goods/523673/truper_r_16m_images_523673342.jpg',
             'https://i8.rozetka.ua/goods/18078392/bosch_06033a2721_images_18078392683.jpg']


def my_decorator(func):
    def wrapper(*args):
        t = Thread(target=func, args=args)
        print(f'{t.getName()} started')
        t.start()
        t.join()
        print(f'Downloading from {args} finished')
        return t
    return wrapper


@my_decorator
def get_link(link):
    res = requests.get(link)
    return res


for link in link_list:
    get_link(link)






