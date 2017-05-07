import sys
import pickle

class Mary():
	def __init__(self):
		self.messages = dict()
		self.messages = {"Mary":[], "Margeret":[]}
		try:
			self.messages = self.deserialize()
		except FileNotFoundError:
			pass


	def write_message(self): 
		mary_message = input("send a message: ")
		for k, v in self.messages.items():
			# print("mary's message", mary_message)
			if k == "Mary":
				v = self.messages["Mary"].append(mary_message)
			# return self.messages
		# print("her_message is gunna run", self.messages)
		self.serialize()


	def read_message(self): 
	# print("mary wants to read")
		self.messages = self.deserialize()
		# print("mary's message", self.messages)
		for k,v in self.messages.items():
			print("message", self.messages)




	def serialize(self):
		# print("serialize is running")
		with open('notes.txt', 'wb+') as f:
			pickle.dump(self.messages, f)


	def deserialize(self):
		print("deserialize is running")
		try:
			with open('notes.txt', 'rb+') as f:
				self.messages = pickle.load(f)
		except EOFError:
			pass

		return self.messages



