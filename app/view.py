
from flask import Flask, render_template
from app import app 
from flask_bootstrap import Bootstrap
from .defaults import data

bootstrap = Bootstrap(app)

default_data2 = {
    'site_title' : 'Responsive Resume/CV Template for Developers',
    'name' : 'Marine Howard',
    'tagline' : 'Full Stack Developer',
    'email' : 'alan.doe@website.com',
    'phone' : '0123 456 789',
    'website' : 'portfoliosite.com',
    'linkedin' : 'linkedin.com/in/alandoe',
    'github' : 'github.com/username',
    'twitter' : '@twittername',

    }


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',  bootstrap=bootstrap, **data)