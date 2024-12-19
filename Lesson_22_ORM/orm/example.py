import example_models
from db_orm import Db

db = Db()


# cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Laptop", 1200))
# cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (2, "Phone", 800))
# cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Tablet", 300))

db.session.add(example_models.Users(name='David', email='david@example.com'))
db.session.add(example_models.Users(name='Max', email='max@example.com'))
db.session.add(example_models.Orders(user_id=2, product="Laptop", amount=1200))
db.session.add(example_models.Orders(user_id=1, product="Phone", amount=800))
db.session.add(example_models.Orders(user_id=1, product="Tablet", amount=300))
db.session.commit()

print('DB created')

# cursor.execute('''
# SELECT users.name, users.email, orders.product, orders.amount
# FROM users
# JOIN orders ON users.id = orders.user_id
# ''')
columns = (example_models.Users.name.label('users.name'),
           example_models.Users.email.label('users.email'),
           example_models.Orders.product.label('orders.product'),
           example_models.Orders.amount.label('orders.amount'))

data = db.session.query(*columns).join(example_models.Orders).all()
print(data)

data2 = db.session.query(*columns).join(example_models.Orders).first()
print(data2._asdict())


