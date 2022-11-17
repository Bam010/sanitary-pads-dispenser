import requests

# from airtable
base_id = "appTlv32dv1GIHn3z"
url_transaction = "https://api.airtable.com/v0/" + base_id + "/" + "Picking"
url_user = "https://api.airtable.com/v0/" + base_id + "/" + "user"
url_countLoc = "https://api.airtable.com/v0/" + base_id + "/" + "countLoc"
url_product = "https://api.airtable.com/v0/" + base_id + "/" + "product"

api_key = "key8YMPs0IVcwKxCe"
headers = {'Authorization': 'Bearer ' + api_key}

def get_record(url):
    params = ()
    airtable_records = []
    run = True
    while run is True:
        response = requests.get(url, params=params, headers=headers)
        airtable_response = response.json()
        airtable_records += (airtable_response['records'])

        if 'offset' in airtable_response:
            run = True
            params = (('offset', airtable_response['offset']),)
        else:
            run = False

    return [value['fields'] for value in airtable_records]

transaction = get_record(url_transaction)
user = get_record(url_user)
countLoc = get_record(url_countLoc)
product = get_record(url_product)