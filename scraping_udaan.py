import time
import json
import os
from random import randint
from tqdm import tqdm
import requests
import logging

def print_requests(enable: bool) -> None:
    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.

    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def pretty_print_curl(curl_req: str) -> None:
    """
    Print Curl request in a readable fashion
    :param curl_req: The complete curl request
    :return: None
    """

    print(curl_req.replace('-H', '\n-H'))


def get_headers_from_curl(curl_req: str) -> dict:
    """
    Extracts the headers from a curl request
    :param curl_req: The complete curl request
    :return: A dictionary of headers, which can directly be passed to requests call
    """

    curl_req = curl_req.replace('--compressed', '')
    list_of_header_infos = curl_req.split('-H')[1:]

    header_dict = {}
    for single_header in list_of_header_infos:
        header_dict[single_header.split(':')[0].strip(' \'')] = ''.join(single_header.split(':')[1:]).strip('\' ')

    return header_dict


def dump_list_json_file(obj: list, file_path: str) -> None:
    """
    Dump the passed obj to the path as json
    :param obj: The object to serialize
    :param file_path: The path where to dump the obj
    :return: None
    """
    if not os.path.exists(''.join(file_path.split('/')[:-1])):
        os.makedirs(''.join(file_path.split('/')[:-1]))

    with open(file_path, 'w') as fp:
        json.dump(obj, fp, indent=2)


search_url = 'https://udaan.com/api/search/v1?q=Prachi%20Creation{}'
login_verify = 'https://udaan.com/api/session/v1'
listings_url = 'https://udaan.com/api/listings/v1/{}'

# curl_request = "curl 'https://udaan.com/api/listings/v1/TLCKRFTMFRD9PBVCRNZPNB55DWPFJ55' -H 'authorization: Bearer eyJraWQiOiI2TW53IiwidHlwIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJhdWQiOiJodHRwczovL2FwaS51ZGFhbi5jb20vIiwic3ViIjoiVVNSRkg2MjlaQkRHRkQyU1pRNk1KQ1BXN1E5OTMiLCJyIjpbInVzZXIiXSwibmJmIjoxNTYwNDA4ODI2LCJpc3MiOiJhdXRoLnVkYWFuLmNvbSIsImV4cCI6MTU2MDQwOTQyNiwibyI6Ik9SRzdXR0tXV0ZIUzBDWEc0VFcySlFLUEM2MUZUIn0.aT1dz1QHfG4N8VkTy6eSJ7F9U3fq7MprDsIe4jywW0JA0TwWnnJfWV0VvcTUKZLKglSchVtSisEO7l3twP8-pA' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36' -H 'accept: */*' -H 'referer: https://udaan.com/listing/TLCKRFTMFRD9PBVCRNZPNB55DWPFJ55' -H 'authority: udaan.com' -H 'cookie: __cfduid=da21246a8d27f5c6b8063e92d7f0357281560162971; ai_user=qPZwl|2019-06-10T10:36:18.730Z; _csrf=OkavUqwOIutPpbGchi70hMoo; rt.0=3y071s44TIwBACAWQgitG2%2Fg6b07QIa%2Bj3%2Ba5X7sDPuTOIy4BGsWJtorAb1thngAb5ylOUyMMrvaZTBaN10pf23R7gSsQux6En5%2BrjO7b0%2Fg9usbG10WzBP0oQ9K3TeMCQwNsAHCyvvfpYk3lJ1yekja%2BXDjk32SsdtlDZg7dYHKxbEpN1tkMzIyYjExYQ%3D%3D; mp_a67dbaed1119f2fb093820c9a14a2bcc_mixpanel=%7B%22distinct_id%22%3A%20%22USRFH629ZBDGFD2SZQ6MJCPW7Q993%22%2C%22%24device_id%22%3A%20%2216b40f5cb23bc-013c87f857bb9-1b29140e-100200-16b40f5cb24a0e%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%2C%22%24user_id%22%3A%20%22USRFH629ZBDGFD2SZQ6MJCPW7Q993%22%7D; ai_session=QRJZ9|1560406957799|1560408087427.77; at.0=t%3DeyJraWQiOiI2TW53IiwidHlwIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJhdWQiOiJodHRwczovL2FwaS51ZGFhbi5jb20vIiwic3ViIjoiVVNSRkg2MjlaQkRHRkQyU1pRNk1KQ1BXN1E5OTMiLCJyIjpbInVzZXIiXSwibmJmIjoxNTYwNDA4NjQwLCJpc3MiOiJhdXRoLnVkYWFuLmNvbSIsImV4cCI6MTU2MDQwOTI0MCwibyI6Ik9SRzdXR0tXV0ZIUzBDWEc0VFcySlFLUEM2MUZUIn0._min-WGweueVpqi62iuwXv_hCf9o2HiDNwx4VGcYw4OGs0wE_V1ijG5i9OMYG4LSwv2exXevV9ueDYx_g6OYsQ%3Ba%3D600%3Be%3D1560409240' --compressed"
curl_request = input('Enter curl data global level: ').strip()
# pretty_print_curl(curl_request)

