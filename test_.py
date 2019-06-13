# Figure out the token thingy from udaan

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


pretty_print_curl("curl 'https://udaan.com/auth/token' -X POST -H 'origin: https://udaan.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36' -H 'accept: */*' -H 'referer: https://udaan.com/search?q=Prachi%20Creation' -H 'authority: udaan.com' -H 'cookie: __cfduid=da21246a8d27f5c6b8063e92d7f0357281560162971; ai_user=qPZwl|2019-06-10T10:36:18.730Z; _csrf=OkavUqwOIutPpbGchi70hMoo; rt.0=3y071s44TIwBACAWQgitG2%2Fg6b07QIa%2Bj3%2Ba5X7sDPuTOIy4BGsWJtorAb1thngAb5ylOUyMMrvaZTBaN10pf23R7gSsQux6En5%2BrjO7b0%2Fg9usbG10WzBP0oQ9K3TeMCQwNsAHCyvvfpYk3lJ1yekja%2BXDjk32SsdtlDZg7dYHKxbEpN1tkMzIyYjExYQ%3D%3D; at.0=t%3DeyJraWQiOiI2TW53IiwidHlwIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJhdWQiOiJodHRwczovL2FwaS51ZGFhbi5jb20vIiwic3ViIjoiVVNSRkg2MjlaQkRHRkQyU1pRNk1KQ1BXN1E5OTMiLCJyIjpbInVzZXIiXSwibmJmIjoxNTYwNDIyNzgxLCJpc3MiOiJhdXRoLnVkYWFuLmNvbSIsImV4cCI6MTU2MDQyMzM4MSwibyI6Ik9SRzdXR0tXV0ZIUzBDWEc0VFcySlFLUEM2MUZUIn0.vaWwKdQsMG1YQlDUtPHmjnBj_RyLbrJ7AGJNoffGkogGWwWadgvb-hykbmy6Bf01qkjv6mOXJh9d8NOdo2kMLg%3Ba%3D600%3Be%3D1560423381; mp_a67dbaed1119f2fb093820c9a14a2bcc_mixpanel=%7B%22distinct_id%22%3A%20%22USRFH629ZBDGFD2SZQ6MJCPW7Q993%22%2C%22%24device_id%22%3A%20%2216b40f5cb23bc-013c87f857bb9-1b29140e-100200-16b40f5cb24a0e%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.in%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.in%22%2C%22%24user_id%22%3A%20%22USRFH629ZBDGFD2SZQ6MJCPW7Q993%22%7D; ai_session=go8mH|1560422118022|1560423219889.25' -H 'content-length: 0' --compressed")