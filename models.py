class User:
	def __init__(self, id, name, points):
		self.id = id
		self.name = name
		self.points = points

	def __repr__(self):
		return '<id {}>'.format(self.id)
	
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'points': self.points
		}