import time
from collections import defaultdict

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/home/zoomtail/PycharmProjects/web_crawler/chromedriver'

def save_html(html_content, path):
    with open(path, 'w') as fp:
        fp.write(html_content)


def read_html(path) -> str:
    with open(path, 'r') as fp:
        return fp.read()


if 1:
    user_message_mapping = defaultdict(list)

    # if 'messages' not in os.listdir('.'):

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get('https://www.facebook.com')

    driver.find_element_by_css_selector('#email').send_keys('fb.test.zoomtail@gmail.com')
    driver.find_element_by_css_selector('#pass').send_keys('qwer12192')
    driver.find_element_by_class_name('uiButton.uiButtonConfirm').click()

    time.sleep(5)


def reply_to_chat():
    try:
        print('Trying to reply to messages')

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # For all current chats find the active one and find its id
        for sel in soup.select(".fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent"):
            if sel.select_one('._4jeh').text.strip() == 'Active now':
                active_id = sel.select_one('._mh6')['id']


        # Reply to the text box that is active
        text_box = driver.find_element_by_css_selector(
            f".fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent #{active_id} ._5rpu")

        text_box.send_keys('The bot is replying')
        text_box.send_keys(Keys.ENTER)

        # click on the close button to close after replying
        driver.find_element_by_class_name('close').click()

    except Exception as e:
        print(e)


while True:
    try:
        driver.find_element_by_class_name('_5yl5')
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # This needs to be tested for multiple users
        user_name = soup.select_one('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._1ogo').text
        user_messages = [mess.text for mess in soup.select('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._5yl5')][-5:]

        # print('Complete user messages', user_messages)

        user_names = [name for name in soup.select_one('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._1ogo')]

        # print('Mapping', user_message_mapping)

        for user_name in user_names:
            if len(user_message_mapping[user_name]):
                if user_message_mapping[user_name][-1] == user_messages[-1]:
                    # Wait a second before next query
                    time.sleep(1)

                else:
                    print('Inserting new messages')

                    try:
                        message_index = user_messages.index(user_message_mapping[user_name][-1]) + 1
                        print(f'Inserting {len(user_messages) - message_index} messages')
                        user_message_mapping[user_name].extend(user_messages[message_index:])

                    except Exception as e:
                        print(e)

                    # Auto-Reply to messages
                    reply_to_chat()

            else:
                print('Inserting first messages')

                user_message_mapping[user_name].extend(user_messages)
                reply_to_chat()

            save_html(driver.page_source, 'messages')

    except NoSuchElementException as no:
        time.sleep(5)
        print(no)

# driver.quit()

# use BeautifulSoup to find out info about the page
# soup = BeautifulSoup(read_html('messages'), 'html.parser')
# print([message.text for message in soup.select('._5yl5')])


# print('The complete message box')
# print(soup.select_one(".fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._4jeh").text)
# print(soup.select_one("//div[@class='_1ia']/descendant::div[@class='_5rpu' and @role='combobox']").prettify())

# Name of the person
# print(soup.select_one('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._1ogo').text)

# All messages
# print([mess.text for mess in soup.select('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._5yl5')])


# print(soup.select_one('.fbNubFlyout.fbDockChatTabFlyout.uiContextualLayerParent ._1mf._1mj').prettify())
