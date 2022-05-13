from app import db, Puppy


## CREATE ##
my_puppy = Puppy('rufus', 5, 'monkey')
db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()
print(all_puppies)

# SELECT BY ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# FILTERS
puppy_sammy = Puppy.query.filter_by(name='sammy')
print(puppy_sammy.all())


## UPDATE ## 
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


## DELETE ##
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_pups = Puppy.query.all()
print(all_pups)