import requests
import os

from bs4 import BeautifulSoup

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

def save_html(html_content, path):
    with open(path, 'wb') as fp:
        fp.write(html_content)

def read_html(path) -> bytes:
    with open(path, 'rb') as fp:
        return fp.read()


if 'media_ratings' not in os.listdir('.'):
    res = requests.get(url)
    save_html(res.content, 'media_ratings')
    html = res.content
    print('Sent a request')

else:
    html = read_html('media_ratings')
    print('Fetched from local')

soup = BeautifulSoup(html, 'html.parser')

rows = soup.select('tbody tr')
# print(rows[0].prettify())

# News Source
for row in rows[:1]:
    # we can also use only .source-title as views-field does not add any extra info
    news_info = row.select_one('.views-field.source-title a')

    news_source = news_info['href']
    news_name = news_info.text.strip()

    allslides_news_link = 'https://www.allslides.com' + news_source
    print(news_name, allslides_news_link)

# Bias Rating
row = rows[0]
bias_info = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
print(bias_info)

# Community Feedback data
community_data_agree = row.select_one('.agree').text
community_data_disagree = row.select_one('.disagree').text

print(community_data_agree, community_data_disagree)