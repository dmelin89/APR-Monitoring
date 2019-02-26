#  Updated for 2018 APRs to include housing move in dates
import zipfile
import csv
from tkinter import *
from tkinter import filedialog
from datetime import datetime
import os


def main():
    print('')
    print('')
    root = Tk()
    root.withdraw()

    #  uses zipfile to extract APR to CWD
    apr = zipfile.ZipFile(filedialog.askopenfilename())
    apr.extractall()

    root.quit()

    #  prints the project name
    q4afile = open('Q4a.csv')
    q4areader = csv.reader(q4afile)
    exampledata = list(q4areader)
    proj = str(exampledata[2][1])
    q4afile.close()
    print('Project Name:', proj)

    #  Number of Clients

    clientcsv = open('Q5a.csv')
    clients = (csv.reader(clientcsv))
    clientdata = list(clients)
    clno = int(clientdata[0][1])
    stayers = int(clientdata[7][1])
    clientcsv.close()

    #  turn clients, adults, and leavers into integers

    print('Total number of clients: ', clno)

    leavers = int((clientdata[4][1]))
    adults = int((clientdata[1][1]))

    #  Number of Stayers
    print('Number of Stayers: ', clno - leavers)

    #  destinations

    #  less than 90 days
    fulldestless90 = open('Q23b.csv')
    fulldestlessread = csv.reader(fulldestless90)
    less90data = list(fulldestlessread)

    #  more than 90 days
    fulldestmore90 = (open('q23a.csv'))
    fulldestmoreread = csv.reader(fulldestmore90)
    more90data = list(fulldestmoreread)
    fulldestless90.close()
    fulldestmore90.close()

    # finds permanent destinations and converts into integer
    pdestless90 = int(less90data[40][1])
    pdestmore90 = int(more90data[40][1])

    #  deaths
    deathless90 = int(less90data[34][1])
    deathmore90 = int(more90data[34][1])

    #  print leavers to perm
    print('Leavers to Perm:', (pdestless90 + pdestmore90))

    # print deaths
    print('Deaths:', (deathless90 + deathmore90))

    #  print total clients
    print('Total Clients:', clno)

    #  18-24
    q11 = open('Q11.csv')
    ages = csv.reader(q11)
    adata = list(ages)
    youth = int(adata[4][1])
    old = int(adata[9][1])
    q11.close()

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
    incomefile.close()
    print('Total with Non-Employment Income:', nonemploy + both)
    print('Total with Employment Income:', employ + both)
    print(incomedata[7][0] + '', incomedata[7][2])

    #  bennies
    q20b = open('Q20b.csv')
    bennies = csv.reader(q20b)
    bdata = list(bennies)
    entrybennies = int(bdata[2][1])
    annualbennies = int(bdata[2][2])
    exitbennies = int(bdata[2][3])
    q20b.close()
    print('Households receiving mainstream benefits: ', entrybennies + annualbennies + exitbennies)

    #  Households
    q7a = open('Q8a.csv')
    total = csv.reader(q7a)
    hdata = list(total)
    households = int(hdata[1][1])
    q7a.close()
    print('Total Households Served:', households)

    #  Bed Utilization Q3
    q7b = open('Q7b.csv')
    utilization = csv.reader(q7b)
    utdata = list(utilization)
    q1 = int(utdata[1][1])
    q2 = int(utdata[2][1])
    q3 = int(utdata[3][1])
    q4 = int(utdata[4][1])
    q7b.close()

    #  Finds today's date, compares it against the most recently completed quarter

    datetoday = datetime.now()
    if datetoday > datetime.strptime('1/1/2020', '%m/%d/%Y'):
        ut = round(((q1 + q2 + q3 + q4) / 4), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('10/1/2019', '%m/%d/%Y'):
        ut = round(((q1 + q2 + q3) / 3), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No clients/APR Error')
    elif datetoday > datetime.strptime('7/1/2019', '%m/%d/%Y'):
        ut = round(((q1 + q2) / 2), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('4/1/2019', '%m/%d/%Y'):
        print('Bed Utilization:', q1)

    #  Priority Populations

    #  avg length to housing
    q22cfile = open('Q22c.csv')
    q22reader = csv.reader(q22cfile)
    q22data = list(q22reader)
    hclients = str(q22data[9][1])
    avclients = str(q22data[10][1])
    q22cfile.close()
    print('Clients Housed:', hclients)
    print('AVG Days to Housing:', avclients)

    #  18-24
    print('18-24 Served:', youth)

    #  The Chronic
    q26a = open('Q26a.csv')
    ch = csv.reader(q26a)
    chdata = list(ch)
    chfam = int(chdata[1][1])
    chron = int((clientdata[10][1]))
    q26a.close()
    print('Total Households with a chronically homeless member:', chfam)

    #  Families
    q8 = open('Q8a.csv')
    families = csv.reader(q8)
    fdata = list(families)
    hwc = int(fdata[1][3])
    q8.close()
    print('Families Served:', hwc)

    #  vets
    q25a = open('Q25a.csv')
    vetno = csv.reader(q25a)
    vetdata = list(vetno)
    chvet = int(vetdata[1][1])
    nonchvet = int(vetdata[2][1])
    q25a.close()
    print('Veterans Served:', (chvet + nonchvet))

    #  DV
    q14a = open('Q14a.csv')
    dv = csv.reader(q14a)
    dvdata = list(dv)
    dvno = int(dvdata[1][1])
    q14a.close()
    print('DV Experience:', dvno)

    #  Harder to serve
    q13a2 = open('Q13a2.csv')
    condi = csv.reader(q13a2)
    condidata = list(condi)
    threebar = int(condidata[4][1])
    twobar = int(condidata[3][1])
    onebar = int(condidata[2][1])
    q13a2.close()

    print('One or more barriers:', threebar + twobar + onebar)
    print('Two or more barriers:', threebar + twobar)
    print('Three or more barriers:', threebar)

    #  Street Outreach elements
    print("")
    print('Street outreach elements:')
    #   Temp exits
    tempexitsless90 = int(less90data[23][1])
    tempexitsmore90 = int(more90data[23][1])
    print('Temporary Exits:', tempexitsless90 + tempexitsmore90)

    #  institutional exits
    instexitsless90 = int(less90data[31][1])
    instextismore90 = int(more90data[31][1])
    print('Institutional Exits:', instexitsless90 + instextismore90)

    #  contacts
    contactscsv = open('Q9a.csv')
    contactsfile = csv.reader(contactscsv)
    contactlist = list(contactsfile)
    contacts = contactlist[5][1]
    contactscsv.close()
    print('Total Persons Contacted:', contacts)

    #  engagements
    engagementscsv = open('Q9b.csv')
    engagmentsfile = csv.reader(engagementscsv)
    engagementslist = list(engagmentsfile)
    engagements = engagementslist[5][1]
    engagementscsv.close()
    print('Total Persons Engagements:', engagements)

    #  avg length of stay
    avgcsv = open('Q22b.csv')
    avgfile = csv.reader(avgcsv)
    avglist = list(avgfile)
    stay_avg = int(avglist[1][2])
    leav_avg = int(avglist[1][1])
    avgcsv.close()
    stay_days = (stay_avg * stayers)
    leav_days = (leav_avg * leavers)
    avgdays = round(((stay_days + leav_days) / clno), 2)
    print('')
    print('Average Days Enrolled:', avgdays, 'Days')
    print('stayers:', stayers, 'staydays', stay_days, 'average', stay_avg)
    print('leavers', leavers, 'leavdays', leav_days, 'average', leav_avg)

    #  zip csv files into new folder
    newzip = zipfile.ZipFile(os.path.join(os.getcwd(), 'apr.zip'), 'w')

    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)

    for file in files:
        if file.endswith('.csv'):
            newzip.write(file)

    newzip.close()

    #  renames zipfile with project name from Q4a
    newname = proj+str('.zip')
    os.replace('apr.zip', newname)

    #  Deletes csv files
    for file in files:
        if file.endswith('.csv'):
            os.remove(file)


while True:
    main()
    if input('Restart the program? (y/n)') != 'y':
        break

input('Press "Enter" to close')
