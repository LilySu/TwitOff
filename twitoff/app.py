#configuring and routing
import os
from pickle import loads, dumps
from decouple import config
from flask import Flask, render_template, request
from models import DB, User
from twitter import add_or_update_user, add_users
from predict2 import predict_user

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template("base.html", title='Home', users=users)

    @app.route('/user', methods=['POST'])#route for users
    #you can decorate a route multiple times, if someone makes a POST request, trigger this
    #if someone does a GET request to user/
    #decorating twice is allowed. Add users - post, get users get request
    #GET request needs parameters, where POST doesn't
    #To add users, we will use a form
    #decorators are functions that take functions and returns functions
    @app.route('/user/<name>', methods=['GET'])
    #name needs a default value because it might not exist
    def user(name=None, message=''):
        # import pdb; pdb.set_trace() #imports python debugger
        name = name or request.values['user_name']
        try:
            if request.method == "POST":
                #we want to add a user if the request method is POST
                add_or_update_user(name)#method lives in twitter
                #not destructive if called multiple times
                message = "User {} successfully added!".format(name)
                #whether or not we get the user, we get their tweets
            tweets = User.query.filter(User.name == name).one().tweets
            #query based on username, get their first user, return tweets
            #"one" will raise an exeception if it doesn't find the user, first will return the first users only.
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            tweets = []#make sure tweet is an empty list
        return render_template("user.html", title=name, tweets=tweets, message=message)
        #we want to display the name, tweet and message.

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1, user2 = sorted([request.values['user1'],
                               request.values['user2']])
        if user1 == user2:
            message = 'Cannot compare a user to themselves!'
        else:
            prediction = predict_user(user1, user2,
                                      request.values['tweet_text'])
        message = '"{}" is more likely to be said by {} than {}'.format(
            request.values['tweet_text'], user1 if prediction else user2,
            user2 if prediction else user1)
        return render_template('prediction.html', title='Prediction', message=message)
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        add_users()
        return render_template('base.html', title='Reset database!', users=[])

    return app
