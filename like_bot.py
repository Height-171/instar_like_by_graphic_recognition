"""
Author:
Last Modification: 2022.10.05
E-mail
https:
"""

from selenium import webdriver
import pywinmacro as pw
import pyautogui as pg
import time

class LikeBot:
    def __init__(self, like_button):
        self.like_button = like_button
        self.tag_url = "https://instagram.com/explore/tags/"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def login(self, id, ps):
        # 로그인 페이지로 이동
        self.driver.get("https://www.instagram.com/accounts/login")

        # 로그인
        time.sleep(5)
        pw.key_press_once("tab")
        pw.typing(id)
        pw.key_press_once("tab")
        pw.typing(ps)
        pw.key_press_once("enter")
        time.sleep(5)

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")

    def search_tag(self, tag):
        self.driver.get(self.tag_url + tag)
        time.sleep(5)

    def select_picture(self):
        # 탭 키를 여러번 누르기
        for i in range(5):
            pw.key_press_once("tab")

        # 엔터키 누르기
        pw.key_press_once("enter")

    # 좋아요 누르는 함수
    def press_link(self):
        like_location = pg.locateCenterOnScreen(self.like_button)
        print(like_location)
        if like_location:
            pw.click(like_location)
        time.sleep(3)

    def insta_jungdok(self, tag, click_num):
        self.search_tag(tag)
        self.select_picture()
        for i in range(click_num):
            self.press_link()
            time.sleep(3)
            pw.key_press_once("right_arrow")
            time.sleep(3)

