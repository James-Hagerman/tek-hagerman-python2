from app import db, Puppy

db.create_all()

sam = Puppy('Sammy', 3, 'monkey')

db.session.add_all([sam])
db.session.commit()

print(sam.name)