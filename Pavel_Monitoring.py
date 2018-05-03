from random import randint
from random import randrange

print "\nHi Pavel! What are you thinking about?\n"
print "1. A big cup of bulgarian yogurt\n2. A new TV series to watch\n3. A lovely italian girl called Milena\n"

tgt=raw_input ("> ")
ans='no'
ansYes=("Don't be hurry","Take your time","Are You sure?")

while tgt=="1" or tgt=="2":
	q=randint(3,6)
	if tgt=="1":
		print "Come on Pavel! You can resist.\n"
	
	else:
		print "Someone should think you're becoming so boring...\n"
	
	i=0
	
	print "Are you still thinking about it? Ans 'yes' or 'no'"
	ans=raw_input ("ans> ")
	ans=ans.lower()
	
	if ans!="no" and ans!="yes":
		print "ERROR!\n\n"
	
	while ans=="yes":
		#print q   #Verifica*
		randomIndexAns=randrange(0,len(ansYes))
		i=i+1
		if i==q:
			print ansYes[randomIndexAns]
			#print ("indice: "), i    #Verifica*
			i=0
			#print i	#Verifica*
			ans=raw_input ("ans> ")
			ans=ans.lower()
		else:
			print "\nTry again!"
			#print i	#Verifica*
			ans=raw_input ("ans> ")
			ans=ans.lower()
				
				
		
	if ans=="no":
		i=0
		print "\n 1 2 3?"
		tgt=raw_input ("> ")
	
if tgt=="3":
	print "Okay, now you're good. You won a kiss.\n\n"
	
if tgt!="1" and tgt!="2" and tgt!="3":
	print "ERROR!\n\n"



#RANDOM
# from random import randint
# for i in range(4):
	# d=randint(3,6)
	# print d
	
# ans_yes=("Don't be hurry","Take your time","Are You sure?")
# for i in range(6):
	# from random import randrange
	# random_index=randrange(0,len(ans_yes))
	# print ("scelta"), i+1
	# print ans_yes[random_index]



