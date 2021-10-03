import os.path

from PIL import Image, ImageOps
from selenium.webdriver import ActionChains

import whatsappTasks
import xpaths
import time
import datetime
import re
import random

from whatsappTasks import Tasks
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import side_image_data


class GroupNameExtract:

    @staticmethod
    def get_members(member_list):
        temp = member_list.split(',')
        names_list = list()
        for i in temp:
            names_list.append(i.strip())
        return names_list


def get_group_members_names(taskobj):
    group_members = taskobj.driver.find_element_by_xpath(xpaths.group_member_list)

    while 'is typing' in group_members.text:
        group_members = taskobj.driver.find_element_by_xpath(xpaths.group_member_list)

    memberList = GroupNameExtract.get_members(group_members.text)
    return memberList


def already_there_in_grp(taskobj, sender, command):
    taskobj.send_chat_messege("listening. . .")
    taskobj.send_chat_messege("```For more info. Type``` *#sidebot help*")


def tag_everyone(taskobj, sender, command):
    print(sender)
    pattern = '\[[\d\s\S\w]*\]'
    snr_name = re.sub(pattern, "", sender).strip()[:-1]
    print(snr_name)
    whitelist = []


    memberList = get_group_members_names(taskobj)
    input_path = xpaths.chat_box_input
    box = taskobj.driver.find_element_by_xpath(input_path)

    if snr_name in whitelist:
        box.send_keys("ACCESS DENIED! :-) ")
        box.send_keys(Keys.ENTER)

    else:
        for i in memberList:
            text = "@" + i
            box.send_keys(text)
            box.send_keys(Keys.TAB)
            box.send_keys(Keys.ENTER)


def who_is_online(taskobj, sender, command):
    try:
        wait_time = 10

        last_num = command.strip().split()[-1]
        if last_num.isdecimal():
            wait_time = int(last_num)

        # last_sender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@role,"region")] //div[contains(@class,"message-in")][last()] //div[contains(@data-pre-plain-text,"[")]')))
        # print(last_sender.get_attribute("data-pre-plain-text"))
        #
        # last_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@role,"region")] //div[contains(@class,"message-in")] [last()] //span[contains(@class,"copyable-text") and (@dir)]')))
        # print(last_message.text)

        box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)

        box.send_keys("Checking.... " + Keys.ENTER)

        time.sleep(1)
        # for i in last_message:
        #     print(i.text)
        # driver.find_element_by_id().

        # time.sleep(5)

        last_messageBox = taskobj.driver.find_element_by_xpath(
            '//div[contains(@role,"region")] //div[contains(@class,"message-out")] [last()] //span[contains(@class,"copyable-text") and (@dir)]')
        # action = ActionChains(driver)
        # # double click operation and perform
        # action.double_click(last_messageBox).perform()
        # print("Clicked")
        print(last_messageBox.text)

        hover = ActionChains(taskobj.driver).move_to_element(last_messageBox)
        hover.perform()

        print("Hovered")

        time.sleep(1)

        down_btn = taskobj.driver.find_element_by_xpath(
            '//div[contains(@role,"region")] //div[contains(@class,"message-out")][last()] //div[contains(@data-js-context-icon,"true")]')
        down_btn.click()

        time.sleep(1)
        msg_info = taskobj.driver.find_element_by_xpath('//div[contains(@aria-label,"Message info")]')
        msg_info.click()

        time.sleep(2)

        time.sleep(wait_time)

        all_ele = taskobj.driver.find_elements_by_xpath(
            '//header[contains(string(),"Message")]/parent::div/div [last()]/div/div/div/div')

        seenData = dict()

        for i in all_ele:
            print(i.text)
            mat = str(i.value_of_css_property("transform"))
            pix = int(mat[mat.rindex(',') + 1:-1])

            name = i.text.split('\n')[0]
            seenData[pix] = name

        print(seenData)
        print()

        seen_names = []
        for i in sorted(seenData.keys()):
            if "remaining" in seenData[i]:
                break

            seen_names.append(seenData[i])

        del seen_names[0]
        print(seen_names)

        if len(seen_names) == 0:
            box.send_keys("No One!")
            box.send_keys(Keys.ENTER)
        else:
            for i in seen_names:
                text = "@" + i
                box.send_keys(text)
                box.send_keys(Keys.TAB)
                box.send_keys(Keys.ENTER)

        box.send_keys("(y)")
        box.send_keys(Keys.ENTER)
        # box.send_keys(Keys.ESCAPE
        time.sleep(2)
        ActionChains(taskobj.driver).send_keys(Keys.ESCAPE).perform()

    except Exception as e:
        print(e)
    finally:
        pass
        # driver.quit()


