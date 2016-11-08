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

def infoTarget(string):
    if (student['Education']["Bachelor's Degree or Higher"] > 50):
        return 1
    return 0

crime = state_crime.get_crime_by_year(2009)
education = education.get_all_states()
demographics = state_demographics.get_all_states()

joint = {}

for state in crime:
    try:
        #information.target.append(alumniTarget(student['Education']["Bachelor's Degree or Higher"]))

        st = state['State'].lower()
        propertyRate = state['Data']['Rates']['Property']
        violentRate = state['Data']['Rates']['Violent']
        joint[st]['AssaultRate'] = violentRate['Assault']
        joint[st]['MurderRate'] = violentRate['Murder']
        joint[st]['RapeRate'] = violentRate['Rape']
        joint[st]['RobberyRate'] = violentRate['Robbery']
        joint[st]['BurglaryRate'] = propertyRate['Burglary']
        joint[st]['LarcenyRate'] = propertyRate['Larceny']
        joint[st]['MotorRate'] = propertyRate['Motor']
    except:
        traceback.print_exc()

for state in education:
    try:
        st = state['State'].lower()
        funding = float(state['data']['funding']['expenditures'])
        attendanceRate = float(state['data']['attendance']['average student rate'])
        joint[st]['Funding'] = funding
        joint[st]['AttendanceRate'] = attendanceRate
    except:
        traceback.print_exc()

for state in demographics:
    try:
        st = state['State'].lower()
        educationST = state['Education']
        ethnicity = state['Ethnicities']
        income = state['Income']
        joint[st]['BachelorsDegree'] = educationST["Bachelor's Degree or Higher"]
        joint[st]['GED'] = educationST["High School or Higher"]
        joint[st]['AmericanIndian'] = ethnicity["American Indian and Alaska Native Alone"]
        joint[st]['Asian'] = ethnicity['Asian Alone']
        joint[st]['Black'] = ethnicity['Black Alone']
        joint[st]['Hispanic'] = ethnicity['Hispanic or Latino']
        joint[st]['Hawaiian'] = ethnicity["Native Hawaiian and Other Pacific Islander Alone"]
        joint[st]['TwoOrMore'] = ethnicity['Two or More Races']
        joint[st]['White'] = ethnicity['White Alone']
        joint[st]['HouseholdIncome'] = income['Median Houseold Income']
        joint[st]['Poverty'] = income['Persons Below Poverty Level']
    except:
        traceback.print_exc()

alumni.feature_names = [
    "Bachelor's Degree or Higher",
    "Persons Below Poverty Level",
]

alumni.target_names = [
    'Most Do Not Have Degree',
    'Most Have Degree',
]

Examples = {
    'Poor with degree': alumni,
}