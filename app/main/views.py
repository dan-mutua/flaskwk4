from flask_login.mixins import UserMixin
from app.main.forms import CommentsForm
from flask import render_template,url_for,redirect
from .. import db
from . import main
from flask_login import login_user,logout_user,login_required
from request import pickquote,pickquote2,pickquote1
from ..models import User


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

@main.route('/table')
@login_required
def table():
    users=User.query.all()
    return render_template('table.html',users=users)



@main.route('/quote/<quote_id>')
def mquote(quote_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('quote.html',id = quote_id)    

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)    