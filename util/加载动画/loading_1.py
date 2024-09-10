import time
import threading
import requests


# 定义一个函数来显示加载动画
def loading_animation():
    chars = '/—\\|'
    idx = 0
    while not getattr(loading_animation, 'stop', False):
        print(chars[idx % len(chars)], end='\r')
        idx += 1


# 发起网络请求的函数
def fetch_url(url):
    try:
        # 开始一个线程用于显示加载动画
        thread = threading.Thread(target=loading_animation)
        thread.start()

        # 发起网络请求
        response = requests.get(url)

        # 停止加载动画
        loading_animation.stop = True
        thread.join()

        # 检查请求是否成功
        if response.status_code == 200:
            return len(response.text)
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except Exception as e:
        # 停止加载动画
        loading_animation.stop = True
        thread.join()
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    # 使用示例
    url = 'https://book.flutterchina.club/chapter8/listener.html#_8-1-2-listener-组件'  # 替换为你想要请求的实际URL
    print("Fetching data...")
    result = fetch_url(url)
    print("\nData fetched:")
    print(result)
