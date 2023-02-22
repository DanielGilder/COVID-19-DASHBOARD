import pickle

updates = []
open_file = open("StoredUpdates.pkl", "wb")
pickle.dump(updates, open_file)
open_file.close()