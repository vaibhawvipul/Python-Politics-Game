"""Om!""" 
import sys
import math
import time
print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vEnter Your name"
name = raw_input("> ")
"""This will display only first name"""
f_name = name.split()
print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vWelcome %r! Be a \n\n\n\n\t\t\t...TRAILBLAZER..." %f_name[0]
print"\n Demo version 2"
print "\v\v\v\v1.Play"
print "\n2.About"
print "\n3.Exit"
print "\nCOPYRIGHTS RESERVED"
a = int(raw_input("\n\nEnter your choice -  "))
if a == 3:
	sys.exit(0)
elif a == 2:
	print "\nThis game was concieved by Vipul Vaibhaw. It was build by very creative team of Fergusson College students"
	print "\nWe are very collaborative team. We have an out of the box idea ready almost everytime."
	print "\nThis game was build using Python."
	print "\nWant to contact us, drop an e-mail to vaibhaw.vipul@gmail.com"
elif a == 1:
	print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vWelcome President %r to your office." %f_name[0]
	print "\n\nHere is a message from intelligence. Press ENTER to see the message"
	raw_input("")
	print "A Terror outfit has grown very strong"
	time.sleep(3)
	print "They are constantly attacking Kamuri. Kamuri is a small nation which shares boundary with us. It also has religious importance for a minority group in your country."
	time.sleep(5)
	print"Kamuri and your Country has ancestral tie-ups"
	time.sleep(2)
	print "Our espionage have reported that it may soon try to overthrow government of Kamuri"
	time.sleep(3)
	print "\nPress ENTER to continue..."
	raw_input("")
	print "\n\v\v\v\v\v\v\v\v\v\v\v\v\vPresident of a Superpower nations has invited you over dinner."
	print "\nIt could be benificial to your country. You could sort out issue like economic relations, weapon treaties or nuclear deal etc."
	print "\nElse you can stay in our own country and solve internal affairs first."
	print "\n\n1.You accept the invitation."
	print "\n2.You decline the invitation."
	b = int(raw_input("\n> "))
	if b == 1:
		print "\n\v\v\vGreat thought! It would not have been a good step to decline the invitation from a Superpower."
		time.sleep(3)
		print "\n\n\n'President Mark will meet you anytime from now. Sorry for inconvinience President %r' says Secretary " %f_name[0]
		time.sleep(5)
		print "\n\n\n\v\v\vPresident Mark is here!"
		time.sleep(3)
		print "\n\n\nPresident %r, Nice to meet you" %f_name[0]
		time.sleep(3)
		print "\nIt is good to know that your country is quite concerned about small countries neighbouring you."
		time.sleep(4)
		print "\nBut sometimes it is better to detach yourself from weak ones..."
		time.sleep(2)
		print "...and attach youself to more powerful nations."
		time.sleep(3)
		print "\n\nPress ENTER to continue..."
		raw_input("")
		print "\v\v\v\v\v'So here is a deal...'"
		print "\n\n1. If you and your ally are ready to let us make army bases in you country, we may support you at war."
		print "\n2. If you allow, while your ally deny We 'will' support you at war. Our soldiers will lead from front."
		print "\n3. If you both deny, Your enemy will be showered with our benevolence." 
		print "\n\n\v\v1. You allow them."
		print "2. You deny them"
		c = int(raw_input("\n> "))
		if c == 1:
			print "\v\v\v'Great! Now let's see what Your ally has to say'"
			time.sleep(3)
			print "\nYour ally supported you in this decision. President Mark has built armybase in your country."
			time.sleep(3)
			print "\nPresident of 'Kamuri' has sent you a message. Press ENTER to read it."
			raw_input("")
			print "\n\n\v\v\vPresident we need help. Terrorists have attacked us. Help us!!"
			print "\n\n1. You send army"
			print "2. You ask Mark to help"
			print "3. You ignore the problem and do not send Army."
			d = int(raw_input("\n> "))
			if d == 2:
				print "Mark denies help. He had said that he 'may' help you at war."
				time.sleep(3)
				print "\n\nWhat will you do now?"
				print "\n1. You send army"
				print "2. You ignore the problem and do not send Army."
				e = int(raw_input("> "))
				if e == 1:
					print "That's like an good ally!"
					time.sleep(2)
					print "Your army is ready to leave for Kamuri"
					time.sleep(3)
					print "ALERT!"
					time.sleep(1)
					print "ALERT!!"
					time.sleep(1)
					print "ALERT!!!"
					time.sleep(2)
					print "\n\nThere is massive flood in your country! Lots of lives are in danger!"
					print "\nMessage from Cheif Minister of that flood-struck state. Press ENTER to see Message"
					raw_input("")
					print "\n\n\vPresident! We need Army support. Only trained personnels like Army men can help us"
					print "\nHundreds of people are trapped here. Army needed immediately!"
					print "\v\v\v\v1. You send your army to Kamuri."
					print "2. You re-direct your army to rescue people from flood-struck state."
					f = int(raw_input(""))
					if f == 1:
						print "\n\nInternational relations matters President %r! But your citizens are feeling unsafe in your country." %f_name[0]
						time.sleep(2)
						print "\nMisiters withdraw support and your government falls..."
						time.sleep(2)
						print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
					else:
						print "\n\nGood decision to send army to rescue your people first."
						print "\nArmy did fantastic job and saved hundreds of lives."
						time.sleep(3)
						print "\nYou become peoples favorite President!"
						time.sleep(3)
						print "\n\nBut Kamuri problem is unsolved yet!"
						time.sleep(3)
						print "Government is about to collapse. It would be a big threat to your country's security as well."
						time.sleep(4)
						print "\n1. Should we plan to offer an Armed force help?"
						print "2. Or Negotitate with Terrorists." 
						time.sleep(3)
						print "\nTerrorists want to contact you."
						time.sleep(2)
						print "\nThey have send you a message"
						print "\nPress ENTER to see the message..."
						raw_input("")
						print "\v\v\nPresident %r if you ignore to help Kamuri, We will support you in next elections." %f_name[0]
						print "People of our religion will support you. Secondly, we may ignore your country from our HIT LIST as well!!"
						g = int(raw_input("\nTake your decision \n>"))
						if g == 2:
							print "\nPresident %r day by day conditions in Kamuri got worse." %f_name[0]
							time.sleep(2)
							print "\nKamuri Government was overthrown by Terrorists"
							time.sleep(2)
							print "\nYou even lost some reputation in World! News spread that you took this decision as you disbelieved your army!"
							time.sleep(3)
							print "You lost trust amongsts citizen and they voted against you!"
							time.sleep(5)
							print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
						elif g == 1:
							print "\nYou saved Kamuri. But back to back floods and warfare has made your economy weak"
							time.sleep(5)
							print "\nPresident Mark has come up with another deal"
							time.sleep(3)
							h = int(raw_input("\n\n1. You agree to meet him. \n2. You deny \n>"))
							if h == 2:
								print "\n\nSuperpower nation is upset now. He breaks offs economic ties and your economy crashes"
								time.sleep(4)
								print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
							else :
								print "\v\v\v\v\vSo Here is the deal!"
								print "\n\n1. If you allow us to make more armybases in your country. We WILL help you at any cost!"
								print "2. If you deny, we break economic ties with you and your economy may crash!"
								raw_input("\nPress ENTER to continue... ")
								print "\n\nHere is a message from Minister of Scientific development"
								time.sleep(4)
								print "\n\n\nWe have developed special kind of rice, which is new to the world market."
								print "\nWe may sell it to world market to stabalize our economy."
								time.sleep(7)
								print "\nBut..."
								time.sleep(3)
								print "\nWe are not sure about its success."
								time.sleep(4)
								i = int(raw_input("Take your decision - "))
								if i == 2:
									print "\n\nSuperPower got upset but our rice was successful invention!"
									print "\nYou managed to survive..."
									time.sleep(5)
									print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU WIN!!"
								else:	
									print "\nThis time you caught MARK! He had to help your country now because of 'will' which he had said in deal."
									time.sleep(5)
									print "\nAlso your rice got successful and Mark needed that rice to help his country"
									time.sleep(4)
									print "\nYou sold that rice to Mark with a deal that from now any of his Army movement won't be allowed without your consesus."
									time.sleep(5)
									print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU WIN!!!!!"
				else:
					print "Being Diplomatic!"
					time.sleep(3)
					print "Riots!!!!"
					time.sleep(2)
					print "Religious Minority in your country got upset and their protest have turned into riots. You LOSE!!"
			elif d == 1:
				print "That's like an good ally!"
				time.sleep(2)
				print "Your army is ready to leave for Kamuri"
				time.sleep(3)
				print "ALERT!"
				time.sleep(1)
				print "ALERT!!"
				time.sleep(1)
				print "ALERT!!!"
				time.sleep(2)
				print "\n\nThere is massive flood in your country! Lots of lives are in danger!"
				print "\nMessage from Cheif Minister of that flood-struck state. Press ENTER to see Message"
				raw_input("")
				print "\n\n\vPresident! We need Army support. Only trained personnels like Army men can help us"
				print "\nHundreds of people are trapped here. Army needed immediately!"
				print "\v\v\v\v1. You send your army to Kamuri."
				print "2. You re-direct your army to rescue people from flood-struck state."
				f = int(raw_input("\n>"))
				if f == 1:
					print "\n\nInternational relations matters President %r! But your citizens are feeling unsafe in your country." %f_name[0]
					time.sleep(2)
					print "\nMisiters withdraw support and your government falls..."
					time.sleep(2)
					print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
				elif f == 2:
					print "\n\nGood decision to send army to rescue your people first."
					print "\nArmy did fantastic job and saved hundreds of lives."
					time.sleep(3)
					print "\nYou become peoples favorite President!"
					time.sleep(3)
					print "\n\nBut Kamuri problem is unsolved yet!"
					time.sleep(3)
					print "Government is about to collapse. It would be a big threat to your country's security as well."
					time.sleep(4)
					print "\n1. Should we plan to offer an Armed force help?"
					print "2. Or Negotitate with Terrorists." 
					time.sleep(3)
					print "\nTerrorists want to contact you."
					time.sleep(2)
					print "\nThey have send you a message"
					print "\nPress ENTER to see the message..."
					raw_input("")
					print "\v\v\nPresident %r if you ignore to help Kamuri, We will support you in next elections." %f_name[0]
					print "People of our religion will support you. Secondly, we may ignore your country from our HIT LIST as well!!"
					g = int(raw_input("\nTake your decision \n>"))
					if g == 2:
						print "\nPresident %r day by day conditions in Kamuri got worse." %f_name[0]
						time.sleep(2)
						print "\nKamuri Government was overthrown by Terrorists"
						time.sleep(2)
						print "\nYou even lost some reputation in World! News spread that you took this decision as you disbelieved your army!"
						time.sleep(3)
						print "You lost trust amongsts citizen and they voted against you!"
						time.sleep(5)
						print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
					elif g == 1:
						print "\nYou saved Kamuri. But back to back floods and warfare has made your economy weak"
						time.sleep(5)
						print "\nPresident Mark has come up with another deal"
						time.sleep(3)
						h = int(raw_input("\n\n1. You agree to meet him. \n2. You deny>"))
						if h == 2:
							print "\n\nSuperpower nation is upset now. He breaks offs economic ties and your economy crashes"
							time.sleep(4)
							print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
						else :
							print "\v\v\v\v\vSo Here is the deal!"
							print "\n\n1. If you allow us to make more armybases in your country. We WILL help you at any cost!"
							print "2. If you deny, we break economic ties with you and your economy may crash!"
							raw_input("\nPress ENTER to continue... ")
							print "\n\nHere is a message from Minister of Scientific development"
							time.sleep(4)
							print "\n\n\nWe have developed special kind of rice, which is new to the world market."
							print "\nWe may sell it to world market to stabalize our economy."
							time.sleep(7)
							print "\nBut..."
							time.sleep(3)
							print "\nWe are not sure about its success."
							time.sleep(4)
							i = int(raw_input("Take your decision - "))
							if i == 2:
								print "\n\nSuperPower got upset but our rice was successful invention!"
								print "\nYou managed to survive..."
								time.sleep(5)
								print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU WIN!!"
							else:	
								print "\nThis time you caught MARK! He had to help your country now because of 'will' which he had said in deal."
								time.sleep(5)
								print "\nAlso your rice got successful and Mark needed that rice to help his country"
								time.sleep(4)
								print "\nYou sold that rice to Mark with a deal that from now any of his Army movement won't be allowed without your consesus."
								time.sleep(5)
								print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU WIN!!!!!"
				else :
					print "Bye!"
			else:
				print "Being Diplomatic!"
				time.sleep(3)
				print "Riots!!!!"
				time.sleep(2)
				print "Religious Minority in your country got upset and their protest have turned into riots"
		else :
			print "'Ok President %r, Hope this decision won't cost you much!'" %f_name[0]
	else :
		print "Not a good decision to decline invitation from a superpower!"
		print "\nPresident of 'Kamuri' has sent you a message. Press ENTER to read it."
		raw_input("")
		print "\n\n\v\v\vPresident we need help. Terrorists have attacked us. Help us!!"
		print "\n\n1. You send army"
		print "2. You ignore the problem and do not send Army."
		d = int(raw_input("\n> "))
		if d == 2:
			print "Mark denies help. He had said that he 'may' help you at war."
			time.sleep(3)
			print "\n\nWhat will you do now?"
			print "\n1. You send army"
			print "2. You ignore the problem and do not send Army."
			e = int(raw_input("> "))
			if e == 1:
				print "That's like an good ally!"
				time.sleep(2)
				print "Your army is ready to leave for Kamuri"
				time.sleep(3)
				print "ALERT!"
				time.sleep(1)
				print "ALERT!!"
				time.sleep(1)
				print "ALERT!!!"
				time.sleep(2)
				print "\n\nThere is massive flood in your country! Lots of lives are in danger!"
				print "\nMessage from Cheif Minister of that flood-struck state. Press ENTER to see Message"
				raw_input("")
				print "\n\n\vPresident! We need Army support. Only trained personnels like Army men can help us"
				print "\nHundreds of people are trapped here. Army needed immediately!"
				print "\v\v\v\v1. You send your army to Kamuri."
				print "2. You re-direct your army to rescue people from flood-struck state."
				f = int(raw_input(""))
				if f == 1:
					print "\n\nInternational relations matters President %r! But your citizens are feeling unsafe in your country." %f_name[0]
					time.sleep(2)
					print "\nMisiters withdraw support and your government falls..."
					time.sleep(2)
					print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
				else:
					print "\n\nGood decision to send army to rescue your people first."
					print "\nArmy did fantastic job and saved hundreds of lives."
					time.sleep(3)
					print "\nYou become peoples favorite President!"
					time.sleep(3)
					print "\n\nBut Kamuri problem is unsolved yet!"
					time.sleep(3)
					print "Government is about to collapse. It would be a big threat to your country's security as well."
					time.sleep(4)
					print "\n1. Should we plan to offer an Armed force help?"
					print "2. Or Negotitate with Terrorists." 
					time.sleep(3)
					print "\nTerrorists want to contact you."
					time.sleep(2)
					print "\nThey have send you a message"
					print "\nPress ENTER to see the message..."
					raw_input("")
					print "\v\v\nPresident %r if you ignore to help Kamuri, We will support you in next elections." %f_name[0]
					print "People of our religion will support you. Secondly, we may ignore your country from our HIT LIST as well!!"
					g = int(raw_input("\nTake your decision \n>"))
					if g == 2:
						print "\nNegotitation with terrorists wasn't a good idea President %r" %f_name[0]
						time.sleep(2)
						print "\nKamuri Government was overthrown by Terrorists"
						time.sleep(2)
						print "\nCitizen felt that their security was at threat and voted against you!"
						time.sleep(3)
						print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
					else:
						print "\nYou saved Kamuri. Your country emerged as a Superpower"
						print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU WON!!!!!!!!"
			else:
				print "Being Diplomatic!"
				time.sleep(3)
				print "Riots!!!!"
				time.sleep(2)
				print "Religious Minority in your country got upset and their protest have turned into riots"
		elif d == 1:
			print "That's like an good ally!"
			time.sleep(2)
			print "Your army is ready to leave for Kamuri"
			time.sleep(3)
			print "ALERT!"
			time.sleep(1)
			print "ALERT!!"
			time.sleep(1)
			print "ALERT!!!"
			time.sleep(2)
			print "\n\nThere is massive flood in your country! Lots of lives are in danger!"
			print "\nMessage from Cheif Minister of that flood-struck state. Press ENTER to see Message"
			raw_input("")
			print "\n\n\vPresident! We need Army support. Only trained personnels like Army men can help us"
			print "\nHundreds of people are trapped here. Army needed immediately!"
			print "\v\v\v\v1. You send your army to Kamuri."
			print "2. You re-direct your army to rescue people from flood-struck state."
			f = int(raw_input("\n>"))
			if f == 1:
				print "\n\nInternational relations matters President %r! But your citizens are feeling unsafe in your country." %f_name[0]
				time.sleep(2)
				print "\nMisiters withdraw support and your government falls..."
				time.sleep(2)
				print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!"
			else:
				print "\n\nGood decision to send army to rescue your people first."
				print "\nArmy did fantastic job and saved hundreds of lives."
				time.sleep(3)
				print "\nYou become peoples favorite President!"
				time.sleep(3)
				print "\n\nBut Kamuri problem is unsolved yet!"
				time.sleep(3)
				print "Government is about to collapse. It would be a big threat to your country's security as well."
				time.sleep(4)
				print "\n1. Should we plan to offer an Armed force help?"
				print "2. Or Negotitate with Terrorists." 
				time.sleep(3)
				print "\nTerrorists want to contact you."
				time.sleep(2)
				print "\nThey have send you a message"
				print "\nPress ENTER to see the message..."
				raw_input("")
				print "\v\v\nPresident %r if you ignore to help Kamuri, We will support you in next elections." %f_name[0]
				print "People of our religion will support you. Secondly, we may ignore your country from our HIT LIST as well!!"
				g = int(raw_input("\nTake your decision \n>"))
				if g == 2:
					print "\nPresident %r day by day conditions in Kamuri got worse." %f_name[0]
					time.sleep(2)
					print "\nKamuri Government was overthrown by Terrorists"
					time.sleep(2)
					print "\nYou even lost some reputation in World! But terrorists ignored to attack your country!"
					time.sleep(3)
					print "This decision of yours gave some time to recover your country from Financial crisis"
					time.sleep(5)
					print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU SURVIVED!!"
				elif g == 1:
					print "\nYou saved Kamuri. But back to back floods and warfare has made your economy weak"
					time.sleep(5)
					print "\nPresident Mark has also cut off economic ties with your country"
					time.sleep(5)
					print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\vYOU LOSE!!" 
				else :
					print "Bye!"
		else:
			print "Being Diplomatic!"
			time.sleep(3)
			print "Riots!!!!"
			time.sleep(2)
			print "Religious Minority in your country got upset and their protest have turned into riots"
	 	
	 
