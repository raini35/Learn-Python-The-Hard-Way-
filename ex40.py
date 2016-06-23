class Song(object): 
	
		def __init__(self, lyrics):
			self.lyrics = lyrics
			
		def sing_me_a_song(self):
			for line in self.lyrics:
				print line 
				
happy_bday = Song(["Happy birthday to you", 
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family", 
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

x = ["Hello"]

first_one = Song(x)

first_one.sing_me_a_song()


class Pet(object): 
	
	def __init__(self, name, species): 
		self.name = name 
		self.species = species 
		
	def getName(self): 
		return self.name
		
	def getSpecies(self): 
		return self.species 
			
	def __str__(self)
		return "%s is a %s" % (self.name, self.species)
			
class Dog(Pet): 
		
	def __init__(self, name, chases_cats): 
		Pet.__init__(self, name, "Dog")
		self.chases_cats = chases_cats
			
	def chasesCats(self): 
		return self.chases_cats
			
class Cat(Pet)

	def __init__(self, name, hates_dogs):
		Pet.__init__(self, name, "Cat")
		self.hates_dogs = hates_dogs
		
	def hatesDogs(self):
		return self.hates_dogs