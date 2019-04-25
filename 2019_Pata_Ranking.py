import zipfile
import csv
from tkinter import *
from tkinter import filedialog
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
    clientcsv.close()

    #  turn clients, adults, and leavers into integers

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
    excludedless90 = int(less90data[41][1])
    excludedmore90 = int(more90data[41][1])

    #  print leavers to perm
    print('Leavers to Perm:', (pdestless90 + pdestmore90))

    # print deaths
    print('Excluded Destinations:', (excludedless90 + excludedmore90))

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
    incomefile = open('Q19.csv')
    incomereader = csv.reader(incomefile)
    incomedata = list(incomereader)
    earned_maintained = int(incomedata[1][3])
    earned_increased = int(incomedata[1][4])
    employ = earned_maintained + earned_increased
    nonemploy = (int(incomedata[3][3]) + int(incomedata[3][4]))
    incomefile.close()
    print('Total with Non-Employment Income:', nonemploy)
    print('Total with Employment Income:', employ)

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
    qtotal = (q1 + q2 + q3 + q4)
    q7b.close()
    print('Bed Utilization: ', round((qtotal / 4), 2))

    #  Priority Populations
    #  18-24
    print('18-24 Served:', youth)

    #  The Chronic
    q26a = open('Q26a.csv')
    ch = csv.reader(q26a)
    chdata = list(ch)
    chfam = int(chdata[1][1])
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
