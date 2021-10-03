import time
import xpaths
import side_commands

from whatsappTasks import Tasks
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


if __name__ == '__main__':

    prof = webdriver.FirefoxProfile('C:/Users/Siddhant/AppData/Roaming/Mozilla/Firefox/Profiles/ga88yjoc.Sid')

    opt = Options()
    # opt.headless = True
    # opt.profile = prof
    driver = webdriver.Firefox(options=opt, firefox_profile=prof)

    # options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=C:\\Users\\Siddhant\\AppData\\Local\\Google\\Chrome\\User Data")
    # driver = webdriver.Chrome(options=options)

    driver.get('https://web.whatsapp.com/')

    start = Tasks(driver)
    start.wait_and_find_element(xpaths.welcome_screen)

    # Getting into Playroom Group
    start.move_to_group("Playroom")
    # Updating Status
    # start.updateStatus("In Playroom")

    time.sleep(1)

    messageId = None

    try:

        while True:
            # Check side chat message
            start.check_and_movelastgroupmessage()


            # Check current group message
            lst_sndr = start.wait_and_find_element(xpaths.last_sender_in)
            lst_msg = start.wait_and_find_element(xpaths.last_messege_in)

            if messageId != lst_sndr.id:
                messageId = lst_sndr.id

                sendr = lst_sndr.get_attribute("data-pre-plain-text")
                msg = lst_msg.text

                if "#sidebot" in msg:
                    side_commands.perform_function(start, sendr, msg)

                # print("New Message Arrived")
                # print(lst_sndr.get_attribute("data-pre-plain-text"))
                # print(lst_msg.text)
                # print()



            time.sleep(1)

        # print('Done')

    except Exception as e:
        print(e)
