import traceback
from submissions.FinalProject import state_crime
from submissions.FinalProject import education
from submissions.FinalProject import state_demographics

class DataFrame:
    data = []
    feature_names = []
    target = []
    target_names = []

information = DataFrame()
information.target = []
information.data = []
'''
Extract data from the CORGIS elections, and merge it with the
CORGIS demographics.  Both data sets are organized by county and state.
'''

# def infoTarget(string):
#     if (student['Education']["Bachelor's Degree or Higher"] > 50):
#         return 1
#     return 0

crime = state_crime.get_crime_by_year(2009)
education = education.get_all_states()
demographics = state_demographics.get_all_states()

joint = {}

for stateCr in crime:
    try:
        #information.target.append(alumniTarget(student['Education']["Bachelor's Degree or Higher"]))

        stCr = stateCr['State'].lower()
        propertyRate = stateCr['Data']['Rates']['Property']
        violentRate = stateCr['Data']['Rates']['Violent']
        joint[stCr] = {}
        joint[stCr]['AssaultRate'] = violentRate['Assault']
        joint[stCr]['MurderRate'] = violentRate['Murder']
        joint[stCr]['RapeRate'] = violentRate['Rape']
        joint[stCr]['RobberyRate'] = violentRate['Robbery']
        joint[stCr]['BurglaryRate'] = propertyRate['Burglary']
        joint[stCr]['LarcenyRate'] = propertyRate['Larceny']
        joint[stCr]['MotorRate'] = propertyRate['Motor']
    except:
        traceback.print_exc()

for stateEd in education:
    try:
        stEd = stateEd['state'].lower()
        funding = float(stateEd['data']['funding']['expenditures'])
        attendanceRate = float(stateEd['data']['attendance']['average student rate'])
        if stEd in joint:
            joint[stEd]['Funding'] = funding
            joint[stEd]['AttendanceRate'] = attendanceRate
    except:
        traceback.print_exc()

for stateDm in demographics:
    try:
        stDm = stateDm['State'].lower()
        educationST = stateDm['Education']
        ethnicity = stateDm['Ethnicities']
        income = stateDm['Income']
        if stDm in joint:
            joint[stDm]['BachelorsDegree'] = educationST["Bachelor's Degree or Higher"]
            joint[stDm]['GED'] = educationST["High School or Higher"]
            joint[stDm]['AmericanIndian'] = ethnicity["American Indian and Alaska Native Alone"]
            joint[stDm]['Asian'] = ethnicity['Asian Alone']
            joint[stDm]['Black'] = ethnicity['Black Alone']
            joint[stDm]['Hispanic'] = ethnicity['Hispanic or Latino']
            joint[stDm]['Hawaiian'] = ethnicity["Native Hawaiian and Other Pacific Islander Alone"]
            joint[stDm]['TwoOrMore'] = ethnicity['Two or More Races']
            joint[stDm]['White'] = ethnicity['White Alone']
            joint[stDm]['HouseholdIncome'] = income['Median Houseold Income']
            joint[stDm]['Poverty'] = income['Persons Below Poverty Level']
    except:
        traceback.print_exc()


intersection = {}
for state in joint:
    if 'Poverty' in joint[state] and 'Funding' in joint[state]:
        intersection[state] = joint[state]



def murderTarget(rate):
    if rate >= 7:
        return 1
    return 0

'''
Build the input frame, row by row.
'''
for stateFN in intersection:
    # choose the input values
    information.data.append([
        intersection[stateFN]['GED'],
        intersection[stateFN]['HouseholdIncome'],
        intersection[stateFN]['Poverty'],
    ])

for stateMR in intersection:
    # choose the target
    mr = murderTarget(intersection[stateMR]['MurderRate'])
    information.target.append(mr)


information.feature_names = [
    "High School or Higher Education",
    "Average Household Income",
    "Poverty Rate"
]

information.target_names = [
    '>= 7 Murder Rate',
    'Below 7 Murder Rate',
]

Examples = {
    'Murder Rate by Income and Highest Education': information,
}