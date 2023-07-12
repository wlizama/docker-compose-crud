from database import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Relationship to posts
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'user': self.user.to_dict()
        }

    def __repr__(self):
        return f"<Post(title='{self.title}')>"