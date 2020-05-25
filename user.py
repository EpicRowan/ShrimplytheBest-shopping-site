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
		"""Convenience method to show information about shrmp in console."""
		return "<Shrimp: {}, {}, {}>".format(self.shrimp_id, self.name, self.price_str())

def read_shrimp_from_file(filepath):
	"""Read shrimp type data and populate dictionary.

	Dictionary will be {id: Shrimp object}
	"""

	shrimp_types = {}

	with open(filepath) as file:
		for line in file:
			(shrimp_id,
			name,
			price,
			image_url,
			) = line.strip().split("|")

			price = float(price)
    
    
			shrimp_types[shrimp_id] = Shrimp(shrimp_id, name, price, image_url)

	return shrimp_types

def get_all():
    """Return list of shrimp"""

    return list(shrimp_types.values())


def get_by_id(shrimp_id):
    """Return a shrimp, given its id."""

    # This relies on access to the global dictionary `shrimp_types`

    return shrimp_types[shrimp_id]


shrimp_types = read_shrimp_from_file("shrimp.txt")
