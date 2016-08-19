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


sortedViolenceRank = sorted(lsoas.items(), key=lambda x: x[1]["Violence and sexual offences"], reverse=True)

g=0

while g < len(sortedViolenceRank):
	sortedViolenceRank[g][1]['violenceRank'] = 0
	violence = sortedViolenceRank[g][1]['Violence and sexual offences']
	previousViolence = sortedViolenceRank[g-1][1]['Violence and sexual offences']
	if g > 0 and violence == previousViolence:
		sortedViolenceRank[g][1]['violenceRank'] = sortedViolenceRank[g-1][1]['violenceRank']
		sortedViolenceRank[g][1]['violenceTie'] = 'Y'
		sortedViolenceRank[g-1][1]['violenceTie'] = 'Y'
	else:
		sortedViolenceRank[g][1]['violenceRank'] = g+1
		sortedViolenceRank[g][1]['violenceTie'] = 'N'
	g+=1



sortedRobberyRank = sorted(lsoas.items(), key=lambda x: x[1]["Robbery"], reverse=True)

h=0

while h < len(sortedRobberyRank):
	sortedRobberyRank[h][1]['robberyRank'] = 0
	robbery = sortedRobberyRank[h][1]['Robbery']
	previousRobbery = sortedRobberyRank[h-1][1]['Robbery']
	if h > 0 and robbery == previousRobbery:
		sortedRobberyRank[h][1]['robberyRank'] = sortedRobberyRank[h-1][1]['robberyRank']
		sortedRobberyRank[h][1]['robberyTie'] = 'Y'
		sortedRobberyRank[h-1][1]['robberyTie'] = 'Y'
	else:
		sortedRobberyRank[h][1]['robberyRank'] = h+1
		sortedRobberyRank[h][1]['robberyTie'] = 'N'
	h+=1



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



sortedBurglaryRank = sorted(lsoas.items(), key=lambda x: x[1]["Burglary"], reverse=True)

k=0

while k < len(sortedBurglaryRank):
	sortedBurglaryRank[k][1]['burglaryRank'] = 0
	burglary = sortedBurglaryRank[k][1]['Burglary']
	previousBurglary = sortedBurglaryRank[k-1][1]['Burglary']
	if k > 0 and burglary == previousBurglary:
		sortedBurglaryRank[k][1]['burglaryRank'] = sortedBurglaryRank[k-1][1]['burglaryRank']
		sortedBurglaryRank[k][1]['burglaryTie'] = 'Y'
		sortedBurglaryRank[k-1][1]['burglaryTie'] = 'Y'
	else:
		sortedBurglaryRank[k][1]['burglaryRank'] = k+1
		sortedBurglaryRank[k][1]['burglaryTie'] = 'N'
	k+=1



sortedCarRank = sorted(lsoas.items(), key=lambda x: x[1]["Vehicle crime"], reverse=True)

l=0

while l < len(sortedProRank):
	sortedCarRank[l][1]['carRank'] = 0
	car = sortedCarRank[l][1]['Vehicle crime']
	previousCar = sortedCarRank[l-1][1]['Vehicle crime']
	if l > 0 and car == previousCar:
		sortedCarRank[l][1]['carRank'] = sortedCarRank[l-1][1]['carRank']
		sortedCarRank[l][1]['carTie'] = 'Y'
		sortedCarRank[l-1][1]['carTie'] = 'Y'
	else:
		sortedCarRank[l][1]['carRank'] = l+1
		sortedCarRank[l][1]['carTie'] = 'N'
	l+=1



sortedBikeRank = sorted(lsoas.items(), key=lambda x: x[1]["Bicycle theft"], reverse=True)

m=0

while m < len(sortedBikeRank):
	sortedBikeRank[m][1]['propertyRank'] = 0
	bike = sortedBikeRank[m][1]['Bicycle theft']
	previousBike = sortedBikeRank[m-1][1]['Bicycle theft']
	if m > 0 and bike == previousBike:
		sortedBikeRank[m][1]['bikeRank'] = sortedBikeRank[m-1][1]['bikeRank']
		sortedBikeRank[m][1]['bikeTie'] = 'Y'
		sortedBikeRank[m-1][1]['bikeTie'] = 'Y'
	else:
		sortedBikeRank[m][1]['bikeRank'] = m+1
		sortedBikeRank[m][1]['bikeTie'] = 'N'
	m+=1



sortedArsonRank = sorted(lsoas.items(), key=lambda x: x[1]["Criminal damage and arson"], reverse=True)

n=0

