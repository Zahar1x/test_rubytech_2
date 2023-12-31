import asyncio
import re
import time

import aiohttp as aiohttp
from tqdm import tqdm


def A(links):
    for link in links:
        print('Check link: ' + link)
        pattern = re.compile(r'^https?:\/\/github\.com\/[-a-zA-Z0-9]+\/([-a-zA-Z0-9_]+)')
        res = pattern.findall(link)
        print(res, '\n')


def B(list1, list2):
    resList = {}
    if len(list1) > len(list2):
        for l in list2:
            resList[l] = list1[list2.index(l)]
    else:
        for l in list1:
            resList[l] = list2[list1.index(l)]
    print('\nTask B result: ')
    print(resList)


def C(l):
    new_list = []
    for it in l:
        try:
            num = int(it)
            new_list.append(num)

        except:
            new_list.append(it)

    res = list(map(lambda x: 'abc_' + x + '_cba' if type(x) == str else pow(x, 2), new_list))
    return res


async def D(url, times):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in tqdm(range(times), desc=f"fetching data from {url}...", colour='GREEN'):
            tasks.append(asyncio.create_task(session.get(url)))

        resp = await asyncio.gather(*tasks)
        return [await r.json() for r in resp]


def run_case_D(func, path, times):
    start_time = time.time()

    asyncio.run(func(path, times))

    task_time = round(time.time() - start_time, 2)
    rps = round(times / task_time, 1)
    print(f'Num of requests = {times}, Total time = {task_time} s, Requests per second = {rps} \n')


class E:


    def __init__(self, text):
        self.text = text

    def commonWord(self):
        """
        Этот метод находит самое часто встречающееся слово в тексте
        """
        lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')', '?', '_', '`']  # и т.д.
        lst = []

        for word in self.text.lower().split():
            if not word in lst_no:
                _word = word
                if word[-1] in lst_no:
                    _word = _word[:-1]
                if word[0] in lst_no:
                    _word = _word[1:]
                lst.append(_word)

        _dict = dict()
        for word in lst:
            _dict[word] = _dict.get(word, 0) + 1

        # сортируем словарь посредством формирования списка (значение, ключ)
        _list = []
        for key, value in _dict.items():
            _list.append((value, key))
            _list.sort(reverse=True)

        # самое частое слово в этом тексте
        print(f'самое частое слово в этом тексте -> `{_list[0][1]}`, использовалось `{_list[0][0]}` раз.')


    def maxLengthWord(self):
        """
        Этот метод находит самое длинное слово из текста
        """
        text = self.text.replace('.', '').replace(',', '').replace(':', '').replace('!', '').replace('?', '').split()

        print('Самое длинное слово в тексте: ')
        print(', '.join([word for word in text if len(word) == len(sorted(text, key=len)[-1])]).lower())

    def amountSpecSymb(self):
        """
        Этот метод подсчитывает общее количество спецсимволов в тексте
        """
        lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')', '?', '_', '`', ';']
        res = 0
        for i in lst_no:
            res += self.text.count(i)
        print('Общее кол-во спецсимволов в тексте: ' + str(res))

    def printPalyndorms(self):
        """
        Этот метод находит все палиндромы в тексте
        :return:
        """
        list_pal = []
        for word in self.text.replace('.', '').replace(',', '').replace(':', '').replace('!', '').replace('?', '').split():
            ls = len(word)
            if word[:ls // 2] == word[ls // 2 + 1:][::-1]:
                list_pal.append(word)
        print('палиндромы в тексте: ' + str(list_pal))

def decorator(func):
    start_time = time.time()
    func()
    task_time = time.time() - start_time
    print("Время выполнения функции: " + str(task_time))


if __name__ == '__main__':
    links = []
    with open('Links.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            links.append(line)
    A(links)

    list_C = []
    with open('C.txt', 'r') as f_c:
        while True:
            line = f_c.readline()
            if not line:
                break
            list_C.append(line.replace('\n', ''))
    new_list_c = C(list_C)
    print(new_list_c)

    B(list_C, links)

    run_case_D(D, 'http://httpbin.org/delay/3', 100)

    text_E = ''
    with open('E.txt', 'r') as f_e:
        while True:
            line = f_e.readline()
            if not line:
                break
            text_E += line

    E_class = E(text_E)

    decorator(E_class.maxLengthWord)
    decorator(E_class.commonWord)
    decorator(E_class.amountSpecSymb)
    decorator(E_class.printPalyndorms)
