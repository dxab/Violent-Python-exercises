import crypt
#This program takes a common password dictionary as dictionary.txt
#file and calculates the crypt() hashes along with a given salt
#it creates an output file of the saltes hashes called ohashes.txt
#it then takes password:combo input from a text file named 
#breaches.txt and parses the hashes from it. These parsed hashes
#output into ihashes.txt. Finally this program compares the two 
#hash lists to find any matches available. If a match is found it 
#prints the hash so the user can manually go check what line the 
#hash was found in the ohashes.txt file and find that same line 
#in the dictionary, thus giving the user the password for the user.


def main():
	#displays welcome message
	show_msg()
	salt = get_salt()
	generate_hashes(salt)
	inputPass = parse_data()
	compare_values()



def show_msg():
	print("Welcome to crypt() cracker v1.0")
def get_salt():
	salt = input("Enter the known salt: ")
	return salt
def generate_hashes(salt):
	#this is the part that creates the ohashes.txt file
	inputFile = open('dictionary.txt', 'r')
	outputFile = open('ohashes.txt', 'w')
	for pwd in inputFile:
		pwd = pwd.rstrip("\n")
		hash = crypt.crypt(pwd,salt)
		outputFile.write(hash + "\n")
	inputFile.close()
	outputFile.close()
def parse_data():
	#this is the part that creates the ihashes.txt file
	inputFile = open("breach.txt", 'r')
	outputFile = open("ihashes.txt", "w")
	for data in inputFile:
		data = data.split(":")
		data = data[1].rstrip("\n")
		outputFile.write(data + "\n")
	outputFile.close()
	inputFile.close()
def compare_values():
	#this is the comparison phase. The line in the ihashes.txt file
	#is fed into the testPass function and it compares it to hashes in the 
	#ohashes file
	breachedHash = open("ihashes.txt", 'r')
	for line in breachedHash:
		breachedPass = line.rstrip("\n")
		testPass(breachedPass)
	breachedHash.close()
def testPass(breachedPass):
	dictHash = open("ohashes.txt", 'r')
	foundHashes = open("foundHashes.txt", "w")
	for line in dictHash:
		dictionaryPass = line.rstrip('\n')
		if breachedPass == dictionaryPass:
			print("Password Found for", breachedPass)
			foundHashes.write(breachedPass + "\n")
	dictHash.close()
	foundHashes.close()
main()

