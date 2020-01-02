import zipfile
from tkinter import Tk
from tkinter import filedialog
from datetime import datetime
import os
import pandas as pd
import dq_calc


def main():
    root = Tk()
    root.withdraw()

    #  uses zipfile to extract APR to

    apr = zipfile.ZipFile(filedialog.askopenfilename())
    root.quit()
    apr.extractall()

    #  project info
    q4a = pd.read_csv('Q4a.csv')
    proj = q4a.iloc[0, 2]
    ptype = q4a.iloc[0, 4]
    org = q4a.iloc[0, 0]

    #  clients
    q5a = pd.read_csv('Q5a.csv', header=None)
    client_text = q5a.iloc[0, 0]
    clients = q5a.iloc[0, 1]
    stayers_text = q5a.iloc[7, 0]
    stayers = q5a.iloc[7, 1]

    # exits
    q23c = pd.read_csv('Q23c.csv')
    perm_text = q23c.iloc[42, 0]
    perm = int(q23c.iloc[42, 1])
    excluded_text = q23c.iloc[43, 0]
    excluded = int(q23c.iloc[43, 1])
    temp_exits = int(q23c.iloc[25, 1])
    institutional_exits = int(q23c.iloc[33, 1])
    all_exits = int(q23c.iloc[41, 1])
    deaths = int(q23c.iloc[36, 1])

    # ages
    q11 = pd.read_csv('Q11.csv')
    senior_text = q11.iloc[8, 0]
    senior_number = q11.iloc[8, 1]
    youth = q11.iloc[3, 1]

    # Employment/Earned income
    q19a1 = pd.read_csv('Q19a1.csv')
    stayer_income_adults = int(q19a1.iloc[0, 7])
    stayer_earned = (int(q19a1.iloc[0, 3]) + int(q19a1.iloc[0, 4]) + int(q19a1.iloc[0, 5]))
    stayer_non_employment = (int(q19a1.iloc[2, 3]) + int(q19a1.iloc[2, 4]) + int(q19a1.iloc[2, 5]))

    q19a2 = pd.read_csv('Q19a2.csv')
    leaver_income_adults = int(q19a2.iloc[0, 7])
    leaver_earned = (int(q19a2.iloc[0, 3]) + int(q19a2.iloc[0, 4]) + int(q19a2.iloc[0, 5]))
    leaver_non_employment = (int(q19a2.iloc[2, 3]) + int(q19a2.iloc[2, 4]) + int(q19a2.iloc[2, 5]))

    # benefits
    q20b = pd.read_csv('Q20b.csv')
    benefits = (q20b.iloc[1, 1] + q20b.iloc[1, 2] + q20b.iloc[1, 3])

    # households
    q8a = pd.read_csv('Q8a.csv')
    households = q8a.iloc[0, 1]
    families = q8a.iloc[0, 3]

    # bed utilization
    q7b = pd.read_csv('Q7b.csv')
    q1 = q7b.iloc[0, 1]
    q2 = q7b.iloc[1, 1]
    q3 = q7b.iloc[2, 1]
    q4 = q7b.iloc[3, 1]

    # finds the date, calculates bed utilization
    datetoday = datetime.now()
    if datetoday > datetime.strptime('1/1/2020', '%m/%d/%Y'):
        ut = round(((q1 + q2 + q3 + q4) / 4), 2)
        if ut == 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('10/1/2020', '%m/%d/%Y'):
        ut = round(((q1 + q2 + q3) / 3), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No clients/APR Error')
    elif datetoday > datetime.strptime('7/1/2020', '%m/%d/%Y'):
        ut = round(((q1 + q2) / 2), 2)
        if ut != 0:
            print('Bed Utilization:', ut)
        elif ut == 0:
            print('No Clients/APR Error')
    elif datetoday > datetime.strptime('4/1/2020', '%m/%d/%Y'):
        print('Bed Utilization:', q1)

    # Priority populations
    # chronic
    q26a = pd.read_csv('Q26a.csv')
    chronic = q26a.iloc[0, 1]

    # vets
    q25a = pd.read_csv('Q25a.csv')
    vets = (q25a.iloc[1, 1] + q25a.iloc[2, 1])

    # DV
    q14a = pd.read_csv('Q14a.csv')
    dv = q14a.iloc[0, 1]

    # harder to serve
    q13a2 = pd.read_csv('Q13a2.csv')
    one_condition = q13a2.iloc[1, 1]
    two_condition = q13a2.iloc[2, 1]
    three_condition = q13a2.iloc[3, 1]

    print('')

    if ptype in [1, 2, 8]:
        print('Project Name:', proj)
        print('exits', all_exits)
        print(perm_text + ':', perm)
        print('Deaths: ', deaths)
        Q22b = pd.read_csv('Q22b.csv')
        leaver_avg_length = Q22b.iloc[0, 1]
        stayer_avg_length = Q22b.iloc[0, 2]
        avg_time = (((all_exits * leaver_avg_length) + (stayer_avg_length * stayers)) / clients)
        print('Average length of stay: ', avg_time)
        dq_calc.main()
    elif ptype == 12:
        print('Project Name:', proj)
        print('Exits: ', all_exits)
        print('Maintain or exits to PH:', (stayers + perm))
        print('Non-Employment Income:', (stayer_non_employment + leaver_non_employment))
        print('Emploment Income:', (stayer_earned + leaver_earned))
        print('Q19 adults', (stayer_income_adults + leaver_income_adults))
        print(senior_text + ':', senior_number)
        print('Deaths:', deaths)
        dq_calc.main()
    elif ptype == 4:
        print('Project Name:', proj)
        print('Exits: ', all_exits)
        print(perm_text + ':', perm)
        print('Exits to Temporary Destinations:', temp_exits)
        print('Exits to Institutional Destinations:', institutional_exits)
        q9b = pd.read_csv('Q9b.csv')
        engaged = int(q9b.iloc[4, 1])
        print('Clients Engaged:', engaged)
        print('Deaths:', deaths)
        dq_calc.main()
    elif ptype in [3, 6, 7, 9, 10, 11, 13, 14]:
        print('Project Name:', proj)
        print(stayers_text + ':', stayers)
        print(perm_text + ':', perm)
        print(excluded_text + ':', excluded)
        print(client_text + ':', clients)
        print('Adults in Q19', (stayer_income_adults + leaver_income_adults))
        print(senior_text + ':', senior_number)
        print('Non-Employment Income:', (stayer_non_employment + leaver_non_employment))
        print('Employment Income:', (stayer_earned + leaver_earned))
        print('Households receiving mainstream benefits:', benefits)
        print('Total Households Served:', households)
        # finds the date, calculates bed utilization
        datetoday = datetime.now()
        if datetoday > datetime.strptime('1/1/2020', '%m/%d/%Y'):
            ut = round(((q1 + q2 + q3 + q4) / 4), 2)
            if ut == 0:
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
        print('18-24 Served:', youth)
        print('Chronically Homeless:', chronic)
        print('Families:', families)
        print('Vets:', vets)
        print('DV Experience:', dv)
        print('One or more barriers:', one_condition + two_condition + three_condition)
        print('Two or more barriers:', two_condition + three_condition)
        print('Three or more barriers:', three_condition)
        dq_calc.main()

    newzip = zipfile.ZipFile(os.path.join(os.getcwd(), 'apr.zip'), 'w')

    path = os.getcwd()
    os.sys.path.append(path)
    files = os.listdir(path)

    for file in files:
        if file.endswith('.csv'):
            newzip.write(file)

    newzip.close()

    #  renames zipfile with project name from Q4a
    newname = org + '' + proj + str('.zip')
    os.replace('apr.zip', newname)

    #  Deletes csv files
    for file in files:
        if file.endswith('.csv'):
            os.remove(file)


while True:
    main()
    if input('Restart the program? (y/n)') != 'y':
        break