def scrape_udaan_supplier_level():
    all_collection = []

    # get the total number of listings

    beginning_of_req = False

    if beginning_of_req:

        res = requests.get(search_url.format(''), headers=get_headers_from_curl(curl_request))

        if res.status_code == 200:
            all_collection.append(res.text)
            print('Got First Req')
            time.sleep(15)

        num_found = res.json()['numFound']

    else:
        num_found = 703

    # In udaan, every single fetch gets 12 products
    for query_num in range(516, num_found, 12):
        res = requests.get(search_url.format(f'&start={query_num}'), headers=get_headers_from_curl(curl_request))
        if res.status_code == 200 and len(res.text) > 1000:
            all_collection.append(res.text)
            print(query_num)
            time.sleep(randint(10, 25))

            if query_num % 24 == 0:
                dump_list_json_file(all_collection, 'prachi-collection/listings_516.json')
                print('dump created')

        else:
            print(query_num, 'Exiting')
            break

def get_listing(listing_id: str, curl_request:str) -> str:
    """
    Given a listing id it returns the specific listing from udaan
    :param listing_id: The listing id to query on
    :return: res.text: str
    """

    res = requests.get(listings_url.format(listing_id), headers=get_headers_from_curl(curl_request))
    if res.status_code == 200 and len(res.text) > 1000:
        return res.text
    else:
        return 'get curl data'



# For listings inside a json obj scrape the data
def scrape_udaan_catalogue_level(curl_request):
    start_time = time.time()

    with open('prachi-collection/listings_516.json', 'r') as fp:
        catalogues = json.load(fp)

    count = 42
    for catalogue_id, catalogue in enumerate(catalogues):
        listings_list = []
        print("catalogue_id", catalogue_id)
        print("Elapsed time is ", time.time() - start_time, time.time() - start_time > 400)

        for listing in json.loads(catalogue)['listings']:
            res_list = get_listing(listing['listingId'], curl_request)

            # If 8 mins have passed ask for new curl info
            if res_list == 'get curl data' or time.time() - start_time > 400:
                curl_request = input('Enter Curl Data: ').strip()
                start_time = time.time()

            else:
                listings_list.append(get_listing(listing['listingId'], curl_request))
                time.sleep(randint(8, 15))

        count = count + 1
        dump_list_json_file(listings_list, f'prachi-collection/individual_{count}.json')


# scrape_udaan_catalogue_level(curl_request)


def scrape_udaan_fab_data(curl_request):
    with open('fab_scrape.json') as fp:
        fab_data = json.load(fp)

    start_time = time.time()
    print("Total length to scrape is: ", len(fab_data))

    count = 0
    for index, data in enumerate(fab_data):
        listings_list = []

        print(index)
        print("Time Elapsed is: ", time.time() - start_time)

        for listing in data['listings']:
            res_list = get_listing(listing['listingId'], curl_request)

            if res_list == 'get curl data' or time.time() - start_time > 400:
                curl_request = input('Enter Curl Data: ').strip()
                start_time = time.time()

            else:
                listings_list.append(get_listing(listing['listingId'], curl_request))
                time.sleep(randint(8, 15))

        count += 1
        dump_list_json_file(listings_list, f'fabfirki/individual_{count}.json')

scrape_udaan_fab_data(curl_request)