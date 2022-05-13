from app import db,Puppy, Owner, Toy

rufus = Puppy('Rufus', 12, 'pug')
fido = Puppy('Fido', 3, 'pug')

## ADD PUPPIES TO DB
db.session.add_all([rufus, fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
# CREATE OWNER OBJECT

jose = Owner('Jose', rufus.id)

# give some toys 
toy1 = Toy('chew toy', rufus.id)
toy2 = Toy('ball', rufus.id)


db.session.add_all([jose,toy1,toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()