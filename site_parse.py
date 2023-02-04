from selenium import webdriver
from selenium.webdriver.common.by import By

from config import LOGIN, PASSWORD, COMMENTS_ADDRESS, LOGIN_ADDRESS
from utils import get_gapon_comments, get_bad_comments
from settings import START_TIME, END_TIME


def parse_site(quantity_checked_pages):
    browser = webdriver.Chrome("chromedriver")
    browser.maximize_window()

    try:
        browser.get(LOGIN_ADDRESS)
        browser.find_element("id", "email").send_keys(LOGIN)
        browser.find_element("id", "password").send_keys(PASSWORD)
        browser.find_element(By.CLASS_NAME, "btn").click()
        browser.get(COMMENTS_ADDRESS)

        gapon_comments_id = []
        bad_comments_id = {}

        for page in range(0, quantity_checked_pages):
            browser.get(f"{COMMENTS_ADDRESS}/page/{page}")
            tbody = browser.find_elements(
                By.XPATH, "//tr[@class='bg-green-transparent']"
            )

            for posts in tbody:

                post = posts.text.split("\n")

                post_time = int(post[0][12:14])
                if START_TIME <= post_time <= END_TIME:
                    gapon_comments_id = get_gapon_comments(post, gapon_comments_id)
                    bad_comments_id = get_bad_comments(post, bad_comments_id)

        return [gapon_comments_id, bad_comments_id]

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()