def invalid_messege(taskobj):
    taskobj.reply_to_new_messege()
    doge = 'res/images/invalid_command/doge_angry.png'
    pony_boy = 'res/images/invalid_command/pony_boy.png'
    what_boy = 'res/images/invalid_command/what.png'
    shit_people = 'res/images/invalid_command/shit_on_people.png'

    images_list = [doge, pony_boy, what_boy, shit_people]

    attch_path = os.path.abspath(random.choice(images_list))
    taskobj.send_attachment(attch_path)


def get_sender_name(sender):
    temp = re.sub('\[.*\] ', '', sender)
    sender_name = temp[:temp.rindex(':')]
    return sender_name


def get_time_now_file():
    y = datetime.datetime.now()
    name = y.strftime("%Y%m%d-%H%M%S%f")
    return name


# Image Commands
def get_profile_image(taskobj, name):
    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@"+str(name))
    time.sleep(0.75)
    imagesouring = taskobj.driver.find_element_by_xpath('//*[@id="main"]/footer/div[4]')
    # print(imagesouring.get_attribute("innerHTML"))
    # printimagesouring.find_element_by_xpath(".//p[@class='test']").text
    if imagesouring.text == '':
        return False

    try:
        imageOfPer = imagesouring.find_element_by_tag_name("img")
        imageUrl = imageOfPer.get_attribute("src")
        print(imageUrl)
        taskobj.driver.execute_script("window.open('');")
        # Switch to the new window and open URL B
        taskobj.driver.switch_to.window(taskobj.driver.window_handles[1])
        taskobj.driver.get(imageUrl)
        time.sleep(2)
        profile_img = taskobj.driver.find_element_by_xpath("/html/body/img")
        file_name = get_time_now_file()+'.png'
        profile_img.screenshot("res/temp_data/profiles/"+file_name)
        taskobj.driver.close()
        taskobj.driver.switch_to.window(taskobj.driver.window_handles[0])
    except NoSuchElementException:
        file_name = "no_profile.png"

    box.send_keys(Keys.CONTROL+"a")
    box.send_keys(Keys.DELETE)

    return file_name


def check_if_valid_user(taskobj, username):
    memberlist = get_group_members_names(taskobj)

    for i in memberlist:
        if (username in i) or (i in username):
            return True
    return False


def pls_slap(taskobj, sender, command):
    taskobj.reply_to_new_messege()

    sender_name = get_sender_name(sender)
    txtsplit = re.search("@.*", command)
    beaten_name = txtsplit.group(0)[1:]
    print(sender_name, "slapped", beaten_name)

    # if not check_if_valid_user(taskobj, beaten_name) and ("sidebot" not in beaten_name.lower()):
    #     invalid_messege(taskobj)
    #     return


    sender_prof_file = get_profile_image(taskobj, sender_name)
    beaten_prof_file = None

    if "sidebot" in beaten_name.lower():
        beaten_prof_file = sender_prof_file
        beaten_name = sender_name
        sender_prof_file = "sidebot_profile.png"
    else:
        beaten_prof_file = get_profile_image(taskobj, beaten_name)


    if not beaten_prof_file:
        invalid_messege(taskobj)
        return

    # print(sender_prof_file)
    # print(beaten_prof_file)
    numbers_array = side_image_data.SlapData.numbers_array
    slap_types = side_image_data.SlapData.slap_types
    image_num = random.choice(numbers_array)
    img = Image.open(slap_types[image_num]['image_path'])

    img1 = Image.open("res/temp_data/profiles/"+sender_prof_file)
    img2 = Image.open("res/temp_data/profiles/"+beaten_prof_file)

    # profile_image_size
    ps = slap_types[image_num]['profile_hw']

    a = img1.resize((ps, ps))
    b = img2.resize((ps, ps))
    # (200,60)
    # (370,200)

    Image.Image.paste(img, a, slap_types[image_num]['slapper_loc'])
    Image.Image.paste(img, b, slap_types[image_num]['beater_loc'])
    # SLap Images Save
    slap_image = get_time_now_file()+'.png'
    slap_image_path = "res/temp_data/slaps/"+slap_image
    img.save(slap_image_path)
    attch_path = os.path.abspath(slap_image_path)

    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@"+beaten_name)
    box.send_keys(Keys.TAB)
    taskobj.send_attachment(attch_path)


