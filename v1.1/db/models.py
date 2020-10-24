from configs import db

# 下方定义模型类  chats table
class Chat(db.Model):
    __tablename__ = 'chats'

    _id = db.Column(db.String(512), primary_key=True)
    time = db.Column(db.String(512))
    userid = db.Column(db.String(512))
    ip = db.Column(db.String(512))
    # is_real = db.Column(db.Boolean)
    text = db.Column(db.String(1024))

    def __repr__(self):
        return '<Chats %s>' % self._id

if __name__ == '__main__':
    db.create_all()