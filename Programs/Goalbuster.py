import random, time, calendar
import pandas as pd

random.seed( calendar.timegm( time.gmtime() ) )

lListOfPeople = [
    "Adam Miritis",
    "Andrew Burke",
    "Andy Bates",
    "Anthony Marney",
    "Brent Turner",
    "Carlo Dalla-Valle",
    "Clifford Lobb",
    "Dan Thorne",
    "Gavin Hingert",
    "Jaydip Patel",
    "Jim Georgiou",
    "Jocky Clelland",
    "Keith Todd",
    "Luke Mitchell",
    "MCSC",
    "Noel Mitchell",
    "Paul Hatch",
    "Russ Saunders",
    "Steve Nichols",
    "Tim Floyd"
]

lTeams = [
    "AFC Bournemouth",
    "Arsenal",
    "Aston Villa",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Norwich",
    "Sheffield United",
    "Southampton",
    "Tottenham Hotspur",
    "Watford",
    "West Ham United",
    "Wolverhampton Wanderers"
]

random.shuffle( lListOfPeople )
random.shuffle( lTeams )

lResults = pd.DataFrame(
    {
        'Name': lListOfPeople,
        'Team': lTeams
    }
)


lResults.to_csv( "Table" + ".csv" )
