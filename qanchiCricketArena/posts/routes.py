from flask import Blueprint
from flask import render_template,url_for,flash,redirect,request,abort
from qanchiCricketArena.models import user,post
from qanchiCricketArena.posts.forms import postForm
from qanchiCricketArena import db
from flask_login import current_user,login_required



postsB=Blueprint('postsB',__name__)


@postsB.route("/post/new",methods=['POST','GET'])
@login_required
def newPostPageFunc():
    form=postForm()
    if form.validate_on_submit():
        post1=post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post1)
        db.session.commit()
        flash("your post has been created",'succcess')
        return redirect(url_for('mainB.homePageFunc'))
    return render_template('newPost.html',title='Post',legend='New Post',form=form)



@postsB.route("/post/<int:post_id>",methods=['POST','GET'])
@login_required
def postPageFunc(post_id):
    post1=post.query.get_or_404(post_id)
    return render_template('post.html',title=post1.title,post=post1)

@postsB.route("/post/<int:post_id>/update",methods=['POST','GET'])
@login_required
def updatePostPageFunc(post_id):
    post1=post.query.get_or_404(post_id)
    if post1.author!=current_user:
        abort(403)
    form=postForm()
    if form.validate_on_submit():
        post1.title=form.title.data
        post1.content=form.content.data
        db.session.commit()
        flash("Your post has been updated",'success')
        return redirect(url_for('postsB.postPageFunc',post_id=post1.id))
    elif request.method=='GET':
        form.title.data=post1.title
        form.content.data=post1.content
    return render_template('newPost.html',title='Update Post',legend='Update Post',form=form)


@postsB.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def deletePostPageFunc(post_id):
    post1 = post.query.get_or_404(post_id)
    if post1.author != current_user:
        abort(403)
    db.session.delete(post1)
    db.session.commit()
    flash("Your post has been deleted",'success')
    return redirect(url_for('mainB.homePageFunc'))



@postsB.route("/user/<string:username>")
@login_required
def userPostFunc(username):
    page=request.args.get('page',1,type=int)
    user1=user.query.filter_by(username=username).first_or_404()
    posts=post.query.filter_by(author=user1).order_by(post.datePosted.desc()).paginate(page=page,per_page=5)
    return render_template ('userPost.html',posts=posts,user=user1)

