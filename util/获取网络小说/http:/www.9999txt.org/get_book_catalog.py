import json
import os.path
from pathlib import Path
import requests
from bs4 import BeautifulSoup


def get_desktop_path_byOS():
    return os.path.join(os.path.expanduser('~'), 'Desktop')


# 获取本地桌面路径
def get_desktop_path_byPath():
    return Path.home() / 'Desktop'


# 获取文本中的书名
def get_book_name_from(soup):
    # novel_title = soup.find('div', {'class': 'novel_info_title'})
    novel_title = soup.find('div', class_='novel_info_title')
    book_name = novel_title.find('h1').get_text()
    return book_name


# 将字典写入文件中
def write_dict_to_path(a_dict, file_path='a_dict_json_file.json'):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(a_dict, file, ensure_ascii=False, indent=4)


def get_abook_catalog_from_url(book_url, book_name):
    # 定义要爬虫的页面
    url = book_url

    # 发送HTTP请求, 获取网页内容
    response = requests.get(url)

    # 确保请求成功(状态码200)
    if response.status_code == 200:

        # # 保存原网页
        # with open('output.html', 'w', encoding='utf-8') as file:
        #     file.write(response.text)

        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 提取网页中的文本内容(去除标签后的)
        # text = soup.get_text()

        # 获取网页中的目录
        catalog = soup.select('#ul_all_chapters')
        catalog_texts = []
        catalog_dict = {}
        for chapter in catalog[0].find_all('li'):
            a_catalog_str = f"{chapter.text}: {chapter.next.get('href')} \n"
            catalog_texts.append(a_catalog_str)
            catalog_dict[chapter.text] = chapter.next.get('href')

        # catalog_texts_str = ''.join(catalog_texts)

        # 查找嵌套元素
        # nested_element = soup.select('div.navigation')
        # print(nested_element)

        # 查找带有特定 id 的元素
        # element = soup.select('#logo')
        # print(element)

        # 获取文本中的书名
        book_name = get_book_name_from(soup)
        # book_name = ''.join([book_name, '.txt'])

        # 保存目录json文件到本地
        write_dict_to_path(catalog_dict, file_path='catalog.json')

        # 保存文本到本地
        # file_path = get_desktop_path_byPath() / book_name
        # with open(file=file_path, mode='w', encoding='utf-8') as file:
        #     file.write(catalog_texts_str)
        print(f'获取 {book_name} 目录成功!')
    else:
        print(f"无法获取网页内容，HTTP状态码：{response.status_code}")


if __name__ == '__main__':
    get_abook_catalog_from_url('http://www.9999txt.org/book/90898.html')
