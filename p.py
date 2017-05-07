# Each module must accept one command line argument 
# that is a message to add to a list (see example below).

# Each module must be able to 
# serialize a dictionary to a file named messages.

# Each module must be able to deserialize 
# the dictionary stored in messages.

# Each module, after the object is deserialized from the file, 
# must add the message to the appropriate list in the dictionary.

# Each module must handle exceptions properly. 
# You may encounter the following while testing your logic.

# FileNotFoundError
# EOFError
# KeyError

# Tip: Make sure you import sys for the command line arguments, and pickle for serialization.
# Dictionary structure
from mary import*
from margaret import* 
import sys 
import pickle



if __name__ == "__main__":
	try:
		# print("im running")
		file_name = sys.argv[0]
		# print("fileName", file_name)
		action = sys.argv[1]
		# print("action", action)
		if action == 'Mary':
			# print("mary wants to run")
			mary = Mary()
			# print("mary is initialized")
			mary.write_message()
			# print("you wrote something")
			mary.read_message()
			# print("mary's reading")
		elif action == 'Marg':
			marg = Margeret()
			marg.write_message()
			marg.read_message()
		# elif action == 'read':
		# 	print("we want to read")
		# 	marv = Mary()
		# 	marv.read_message()
# elif action == 'read' or action == 'a':

	except IndexError:
		print("index error")	
		pass


# mary = Mary()


# marg = Margeret()

# if then run mary and or margaret


# mary.write_message()

