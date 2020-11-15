from app import app
from flask import render_template
from .projects import SiteData


@app.route('/', methods=['GET', 'POST'])
def index():
    content = {
        'title': 'vnkrtv',
        'projects': SiteData.projects,
        'carousel_images': SiteData.carousel_images
    }
    return render_template('index.html', **content)
