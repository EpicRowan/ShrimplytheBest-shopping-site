from model import Shrimp, User, connect_to_db, db
from server import app


def load_users(user_file_name):

	for i, row in enumerate(open(file_name)):
		row = row.rstrip()
		user_id, email, password = row.split("|")

		user = User(email = email, password = password)

		db.session.add(user)

	db.session.commit(user)


def load_shrimp(shrimp_file_name):

	for i, row in enumerate(open(filename)):
		row = row.rstrip()

		shrimp = Shrimp()

		db.session.add(shrimp)

	db.session.commit(shrimp)


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    user_filename = "seed_data/users.txt"
    shrimp_filename = "seed_data/shrimp.txt"
    load_users(user_filename)
    load_shrimp(shrimp_filename)
