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
    Q4afile = open('Q4a.csv')
    Q4areader = csv.reader(Q4afile)
    exampledata = list(Q4areader)
    proj = str(exampledata[2][1])
    Q4afile.close()
    print('Project Name:', proj)

    #  Number of Clients

    clientcsv = open('Q5a.csv')
    clients = (csv.reader(clientcsv))
    clientdata = list(clients)
    clno = int(clientdata[0][1])
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
    Q11 = open('Q11.csv')
    ages = csv.reader(Q11)
    adata = list(ages)
    youth = int(adata[4][1])
    old = int(adata[9][1])
    Q11.close()

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
    Q20b = open('Q20b.csv')
    bennies = csv.reader(Q20b)
    bdata = list(bennies)
    entrybennies = int(bdata[2][1])
    annualbennies = int(bdata[2][2])
    exitbennies = int(bdata[2][3])
    Q20b.close()
    print('Households receiving mainstream benefits: ', entrybennies + annualbennies + exitbennies)

    #  Households
    Q7a = open('Q8a.csv')
    total = csv.reader(Q7a)
    hdata = list(total)
    households = int(hdata[1][1])
    Q7a.close()
    print('Total Households Served:', households)

    #  Bed Utilization Q3
    Q7b = open('Q7b.csv')
    utilization = csv.reader(Q7b)
    utdata = list(utilization)
    Q1 = int(utdata[1][1])
    Q2 = int(utdata[2][1])
    Q3 = int(utdata[3][1])
    Q4 = int(utdata[4][1])
    Q7b.close()

    #  Finds today's date, compares it against the most recently completed quarter

    datetoday = datetime.now()
    if datetoday > datetime.strptime('1/1/2019', '%m/%d/%Y'):
        ut = round(((Q1 + Q2 + Q3 + Q4) / 4), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('10/1/2018', '%m/%d/%Y'):
        ut = round(((Q1 + Q2 + Q3) / 3), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No clients/APR Error')
    elif datetoday > datetime.strptime('7/1/2018', '%m/%d/%Y'):
        ut = round(((Q1 + Q2) / 2), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('4/1/2018', '%m/%d/%Y'):
        print('Bed Utilization:', Q1)

    #  Priority Populations

    #  avg length to housing
    Q22cfile = open('Q22c.csv')
    Q22reader = csv.reader(Q22cfile)
    Q22data = list(Q22reader)
    hclients = str(Q22data[9][1])
    avclients = str(Q22data[10][1])
    Q22cfile.close()
    print('Clients Housed:', hclients)
    print('AVG Days to Housing:', avclients)

    #  18-24
    print('18-24 Served:', youth)

    #  The Chronic
    Q26a = open('Q26a.csv')
    ch = csv.reader(Q26a)
    chdata = list(ch)
    chfam = int(chdata[1][1])
    chron = int((clientdata[10][1]))
    Q26a.close()
    print('Total Households with a chronically homeless member:', chfam)

    #  Families
    Q8 = open('Q8a.csv')
    families = csv.reader(Q8)
    fdata = list(families)
    hwc = int(fdata[1][3])
    Q8.close()
    print('Families Served:', hwc)

    #  vets
    Q25a = open('Q25a.csv')
    vetno = csv.reader(Q25a)
    vetdata = list(vetno)
    chvet = int(vetdata[1][1])
    nonchvet = int(vetdata[2][1])
    Q25a.close()
    print('Veterans Served:', (chvet + nonchvet))

    #  DV
    Q14a = open('Q14a.csv')
    dv = csv.reader(Q14a)
    dvdata = list(dv)
    dvno = int(dvdata[1][1])
    Q14a.close()
    print('DV Experience:', dvno)

    #  Harder to serve
    Q13a2 = open('Q13a2.csv')
    condi = csv.reader(Q13a2)
    condidata = list(condi)
    threebar = int(condidata[4][1])
    twobar = int(condidata[3][1])
    onebar = int(condidata[2][1])
    Q13a2.close()

    print('One or more barriers:', threebar + twobar + onebar)
    print('Two or more barriers:', threebar + twobar)
    print('Three or more barriers:', threebar)

    # zip csv files into new folder
    newzip = zipfile.ZipFile(os.path.join(os.getcwd(), 'apr.zip'), 'w')

    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)

    for file in files:
        if file.endswith('.csv'):
            newzip.write(file)

    newzip.close()

    #  Deletes csv files
    for file in files:
        if file.endswith('.csv'):
            os.remove(file)

while True:
    main()
    if input('Restart the program? (y/n)') != 'y':
        break

input('Press "Enter" to close')
