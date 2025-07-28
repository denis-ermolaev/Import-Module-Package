from time import sleep
from tqdm import tqdm


def get_employees():
    print("Получение числа работников из базы данных")
    for i in tqdm(range(0,5)):
        sleep(1)
    print("Всего работников 458")