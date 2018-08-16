import pandas as pd

df = pd.read_csv('Q6a.csv')

#  selects missing/don'tknow, not collected, and data issue fields
MI = df.iloc[:, 1:4]

#  fills NaN with 0
df2 = MI.fillna(0)

#  creates new column for total issues
df2['Total Issues'] = df2.iloc[:, 0] + df2['Information Missing'] + df2['Data Issues']

#  gets the sum of total issues for PII
dqi = int(sum(df2['Total Issues']))

#  validation stuff
df2 = pd.read_csv('Q5a.csv')
allclients = int(df2.columns[1])
adults = int(df2.iloc[0, 1])
minorHoH = int(df2.iloc[13, 1])
HoH = int(df2.iloc[12, 1]) + minorHoH
incexiters = int(df2.iloc[5, 1])
exiters = int(df2.iloc[3, 1])
annual = int(df2.iloc[14, 1])


#  round to two decimal points
issues = round(float((dqi / (allclients * 6)) * 100), 2)
print('PPI:', issues, '% data quality issues')

#  DQ3: UDE
df3 = pd.read_csv('Q6b.csv')
udeerr = int(sum(df3['Error Count']))
uderecs = (allclients * 3) + adults + HoH
udeissues = round(float((udeerr / uderecs) * 100), 2)
print('UDE:', udeissues, '% data quality issues')

df4 = pd.read_csv('Q6c.csv')
inchouserr = int(sum(df4['Error Count']))
inchouserecs = incexiters + adults + minorHoH + annual + exiters
incissues = round(float((inchouserr / inchouserecs) * 100), 2)
print('Income and Housing:', incissues, '% data quality issues')

#  chronic homelessness
df5 = pd.read_csv('Q6d.csv')
chrecstotal = int(df5.iloc[3, 1])
df5.fillna(0, inplace=True)
missingCH = int(sum(df5.iloc[:, 6] + df5.iloc[:, 5] + df5.iloc[:, 4] + df5.iloc[:, 3] + df5.iloc[:, 2]))
esrecs = int(df5.iloc[0, 1] * 3)
threcs = int(df5.iloc[1, 1] * 5)
phrecs = int(df5.iloc[2, 3] * 5)
allchrecs = esrecs + threcs + phrecs
if allchrecs == 0:
    print('No Records for Q6d.csv')
elif allchrecs != 0:
    CHissues = round(float((missingCH / allchrecs)), 2)
    print('3.917:', CHissues, '% data quality issues')

#  totes
allerr = (dqi + udeerr + inchouserr + missingCH)
denom = (uderecs + inchouserecs + allchrecs) + (allclients * 6)
totalissues = round(float((allerr / denom) * 100), 2)

print("")
print(allerr, 'Total data errors', 'Out of', denom, 'Total Records')
print('Total Percent Missing:', totalissues, '% data quality issues')
