from flask_login.mixins import UserMixin
from app.main.forms import CommentsForm
from flask import  render_template,url_for,redirect,abort
from .. import db
from . import main
from flask_login import login_user,logout_user,login_required,current_user
from request import pickquote,pickquote2,pickquote1
from ..models import User,Comment
from .forms import UpdateProfile,UpvoteForm,CommentsForm

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

@main.route('/admin')  
@login_required
def admin():
  
  return render_template(admin.site.register)


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

@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(post_id=id, comment=comment.form.data, author=current_user)
        new_comment.save_comment()

    return render_template('main/comment.html', comment_form=comment_form)     