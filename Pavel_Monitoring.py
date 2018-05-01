from random import randint
from random import randrange

print "\nHi Pavel! What are you thinking about?\n"
print "1. A big cup of bulgarian yogurt\n2. A new TV series to watch\n3. A lovely italian girl called Milena\n"

thought=raw_input ("> ")
ans='no'
ans_yes=("Don't be hurry","Take your time","Are You sure?")

while thought=="1" or thought=="2":
	q=randint(3,6)
	if thought=="1":
		print "Come on Pavel! You can resist.\n"
	
	else:
		print "Someone should think you're becoming so boring...\n"
	
	i1=0
	i2=0
	
	print "Are you still thinking about it?"
	ans=raw_input ("ans> ")
	
	while ans!="no":
		#print q   #Verifica*
		random_index_ans=randrange(0,len(ans_yes))
		
		if thought=="1":
			i1=i1+1
			if i1==q:
				print ans_yes[random_index_ans]
				#print ("indice: "), i1    #Verifica*
				i1=0
				#print i1	#Verifica*
				ans=raw_input ("ans> ")
			else:
				print "\nTry again!"
				#print i1	#Verifica*
				ans=raw_input ("ans> ")
				
		else:
			i2=i2+1
			if i2==q:
				print ans_yes[random_index_ans]
				#print ("indice: "), i1    #Verifica*
				i2=0
				#print i2	#Verifica*
				ans=raw_input ("ans> ")
			else:
				print "\nTry again!"
				#print i1	#Verifica*
				ans=raw_input ("ans> ")
				
		
	if ans=="no":
		i1=0
		i2=0
		print "\n 1 2 3?"
		thought=raw_input ("> ")
	
if thought=="3":
	print "Okay, now you're good. You won a kiss.\n"



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



