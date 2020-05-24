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