def pls_help(taskobj, sender, command):
    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)

    box.send_keys("Side Bot :-)")
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    # box.send_keys("https://thechat.in/SideBOT")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("```Commands```")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot help* - HELP MENU")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot pls come here* - CHANGES GROUP and MAKES SideBOT ACTIVE (ISSUE FIXED)")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot status* - SHOWS SideBOT STATUS IN GROUP")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot tag everyone* - TAGS EVERYONE IN THE GROUP ;-)")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot whoisonline* - SHOWS WHO IS ONLINE^_^")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("```FUN Commands (UNDER DEV.)```")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot pls slap @TAG_USER* - SLAP COMMAND")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot congrats @TAG_USER* - CONGRATULATION COMMAND")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot wanted @TAG_USER* - WANTED COMMAND")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot danger @TAG_USER* - DANGER COMMAND")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*#sidebot jail @TAG_USER* - JAIL COMMAND")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("-----")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("*DISCLAIMER*: ```This BOT is not affiliated with nor endorsed by WhatsApp Inc.```")

    box.send_keys(Keys.SHIFT+Keys.ENTER)
    box.send_keys(Keys.SHIFT+Keys.ENTER)

    box.send_keys("@Rishu")

    box.send_keys(Keys.TAB)
    box.send_keys(Keys.ENTER)

    box.send_keys(Keys.ENTER)


def pls_congrats(taskobj, sender, command):
    taskobj.reply_to_new_messege()
    sender_name = get_sender_name(sender)
    txtsplit = re.search("@.*", command)
    beaten_name = txtsplit.group(0)[1:]
    print(sender_name, "congrats", beaten_name)

    # if not check_if_valid_user(taskobj, beaten_name) and ("sidebot" not in beaten_name.lower()):
    #     invalid_messege(taskobj)
    #     return

    winner_profile = None
    if "sidebot" in beaten_name.lower():
        winner_profile = "sidebot_profile.png"
    else:
        winner_profile = get_profile_image(taskobj, beaten_name)

    if not winner_profile:
        invalid_messege(taskobj)
        return

    numbers_array = side_image_data.CongratsData.numbers_array
    cong_types = side_image_data.CongratsData.cong_types
    image_num = random.choice(numbers_array)

    back = Image.open(cong_types[image_num]['image_path'])
    fore = Image.open("res/temp_data/profiles/" + winner_profile)

    trans_over = cong_types[image_num]['trans_over']

    attch_path = None

    if trans_over:
        jil = back.resize(fore.size)
        fore.paste(jil, (0, 0), jil)
        slap_image = get_time_now_file() + '.png'
        slap_image_path = "res/temp_data/congrats/" + slap_image
        fore.save(slap_image_path)
        attch_path = os.path.abspath(slap_image_path)

        pass
    else:
        ps = cong_types[image_num]['profile_hw']
        fore = fore.resize((ps, ps))
        Image.Image.paste(back, fore, cong_types[image_num]['congrats_loc'])
        slap_image = get_time_now_file() + '.png'
        slap_image_path = "res/temp_data/congrats/" + slap_image
        back.save(slap_image_path)
        attch_path = os.path.abspath(slap_image_path)
        pass

    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@" + beaten_name)
    box.send_keys(Keys.TAB)
    taskobj.send_attachment(attch_path)


