import xpaths
import side_commands

import time
import pyautogui


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.relative_locator import with_tag_name


class Tasks:

    driver = None

    def __init__(self, driver_obj):
        self.driver = driver_obj
        # self.driver = webdriver.Chrome()

    def wait_and_find_element(self, ele_xpath):
        ele = None
        try:
            ele = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, ele_xpath))
            )
        except Exception as e:
            print(e)
        return ele

    def send_chat_messege(self, messege):
        # box = driver.find_element_by_xpath(input_path)
        c_box = self.driver.find_element_by_xpath(xpaths.chat_box_input)
        c_box.send_keys(messege)
        c_box.send_keys(Keys.ENTER)
        time.sleep(1)

    def move_to_group(self, group_name):
        s_bo = self.wait_and_find_element(xpaths.search_box)
        s_bo.click()
        s_bo.send_keys(group_name)
        time.sleep(2)
        s_bo.send_keys(Keys.ENTER)
        self.send_chat_messege("Hi! I'm SideBot :)")


    def updateStatus(self, status_text):
        # Pressing CTRL + ALT + P
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('p').perform()

        # Finding About Div
        aboutDiv = self.wait_and_find_element(xpaths.about_div)

        time.sleep(1)
        # Finding Pencil Btn
        pencilBtn = aboutDiv.find_element_by_xpath(xpaths.pencil_btn)
        pencilBtn.click()

        time.sleep(1)

        pyautogui.click(310, 910)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a', 'backspace')
        pyautogui.typewrite(status_text)


        ticked = self.wait_and_find_element(xpaths.tick_btn)
        ticked.click()

        time.sleep(2)
        actions.send_keys(Keys.ESCAPE).perform()


    def check_and_movelastgroupmessage(self):
        last_chat_div = self.wait_and_find_element(xpaths.last_div_side)
        try:
            last_messege = last_chat_div.text
            lasttext = last_messege.splitlines()
            # print(lasttext)
            if str(lasttext[-1]).isdigit() and lasttext[3] == ': ':
                # print("MESSAGE IS FROM GROUP")
                # Check if sidebotcall if true then move to it and update status
                if side_commands.change_group in last_messege:
                    last_chat_div.click()
                    # self.updateStatus(f"In {lasttext[0]}")
                    time.sleep(1)
                    self.send_chat_messege("Hi! I'm Side BOT :)")

            else:
                # print("FROM USER")
                pass

        except IndexError:
            pass
            # Valid New Messege from other group


            # Check if last part is int (no of new messages shown in bubble) if it's there that means it's new valid message from other group


            # Group Name at 0
            # Chat name
        finally:
            pass


    def send_attachment(self, path):
        attachment_section = self.wait_and_find_element(xpaths.attachment_btn)
        attachment_section.click()
        image_box = self.wait_and_find_element(xpaths.attachment_img)
        image_box.send_keys(path)
        time.sleep(2)
        send_button = self.wait_and_find_element(xpaths.attachment_send)
        send_button.click()

    def reply_to_new_messege(self):
        lst_msg_div = self.wait_and_find_element(xpaths.last_messege_in_div)
        action = ActionChains(self.driver)
        # double click operation and perform
        action.double_click(lst_msg_div).perform()
        print("Clicked")

        time.sleep(1)
