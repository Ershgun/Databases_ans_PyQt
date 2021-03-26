"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import Popen, PIPE
from socket import gethostbyname, gaierror


def host_ping(list_ip_addresses, timeout=500, requests=1):
    """
    Функция проверяет доступность сетевых узлов
    :param list_ip_addresses: список ip адресов и доменных имён
    :param timeout: таймаут запросов, 500 = 0.5 сек
    :param requests: количество запросов
    :return []: возврат словаря с доступными и недоступными узлами
    """
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}  # словарь с результатами
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        # обойдем такие исключения
        except ValueError:
            address = get_host_by_name(address, get_ip_address=True)
        process = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        # проверяем код завершения подпроцесса
        if process.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            result_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            result_string = f'{address} - Узел недоступен'
        print(result_string)
    return results


def get_host_by_name(address, get_ip_address=False):
    try:
        # преобразуем доменное имя к ip-адресу
        ip = gethostbyname(address)
        print(f'*** Доменное имя: {address} преобразовано в ip-адрес: {ip} ***')
        if get_ip_address:
            ip = ip_address(ip)
        return ip
    except gaierror:
        print(f'!!! Не удалось получить ip адрес по доменну имени: {address}. Проверьте корректность !!!')


if __name__ == '__main__':
    ip_addresses = ['yandex.ru', 'google.com', 'goodddddgle.com', '2.2.2.2', '192.168.0.100', '192.168.0.101']
    host_ping(ip_addresses)
