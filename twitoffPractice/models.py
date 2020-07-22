from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    """Twitter users."""
    id = db.Column(db.BigInterger, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    # Tweet IDs are ordinal interger, so can be use to only fetch the most recent
    newest_tweet_id = db.Column(db.BigInterger)

    def __repr__(self):
        return '[User {}]'.format(self.name)


class Tweet(db.Model):
    """Tweets and their embedding from Basilica."""
    id = db.Column(db.BigInterger, primary_key=True)
    text = db.Column(db.Unicode(300))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.BigInterger, db.ForignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))
    
    def __repr__(self):
        return '[Tweet {}]'.format(self.text)
