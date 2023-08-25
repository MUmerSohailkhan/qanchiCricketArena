from flask import render_template,request,Blueprint
from qanchiCricketArena.models import post
from qanchiCricketArena import db
mainB=Blueprint('mainB',__name__)


@mainB.route("/")
@mainB.route("/home")
def homePageFunc():
    page=request.args.get('page',1,type=int)
    posts=post.query.order_by(post.datePosted.desc()).paginate(page=page,per_page=7)

    return render_template('home.html',posts=posts)


@mainB.route("/QSAHome")
def QSAHome():
    return render_template('QSAHome.html')



@mainB.route("/about")
def aboutPageFunc():
    return render_template('about.html',title='About')

@mainB.route('/create_db_and_upload_folder')
def create_db():
    # Create db
    db.create_all()
    # Create the "upload" folder if it doesn't exist

    return 'Database and upload folder created successfully!'

