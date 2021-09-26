from flask import render_template
from . import main
from flask_login import login_user,logout_user,login_required
from request import pickquote,pickquote2,pickquote1


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    data=pickquote()
    data1=pickquote1()
    data2=pickquote2()

    return render_template('index.html', data=data,data1=data1,data2=data2)


@main.route('/quote/<quote_id>')
def movie(quote_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('quote.html',id = quote_id)    