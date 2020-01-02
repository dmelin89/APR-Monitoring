import pandas as pd


def main():

    #  data quality section
    dq_df = pd.read_csv('Q6a.csv')

    #  selects missing/don'tknow, not collected, and data issue fields
    MI = dq_df.iloc[:, 1:4]

    #  fills NaN with 0
    dq_df2 = MI.fillna(0)

    #  creates new column for total issues
    dq_df2['Total Issues'] = dq_df2.iloc[:, 0] + dq_df2['Information Missing'] + dq_df2['Data Issues']

    #  gets the sum of total issues for PII
    dqi = int(sum(dq_df2['Total Issues']))

    #  validation stuff
    dq_df3 = pd.read_csv('Q5a.csv')
    allclients = int(dq_df3.columns[1])
    adults = int(dq_df3.iloc[0, 1])
    minorHoH = int(dq_df3.iloc[13, 1])
    HoH = int(dq_df3.iloc[12, 1]) + minorHoH
    incexiters = int(dq_df3.iloc[5, 1])
    exiters = int(dq_df3.iloc[3, 1])
    annual = int(dq_df3.iloc[14, 1])

    # skips calculations if there are no clients
    if allclients == 0:
        print('No clients, no data quality errors.')
    elif allclients > 0:
        piirecs = (allclients * 6)

        #  DQ3: UDE
        dq_df4 = pd.read_csv('Q6b.csv')
        udeerr = int(sum(dq_df4['Error Count']))
        uderecs = (allclients * 3) + adults + HoH

        # DQ 4: Income
        dq_df5 = pd.read_csv('Q6c.csv')
        inchouserr = int(sum(dq_df5['Error Count']))
        inchouserecs = incexiters + adults + minorHoH + annual + exiters

        #  chronic homelessness
        dq_df6 = pd.read_csv('Q6d.csv')
        dq_df6.fillna(0, inplace=True)
        missingch = int(sum(dq_df6.iloc[:, 6] + dq_df6.iloc[:, 5] +
                            dq_df6.iloc[:, 4] + dq_df6.iloc[:, 3] + dq_df6.iloc[:, 2]))
        esrecs = int(dq_df6.iloc[0, 1] * 3)
        threcs = int(dq_df6.iloc[1, 1] * 5)
        phrecs = int(dq_df6.iloc[2, 1] * 5)
        allchrecs = esrecs + threcs + phrecs

        #  totes
        allerr = (dqi + udeerr + inchouserr + missingch)
        denom = (piirecs + uderecs + inchouserecs + allchrecs)
        totalissues = round(float((allerr / denom) * 100), 2)
        totalissuesstr = str(totalissues)

        print('Data Quality Issues:', totalissuesstr + '%')


