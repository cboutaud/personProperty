import csv
import operator

inputfile = open('crimes.csv', 'rU')
csv_reader = csv.DictReader(inputfile)

lsoasPer = {}
lsoasPro = {}
lsoas = {}

# FOR TEST
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

sortedPerRank = sorted(lsoas.items(), key=lambda x: x[1]["personTotal"], reverse=True)

i=0

while i < len(sortedPerRank):
	sortedPerRank[i][1]['personRank'] = 0
	personTotal = sortedPerRank[i][1]['personTotal']
	previousPersonTotal = sortedPerRank[i-1][1]['personTotal']
	if i > 0 and personTotal == previousPersonTotal:
		sortedPerRank[i][1]['personRank'] = sortedPerRank[i-1][1]['personRank']
		sortedPerRank[i][1]['personTie'] = 'Y'
		sortedPerRank[i-1][1]['personTie'] = 'Y'
	else:
		sortedPerRank[i][1]['personRank'] = i+1
		sortedPerRank[i][1]['personTie'] = 'N'
	i+=1

sortedProRank = sorted(lsoas.items(), key=lambda x: x[1]["propertyTotal"], reverse=True)

j=0

while j < len(sortedProRank):
	sortedProRank[j][1]['propertyRank'] = 0
	propertyTotal = sortedProRank[j][1]['propertyTotal']
	previousPropertyTotal = sortedProRank[j-1][1]['propertyTotal']
	if j > 0 and propertyTotal == previousPropertyTotal:
		sortedProRank[j][1]['propertyRank'] = sortedProRank[j-1][1]['propertyRank']
		sortedProRank[j][1]['propertyTie'] = 'Y'
		sortedProRank[j-1][1]['propertyTie'] = 'Y'
	else:
		sortedProRank[j][1]['propertyRank'] = j+1
		sortedProRank[j][1]['propertyTie'] = 'N'
	j+=1
	
sortedLsoas = sorted(lsoas.items(), key=operator.itemgetter(0))


outputfile = open('lsoa.csv', 'wb')
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["lsoa","id","Violence and sexual offences","Robbery","personTotal","personRank","personTie","Burglary","Vehicle crime","Bicycle theft","Criminal damage and arson","Other theft","Shoplifting","Theft from the person","propertyTotal","propertyRank","propertyTie"])
for lsoa in sortedLsoas:
	csv_writer.writerow([lsoa[0],lsoa[1]["id"],lsoa[1]["Violence and sexual offences"],lsoa[1]["Robbery"],lsoa[1]["personTotal"],lsoa[1]["personRank"],lsoa[1]["personTie"],lsoa[1]["Burglary"],lsoa[1]["Vehicle crime"],lsoa[1]["Bicycle theft"],lsoa[1]["Criminal damage and arson"],lsoa[1]["Other theft"],lsoa[1]["Shoplifting"],lsoa[1]["Theft from the person"],lsoa[1]["propertyTotal"],lsoa[1]["propertyRank"],lsoa[1]["propertyTie"]])
