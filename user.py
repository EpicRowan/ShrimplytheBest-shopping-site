class User(object):

	def __init__(self,
				user_id,
				email,
				password,
				):

		self.user_id = user_id
		self.email = email
		self.password = password

	def __repr__(self):
		"""Convenience method to show information about user in console."""
		return "<User: {}, {}, {}>".format(self.user_id, self.email)

def read_user_from_file(filepath):
	"""Read user data and populate dictionary.

	Dictionary will be {id: User object}
	"""

	users = {}

	with open(filepath) as file:
		for line in file:
			(user_id,
			email,
			password,
			) = line.strip().split("|")
    
    
			users[user_id] = User(user_id, email, password)

	return users

def get_all_users():
    """Return list of users"""

    return list(users.values())


def get_user_by_id(user_id):
    """Return a shrimp, given its id."""

    # This relies on access to the global dictionary `shrimp_types`

    return users[user_id]


users = read_user_from_file("users.txt")
