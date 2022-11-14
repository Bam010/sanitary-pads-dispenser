from flask import Flask, render_template, request
from jinja2 import TemplateNotFound
from flask import Blueprint
import os

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


# start of Flask
blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)

@blueprint.route('/')
def defualt():

    return render_template('home/index.html', segment='index')

@blueprint.route('/index')
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
app = Flask(__name__)
app.config.ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
app.config.db = {'trans': transaction,
                'user': user,
                'loc': countLoc,
                'prod': product}


app.register_blueprint(blueprint)