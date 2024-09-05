from bs4 import BeautifulSoup
import requests


def get_chapter_content_from_url(chapter_url):
    novel_web_domain = 'http://www.9999txt.org'

    # 下载网页内容
    response = requests.get(f'{novel_web_domain}{chapter_url}')
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取的下一页url
    next_page_url = soup.select('#next_url')[0].get('href')

    # 获取内容
    article = soup.find('article').contents
    chapter_lines = list(map(lambda x: '\n' if x.text.isspace() else x.text.strip(), article))

    # 获取的下一页内容
    next_res = requests.get(f'{novel_web_domain}{next_page_url}')
    next_soup = BeautifulSoup(next_res.text, 'html.parser')
    next_article = next_soup.find('article').contents
    for p in next_article:
        if p.text.isspace():
            chapter_lines.append('\n')
        else:
            chapter_lines.append(p.text.strip())

    return chapter_lines


if __name__ == "__main__":
    result = get_chapter_content_from_url('http://www.9999txt.org/read/90898/32875704.html');
