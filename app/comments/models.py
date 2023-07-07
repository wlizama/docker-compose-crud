from database import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
