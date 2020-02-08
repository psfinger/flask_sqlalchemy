from db import db, User

if __name__ == '__main__':
    db.create_all()
    admin = User('l2i', 'l2i@example.com')
    print(admin)
    db.session.add(admin)
    db.session.commit()
