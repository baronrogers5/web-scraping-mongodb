import json
import os

count_of_listings = 0
list_of_listings = []

for file in [files for files in os.listdir('prachi-collection') if 'individual_' in files]:

    with open('prachi-collection/' + file) as fp:
        listings = json.load(fp)
        for listing in listings:
            single_listing = json.loads(listing)
            # print(single_listing['listingId'])
            count_of_listings += 1
            list_of_listings.append(single_listing['listingId'])


print("Total listings are", count_of_listings)
print("Unique listing count is", len(set(list_of_listings)))

