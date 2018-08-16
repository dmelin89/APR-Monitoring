#  Use this one. Reads CSV files and returns relevant info.
from zipfile import ZipFile
import csv
from tkinter import filedialog

#  uses zipfile to extract APR to CWD
apr = ZipFile(filedialog.askopenfilename())
apr.extractall()

#   Asks which quarter the monitoring is for
def validate_quarter(quarter):
    if quarter in ('Q1', 'Q2', 'Q3', 'Q4', 'av', 'ytd'):
        return True
    print('Invalid input. Q1, Q2, Q3, Q4, av, ytd')
    return False

while True:
    try:
        quarter = input('What Quarter are you monitoring? (Q1, Q2, Q3, Q4, av, or ytd)')
        if validate_quarter(quarter):
            break
    except ValueError:
        print('Enter a valid input.')
        continue


#  prints the project name
Q4afile = open('Q4a.csv')
Q4areader = csv.reader(Q4afile)
exampledata = list(Q4areader)
print('Project Name:', exampledata[2][1])

#  Number of Clients

clientcsv = open('Q5a.csv')
clients = (csv.reader(clientcsv))
clientdata = list(clients)
clno = int(clientdata[0][1])

#  turn clients, adults, and leavers into integers

print('Total number of clients: ', clno)

leavers = int((clientdata[4][1]))
adults = int((clientdata[1][1]))

#  Number of Stayers
print('Number of Stayers: ', clno-leavers)

#  destinations

#  less than 90 days
fulldestless90 = open('Q23b.csv')
fulldestlessread = csv.reader(fulldestless90)
less90data = list(fulldestlessread)

#  more than 90 days
fulldestmore90 = (open('q23a.csv'))
fulldestmoreread = csv.reader(fulldestmore90)
more90data = list(fulldestmoreread)


# finds permanent destinations and converts into integer
pdestless90 = int(less90data[40][1])
pdestmore90 = int(more90data[40][1])

#  deaths
deathless90 = int(less90data[34][1])
deathmore90 = int(more90data[34][1])


#  print leavers to perm
print('Leavers to Perm:', (pdestless90+pdestmore90))

# print deaths
print('Deaths:', (deathless90+deathmore90))

#  print total clients
print('Total Clients:', clno)

#  18-24
Q11 = open('Q11.csv')
ages = csv.reader(Q11)
adata = list(ages)
youth = int(adata[4][1])
old = int(adata[9][1])

print('Total Adults:', adults)
print('62+:', old)


#  income
incomefile = open('Q18.csv')
incomereader = csv.reader(incomefile)
incomedata = list(incomereader)
earnedonly1 = int(incomedata[1][1])
earnedonly2 = int(incomedata[1][2])
earnedonly3 = int(incomedata[1][3])
employ = int(earnedonly1 + earnedonly2 + earnedonly3)
nonemploy = int(int(incomedata[2][1]) + int(incomedata[2][2]) + int(incomedata[2][3]))
both = int(int(incomedata[3][1]) + int(incomedata[3][2]) + int(incomedata[3][3]))

print('Total with Non-Employment Income:', nonemploy+both)
print('Total with Employment Income:', employ+both)
print(incomedata[7][0] + '', incomedata[7][2])

#  bennies
Q20b = open('Q20b.csv')
bennies = csv.reader(Q20b)
bdata = list(bennies)
entrybennies = int(bdata[2][1])
annualbennies = int(bdata[2][2])
exitbennies = int(bdata[2][3])
print('Households receiving mainstream benefits: ', entrybennies + annualbennies + exitbennies)

#  Bed Utilization Q3
Q7b = open('Q7b.csv')
utilization = csv.reader(Q7b)
utdata = list(utilization)
Q1 = int(utdata[1][1])
Q2 = int(utdata[2][1])
Q3 = int(utdata[3][1])
Q4 = int(utdata[4][1])
av = ((Q1 + Q2 + Q3 + Q4)/4)
ytd = ((Q1+Q2)/2)

#  using input statement from earlier to determine quarter
if quarter == 'Q1':
    quarter = Q1
elif quarter == 'Q2':
    quarter = Q2
elif quarter == 'Q3':
    quarter = Q3
elif quarter == 'Q4':
    quarter = Q4
elif quarter == 'av':
    quarter = av
elif quarter == 'ytd':
    quarter = ytd



#  Priority Populations

#  Households
Q7a = open('Q8a.csv')
total = csv.reader(Q7a)
hdata = list(total)
households = int(hdata[1][1])
print('Total Households Served:', households)

#  Print out bed utiliztion
print('This quarter there were', quarter, 'people on the night of the count.')

#  18-24
print('18-24 Served:', youth)

#  The Chronic
Q26a = open('Q26a.csv')
ch = csv.reader(Q26a)
chdata = list(ch)
chfam = int(chdata[1][1])
chron = int((clientdata[10][1]))
print('Total Households with a chronically homeless member:', chfam)

#  Families
Q8 = open('Q8a.csv')
families = csv.reader(Q8)
fdata = list(families)
hwc = int(fdata[1][3])
print('Families Served:', hwc)

#  vets
Q25a = open('Q25a.csv')
vetno = csv.reader(Q25a)
vetdata = list(vetno)
chvet = int(vetdata[1][1])
nonchvet = int(vetdata[2][1])
print('Veterans Served:', (chvet+nonchvet))

#  DV
Q14a = open('Q14a.csv')
dv = csv.reader(Q14a)
dvdata = list(dv)
dvno = int(dvdata[1][1])
print('DV Experience:', dvno)

#  Harder to serve
Q13a2 = open('Q13a2.csv')
condi = csv.reader(Q13a2)
condidata = list(condi)
threebar = int(condidata[4][1])
twobar = int(condidata[3][1])
onebar = int(condidata[2][1])
print('One or more barriers:', threebar + twobar + onebar)
print('Two or more barriers:', threebar + twobar)
print('Three or more barriers:', threebar)

#  Street Outreach elements
print("")
print('Street outreach elements:')
#   Temp exits
tempexitsless90 = int(less90data[23][1])
tempexitsmore90 = int(more90data[23][1])
print('Temporary Exits:', tempexitsless90+tempexitsmore90)

#  institutional exits
instexitsless90 = int(less90data[31][1])
instextismore90 = int(more90data[31][1])
print('Institutional Exits:', instexitsless90+instextismore90)

#  contacts
contactscsv = open('Q9a.csv')
contactsfile = csv.reader(contactscsv)
contactlist = list(contactsfile)
contacts = contactlist[5][1]
print('Total Persons Contacted:', contacts)

#  engagements
engagementscsv = open('Q9b.csv')
engagmentsfile = csv.reader(engagementscsv)
engagementslist = list(engagmentsfile)
engagements = engagementslist[5][1]
print('Total Persons Engagements:', engagements)
