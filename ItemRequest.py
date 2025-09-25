import json

import requests
from Item import *


def create_item_object(id, itemName, img):
    return Item(id=id, name=itemName, img=img)

#Barcode placeholder
barcode_id = 7039010132435
barcodeTranslateWebsite = 'https://world.openfoodfacts.org/api/v0/product/{}.json'.format(barcode_id)


try:
    # Response item
    r = requests.get(barcodeTranslateWebsite)
    r.raise_for_status()
    itemData = r.json()

    if itemData["status"] == 0:
        print("Item not found")
    else:
        # Pretty print of json
        # print(json.dumps(itemData, indent=2, ensure_ascii=False))

        item = create_item_object(itemData["product"]["id"], itemData["product"]["product_name"], itemData["product"]["image_front_url"])
        print(item)


except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")