def make_wanted(taskobj, sender, command):
    taskobj.reply_to_new_messege()
    sender_name = get_sender_name(sender)
    txtsplit = re.search("@.*", command)
    wanted_user = txtsplit.group(0)[1:]
    print(sender_name, "wanted", wanted_user)

    # if not check_if_valid_user(taskobj, wanted_user) and ("sidebot" not in wanted_user.lower()):
    #     invalid_messege(taskobj)
    #     return

    wanted_profile = None
    if "sidebot" in wanted_user.lower():
        wanted_profile = "sidebot_profile.png"
    else:
        wanted_profile = get_profile_image(taskobj, wanted_user)


    if not wanted_profile:
        invalid_messege(taskobj)
        return

    numbers_array = side_image_data.WantedData.numbers_array
    want_types = side_image_data.WantedData.want_types
    image_num = random.choice(numbers_array)

    back = Image.open(want_types[image_num]['image_path'])
    fore = Image.open("res/temp_data/profiles/" + wanted_profile)

    attch_path = None

    ps = want_types[image_num]['profile_hw']
    fore = fore.resize((ps, ps))
    Image.Image.paste(back, fore, want_types[image_num]['congrats_loc'])
    slap_image = get_time_now_file() + '.png'
    slap_image_path = "res/temp_data/wanted/" + slap_image
    back.save(slap_image_path)
    attch_path = os.path.abspath(slap_image_path)

    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@" + wanted_user)
    box.send_keys(Keys.TAB)
    taskobj.send_attachment(attch_path)


def in_danger(taskobj, sender, command):
    taskobj.reply_to_new_messege()
    sender_name = get_sender_name(sender)
    txtsplit = re.search("@.*", command)
    danger_user = txtsplit.group(0)[1:]
    print(sender_name, "dangered", danger_user)

    # if not check_if_valid_user(taskobj, danger_user) and ("sidebot" not in danger_user.lower()):
    #     invalid_messege(taskobj)
    #     return

    danger_profile = None
    if "sidebot" in danger_user.lower():
        danger_profile = "sidebot_profile.png"
    else:
        danger_profile = get_profile_image(taskobj, danger_user)


    if not danger_profile:
        invalid_messege(taskobj)
        return


    numbers_array = side_image_data.DangerData.numbers_array
    dangr_types = side_image_data.DangerData.dang_types
    image_num = random.choice(numbers_array)

    back = Image.open(dangr_types[image_num]['image_path'])
    fore = Image.open("res/temp_data/profiles/" + danger_profile)

    attch_path = None

    ps = dangr_types[image_num]['profile_hw']
    fore = fore.resize((ps, ps))
    Image.Image.paste(back, fore, dangr_types[image_num]['danger_loc'])
    slap_image = get_time_now_file() + '.png'
    slap_image_path = "res/temp_data/danger/" + slap_image
    back.save(slap_image_path)
    attch_path = os.path.abspath(slap_image_path)

    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@" + danger_user)
    box.send_keys(Keys.TAB)
    taskobj.send_attachment(attch_path)


def in_jail(taskobj, sender, command):
    taskobj.reply_to_new_messege()
    sender_name = get_sender_name(sender)
    txtsplit = re.search("@.*", command)
    jail_user = txtsplit.group(0)[1:]
    print(sender_name, "jailed", jail_user)

    # if not check_if_valid_user(taskobj, jail_user) and ("sidebot" not in jail_user.lower()):
    #     invalid_messege(taskobj)
    #     return

    jailed_profile = None
    if "sidebot" in jail_user.lower():
        jailed_profile = "sidebot_profile.png"
    else:
        jailed_profile = get_profile_image(taskobj, jail_user)

    if not jailed_profile:
        invalid_messege(taskobj)
        return


    numbers_array = side_image_data.JailData.numbers_array
    cong_types = side_image_data.JailData.jail_types
    image_num = random.choice(numbers_array)

    back = Image.open(cong_types[image_num]['image_path'])
    fore = Image.open("res/temp_data/profiles/" + jailed_profile)

    jil = back.resize(fore.size)
    img = ImageOps.grayscale(fore)
    img.paste(jil, (0, 0), jil)
    slap_image = get_time_now_file() + '.png'
    slap_image_path = "res/temp_data/jailed/" + slap_image
    img.save(slap_image_path)
    attch_path = os.path.abspath(slap_image_path)

    box = taskobj.driver.find_element_by_xpath(xpaths.chat_box_input)
    box.send_keys("@" + jail_user)
    box.send_keys(Keys.TAB)
    taskobj.send_attachment(attch_path)
