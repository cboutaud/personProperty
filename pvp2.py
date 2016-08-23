import csv
import operator
import scipy.stats as ss

inputfile = open('crimes.csv', 'rU')
csv_reader = csv.DictReader(inputfile)

lsoasPer = {}
lsoasPro = {}
lsoas = {}

# USING ONLY FIRST 100 ROWS FOR TEST
# for index, row in enumerate(csv_reader):
# 	if index >= 100:
# 		break

for row in csv_reader:
	lsoa = row["LSOA.name"]
	lsoaCode = row["LSOA.code"]
	pvp = row["pvp"]
	crimetype = row["Crime.type"]

	if (lsoa not in lsoas):
		lsoas[lsoa] = {}
		lsoas[lsoa]["id"] = lsoaCode
		lsoas[lsoa]["personTotal"] = 0
		lsoas[lsoa]["propertyTotal"] = 0
		lsoas[lsoa]["Violence and sexual offences"] = 0
		lsoas[lsoa]["Robbery"] = 0
		lsoas[lsoa]["Burglary"] = 0
		lsoas[lsoa]["Vehicle crime"] = 0
		lsoas[lsoa]["Bicycle theft"] = 0
		lsoas[lsoa]["Criminal damage and arson"] = 0
		lsoas[lsoa]["Other theft"] = 0
		lsoas[lsoa]["Shoplifting"] = 0
		lsoas[lsoa]["Theft from the person"] = 0
	else:
		pass

	if pvp == "person":
		lsoas[lsoa]["personTotal"] += 1
		if crimetype == "Violence and sexual offences":
			lsoas[lsoa]["Violence and sexual offences"] += 1
		elif crimetype == "Robbery":
			lsoas[lsoa]["Robbery"] += 1
		else:
			print "HODOR"
	elif pvp == "property":
		lsoas[lsoa]["propertyTotal"] += 1
		if crimetype == "Burglary":
			lsoas[lsoa]["Burglary"] += 1
		elif crimetype == "Vehicle crime":
			lsoas[lsoa]["Vehicle crime"] += 1
		elif crimetype == "Bicycle theft":
			lsoas[lsoa]["Bicycle theft"] += 1
		elif crimetype == "Criminal damage and arson":
			lsoas[lsoa]["Criminal damage and arson"] += 1
		elif crimetype == "Other theft":
			lsoas[lsoa]["Other theft"] += 1
		elif crimetype == "Shoplifting":
			lsoas[lsoa]["Shoplifting"] += 1
		elif crimetype == "Theft from the person":
			lsoas[lsoa]["Theft from the person"] += 1
		else:
			print "HODOR"
	else:
		pass

print "HOLD THE DOOR"


#RANKING VIOLENCE AND SEXUAL OFFENCES
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Violence and sexual offences"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["violenceRank"] = ranked[j]
	j += 1



#RANKING ROBBERY
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Robbery"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["robberyRank"] = ranked[j]
	j += 1



#RANKING PERSON CRIME
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["personTotal"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["personRank"] = ranked[j]
	j += 1

print "HOLDTHEDOOR"

#RANKING PROPERTY CRIME
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["propertyTotal"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["propertyRank"] = ranked[j]
	j += 1


#RANKING BURGLARY CRIME
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Burglary"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["burglaryRank"] = ranked[j]
	j += 1

print "HOLDDOOR"

#RANKING VEHICLE CRIME CRIME
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Vehicle crime"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["carRank"] = ranked[j]
	j += 1



#RANKING BICYCLE THEFT CRIME
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Bicycle theft"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["bikeRank"] = ranked[j]
	j += 1



#RANKING CRIMINAL DAMAGE AND ARSON
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Criminal damage and arson"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["arsonRank"] = ranked[j]
	j += 1



#RANKING OTHER THEFT
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Other theft"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["otherRank"] = ranked[j]
	j += 1



#RANKING SHOPLIFTING
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Shoplifting"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["shopRank"] = ranked[j]
	j += 1



#RANKING THEFT FROM THE PERSON
toBeRanked = []

i=0
while i < len(lsoas):
	toBeRanked.append(lsoas.values()[i]["Theft from the person"])
	i+=1

ranked = (len(toBeRanked) - ss.rankdata(toBeRanked))

j = 0
while j < len(lsoas):
	lsoas.values()[j]["directRank"] = ranked[j]
	j += 1
	
sortedLsoas = sorted(lsoas.items(), key=operator.itemgetter(0))

print "HODOR"

outputfile = open('lsoa.csv', 'wb')
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["lsoa","id","Violence and sexual offences","violenceRank","Robbery","robberyRank","personTotal","personRank","Burglary","burglaryRank","Vehicle crime","carRank","Bicycle theft","bikeRank","Criminal damage and arson","arsonRank","Other theft","otherRank","Shoplifting","shopRank","Theft from the person","directRank","propertyTotal","propertyRank"])
for lsoa in sortedLsoas:
	csv_writer.writerow([lsoa[0],lsoa[1]["id"],lsoa[1]["Violence and sexual offences"],lsoa[1]["violenceRank"],lsoa[1]["Robbery"],lsoa[1]["robberyRank"],lsoa[1]["personTotal"],lsoa[1]["personRank"],lsoa[1]["Burglary"],lsoa[1]["burglaryRank"],lsoa[1]["Vehicle crime"],lsoa[1]["carRank"],lsoa[1]["Bicycle theft"],lsoa[1]["bikeRank"],lsoa[1]["Criminal damage and arson"],lsoa[1]["arsonRank"],lsoa[1]["Other theft"],lsoa[1]["otherRank"],lsoa[1]["Shoplifting"],lsoa[1]["shopRank"],lsoa[1]["Theft from the person"],lsoa[1]["directRank"],lsoa[1]["propertyTotal"],lsoa[1]["propertyRank"]])
