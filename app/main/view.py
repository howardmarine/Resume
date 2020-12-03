from . import main
from flask import render_template

default_data = {
    'site_title' : 'Responsive Resume/CV Template for Developers',
    'name' : 'Alan Doe',
    'tagline' : 'Full Stack Developer',
    'email' : 'alan.doe@website.com',
    'phone' : '0123 456 789',
    'website' : 'portfoliosite.com',
    'linkedin' : 'linkedin.com/in/alandoe',
    'github' : 'github.com/username',
    'twitter' : '@twittername',

    }


@main.route('/')
def index():
    return render_template('index.html', data=default_data)