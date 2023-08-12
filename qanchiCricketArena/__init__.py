from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from qanchiCricketArena.config import Config


#extension Initialization
mail=Mail()
db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()

login_manager.login_view='usersB.loginPageFunc'
login_manager.login_message_category='info'






def createApp(configClass=Config):
    #app creation
    app = Flask(__name__)
    app.config.from_object(Config)

    #extension
    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    #BluePrints
    from qanchiCricketArena.users.routes import usersB
    from qanchiCricketArena.posts.routes import postsB
    from qanchiCricketArena.main.routes import mainB
    from qanchiCricketArena.booking.routes import bookingB


    app.register_blueprint(usersB)
    app.register_blueprint(postsB)
    app.register_blueprint(mainB)
    app.register_blueprint(bookingB)

    return app