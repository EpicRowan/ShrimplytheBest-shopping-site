
def load_users(file_name):

	for i, row in enumerate(open(file_name)):
		row = row.rstrip()
		user_id, email, password = row.split("|")

		user = User(email = email, password = password)

		db.session.add(user)

	db.session.commit(user)


def load_shrimp(file_name):

	for i, row in enumerate(open(filename)):
		row = row.rstrip()

		shrimp = Shrimp()

		db.session.add(shrimp)

	db.session.commit(shrimp)