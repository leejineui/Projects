# 예제 3-38 라이브러리 추가하기
import platform
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


def youtube():
    # 예제 3-39 webdriver로 크롬 브라우저 실행하기
    browser = webdriver.Chrome('c:/driver/chromedriver.exe')
    url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
    browser.get(url)
    # 예제 3-40 페이지 정보 가져오기
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # page crawl
    page = 1
    url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(
        page)
    print(url)
    # 예제 3-49 반복문으로 유튜브 랭킹 화면의 여러 페이지를 크롤링하기
    results = []
    for page in range(1, 11):
        url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
        browser.get(url)
        time.sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        channel_list = soup.select('form > table > tbody > tr')
        for channel in channel_list:
            title = channel.select('h1 > a')[0].text.strip()
            category = channel.select('p.category')[0].text.strip()
            subscriber = channel.select('.subscriber_cnt')[0].text
            view = channel.select('.view_cnt')[0].text
            video = channel.select('.video_cnt')[0].text
            data = [title, category, subscriber, view, video]
            results.append(data)
    print("@##########")

    df = pd.DataFrame(results)
    df.columns = ['title', 'category', 'subscriber', 'view', 'video']
    df.to_excel('./files/youtube_rank.xlsx', index=False)  # Cr
    print("========저장")

    time.sleep(3)
    browser.quit()

    return results

    # 예제 3-50 데이터 칼럼명을 설정하고 엑셀 파일로 저장하기


# if __name__ == "__main__":
#     youtube()
