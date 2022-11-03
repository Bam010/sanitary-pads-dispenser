from flask import Flask, render_template, request
from jinja2 import TemplateNotFound
from flask import Blueprint
import os

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)

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


app.register_blueprint(blueprint)
