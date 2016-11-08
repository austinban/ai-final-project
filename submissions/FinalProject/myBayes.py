import traceback
from submissions.FinalProject import state_crime
from submissions.FinalProject import education
from submissions.FinalProject import

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

def alumniTarget(string):
    if (student['Education']["Bachelor's Degree or Higher"] > 50):
        return 1
    return 0

crime = state_crime.get_crime_by_year(2009)
education = education.get_all_states()

for state in crime:
    try:
        alumni.target.append(alumniTarget(student['Education']["Bachelor's Degree or Higher"]))

        college = float(student['Education']["Bachelor's Degree or Higher"])
        poverty = float(student['Income']["Persons Below Poverty Level"])

        alumni.data.append([college, poverty])
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