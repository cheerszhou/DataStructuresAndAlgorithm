import json

import get_book_catalog as catalog
import get_chapter_content_from_url as chapter


# book_url 为能够获取书籍目录的网页地址
def get_book_content_from_web(book_url, book_name):
    # 获取目录
    catalog.get_abook_catalog_from_url(book_url, book_name)
    # 创建文件
    with open(f'{catalog.get_desktop_path_byPath()}/{book_name}.txt', 'w', encoding='utf-8') as file:
        file.write('\n')
    # 获取目录dict
    with open('catalog.json', 'r', encoding='utf-8') as file:
        json_dict = json.load(file)

    # 写入文件
    with open(f'{catalog.get_desktop_path_byPath()}/{book_name}.txt', 'a', encoding='utf-8') as file:
        for key, value in json_dict.items():
            file.write(f'{key}\n\n')
            lines = chapter.get_chapter_content_from_url(value)
            # for line_text in lines:
            #     file.write(line_text)
            file.writelines(lines)
            file.write('\n')
            print(f'{key} 写入完成!')


if __name__ == '__main__':
    # get_book_content_from_web('http://www.9999txt.org/book/86459.html', '凡徒')
    get_book_content_from_web('http://www.9999txt.org/book/90898.html', '请叫我幻仙')
