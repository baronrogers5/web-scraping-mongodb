import os
from pprint import pprint
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

# For IndiaMart search
base_url = 'https://dir.indiamart.com/search.mp?ss={}&prdsrc=1'

def save_html(html_content, path):
    with open(path, 'wb') as fp:
        fp.write(html_content)


def read_html(path) -> bytes:
    with open(path, 'rb') as fp:
        return fp.read()


file_names = ['Arihant Nx', 'Bandidhari Fashion']

file_names = [name.replace(' ', '+') for name in file_names]

prod_catalog = defaultdict(lambda: defaultdict(list))

for file_name in file_names:
    if file_name not in os.listdir('.'):
        res = requests.get(base_url.format(file_name))
        save_html(res.content, file_name)
        html = res.content
        print('Sent a request')

    else:
        html = read_html(file_name)
        print('Fetched from local')

    soup = BeautifulSoup(html, 'html.parser')
    all_prod_info = soup.select('.l-cl.b-w')


    for prod in all_prod_info:


        try:
            # Get prod name
            prod_catalog[file_name]['prod_name'].append(prod.select_one('.lg').text.strip())
        except:
            continue

        try:
            prod_info = prod.select_one('.prd-img')
            # Get image link
            prod_catalog[file_name]['image_link'].append('https:' + prod_info.select_one('img')['data-limg'])
        except:
            prod_catalog[file_name]['image_link'].append('')


        try:
            prod_catalog[file_name]['prod_url'].append(prod.select_one('.cur')['href'])
        except:
            prod_catalog[file_name]['prod_url'].append('')

        try:
            # Prod price needs to pass via a function that removes the non-req items and
            # converts it to an int
            prod_catalog[file_name]['prod_price'].append(prod.select_one('.prc.cur').text.split(' ')[0].replace(' ', ''))
        except:
            prod_catalog[file_name]['prod_price'].append('')

        try:
            prod_catalog[file_name]['extra_prod_info'].append([info.text for info in prod.select('.desc.des_p p')])
        except:
            prod_catalog[file_name]['extra_prod_info'].append([])


# print(f"Saved prods are {len(prod_catalog)} in number")
pprint(prod_catalog)