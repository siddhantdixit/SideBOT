# Welcome Screen

welcome_screen = '//h1[contains(string(),"Keep your")]'

# Search Box

search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'

# Chat Box Text Field

chat_box_input = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'

# Attachment Buttons
attachment_btn = '//div[@title = "Attach"]'

attachment_img = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'

attachment_send = '//span[@data-icon="send"]'


# Last Chat DIV (SideBar)

last_div_side = '//div[contains(@aria-label,"Chat list")]/div[contains(@style,"translateY(0px)")]'


# Status Update

about_div = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4]'

pencil_btn = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4] //div[contains(@title,"Edit")]'

about_status_text = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4] //div[contains(@contenteditable,"true")]'

tick_btn = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4] //div[contains(@title,"Click to save")]'


# Current Group

group_member_list = '//*[@id="main"]/header/div[2]/div[2]/span'

last_sender_in = '//div[contains(@role,"region")] //div[contains(@class,"message-in")][last()] //div[contains(@data-pre-plain-text,"[")]'

last_messege_in = '//div[contains(@role,"region")] //div[contains(@class,"message-in")] [last()] //span[contains(@class,"copyable-text") and (@dir)]'

last_messege_in_div = '//div[contains(@role,"region")] //div[contains(@class,"message-in")][last()]'