while n < len(sortedArsonRank):
	sortedArsonRank[n][1]['arsonRank'] = 0
	arson = sortedArsonRank[n][1]['Criminal damage and arson']
	previousArson = sortedArsonRank[n-1][1]['Criminal damage and arson']
	if n > 0 and arson == previousArson:
		sortedArsonRank[n][1]['arsonRank'] = sortedArsonRank[n-1][1]['arsonRank']
		sortedArsonRank[n][1]['arsonTie'] = 'Y'
		sortedArsonRank[n-1][1]['arsonTie'] = 'Y'
	else:
		sortedArsonRank[n][1]['arsonRank'] = n+1
		sortedArsonRank[n][1]['arsonTie'] = 'N'
	n+=1



sortedOtherRank = sorted(lsoas.items(), key=lambda x: x[1]["Other theft"], reverse=True)

o=0

while o < len(sortedOtherRank):
	sortedOtherRank[o][1]['otherRank'] = 0
	other = sortedOtherRank[o][1]['Other theft']
	previousOther = sortedOtherRank[o-1][1]['Other theft']
	if o > 0 and other == previousOther:
		sortedOtherRank[o][1]['otherRank'] = sortedOtherRank[o-1][1]['otherRank']
		sortedOtherRank[o][1]['otherTie'] = 'Y'
		sortedOtherRank[o-1][1]['otherTie'] = 'Y'
	else:
		sortedOtherRank[o][1]['otherRank'] = o+1
		sortedOtherRank[o][1]['otherTie'] = 'N'
	o+=1



sortedShopRank = sorted(lsoas.items(), key=lambda x: x[1]["Shoplifting"], reverse=True)

p=0

while p < len(sortedShopRank):
	sortedShopRank[p][1]['shopRank'] = 0
	shop = sortedShopRank[p][1]['Shoplifting']
	previousShop = sortedShopRank[p-1][1]['Shoplifting']
	if p > 0 and shop == previousShop:
		sortedShopRank[p][1]['shopRank'] = sortedShopRank[p-1][1]['shopRank']
		sortedShopRank[p][1]['shopTie'] = 'Y'
		sortedShopRank[p-1][1]['shopTie'] = 'Y'
	else:
		sortedShopRank[p][1]['shopRank'] = p+1
		sortedShopRank[p][1]['shopTie'] = 'N'
	p+=1



sortedDirectRank = sorted(lsoas.items(), key=lambda x: x[1]["Theft from the person"], reverse=True)

q=0

while q < len(sortedDirectRank):
	sortedDirectRank[q][1]['directRank'] = 0
	direct = sortedDirectRank[q][1]['Theft from the person']
	previousDirect = sortedDirectRank[q-1][1]['Theft from the person']
	if q > 0 and direct == previousDirect:
		sortedDirectRank[q][1]['directRank'] = sortedDirectRank[q-1][1]['directRank']
		sortedDirectRank[q][1]['directTie'] = 'Y'
		sortedDirectRank[q-1][1]['directTie'] = 'Y'
	else:
		sortedDirectRank[q][1]['directRank'] = q+1
		sortedDirectRank[q][1]['directTie'] = 'N'
	q+=1


	
sortedLsoas = sorted(lsoas.items(), key=operator.itemgetter(0))


outputfile = open('lsoa.csv', 'wb')
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["lsoa","id","Violence and sexual offences","violenceRank","Robbery","robberyRank","personTotal","personRank","personTie","Burglary","burglaryRank","Vehicle crime","carRank","Bicycle theft","bikeRank","Criminal damage and arson","arsonRank","Other theft","otherRank","Shoplifting","shopRank","Theft from the person","directRank","propertyTotal","propertyRank","propertyTie"])
for lsoa in sortedLsoas:
	csv_writer.writerow([lsoa[0],lsoa[1]["id"],lsoa[1]["Violence and sexual offences"],lsoa[1]["violenceRank"],lsoa[1]["Robbery"],lsoa[1]["robberyRank"],lsoa[1]["personTotal"],lsoa[1]["personRank"],lsoa[1]["personTie"],lsoa[1]["Burglary"],lsoa[1]["burglaryRank"],lsoa[1]["Vehicle crime"],lsoa[1]["carRank"],lsoa[1]["Bicycle theft"],lsoa[1]["bikeRank"],lsoa[1]["Criminal damage and arson"],lsoa[1]["arsonRank"],lsoa[1]["Other theft"],lsoa[1]["otherRank"],lsoa[1]["Shoplifting"],lsoa[1]["shopRank"],lsoa[1]["Theft from the person"],lsoa[1]["directRank"],lsoa[1]["propertyTotal"],lsoa[1]["propertyRank"],lsoa[1]["propertyTie"]])
