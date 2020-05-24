"""Shrimp and more for sale!

This provides a shrimp class, helper methods to get all shrimp, find a
shrimp by id.

It reads shrimp data in from a text file.
"""

class Shrimp(object):

	def __init__(self,
				shrimp_id,
				name,
				price,
				image_url,
				)

		self.shrimp_id = shrimp_id
		self.name = name
		self.price = price
		self.image_url  = image_url

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
    
    
            shrimp_types[shrimp_id] = Shrimp(shrimp_id,
											 name,
											 price,
											 image_url,
											 )

    return shrimp_types

def get_by_name(name):
    """Return a shrimp, given its name."""

    # This relies on access to the global dictionary `shrimp_types`

    return shrimp_types[name]


shrimp_types = read_shrimp_from_file("shrimp.txt")
