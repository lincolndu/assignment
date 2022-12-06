mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
if(mobile_data['status']):
    i = 0
    while i < len(mobile_data['data']):
        price = float(mobile_data['data'][i]['price'].split(' ')[0]) * mobile_data['exchnage_rate']
        print(f'{mobile_data["data"][i]["name"]} mobile made in {mobile_data["data"][i]["made"]}. This phone price is {mobile_data["data"][i]["price"]} and {price} taka for Bangladesh')
        i += 1
else:
    j = 0
    while j < len(mobile_data['data']):
        price = float(mobile_data['data'][j]['price'].split(' ')[0]) * mobile_data['exchnage_rate']
        print(f'{mobile_data["data"][j]["name"]} is made in {mobile_data["data"][j]["made"]}. The price is {mobile_data["data"][j]["price"]} which is almost equal to {price} BDT')
        j += 1 