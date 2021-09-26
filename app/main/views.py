from flask import render_template
from . import main
from request import pickquote


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    data=pickquote()

    return render_template('index.html', data=data)


@main.route('/quote/<quote_id>')
def movie(quote_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('quote.html',id = quote_id)    