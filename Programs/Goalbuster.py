import random, time, calendar
import pandas as pd

random.seed( calendar.timegm( time.gmtime() ) )

lListOfPeople = [
    "Alex Burrows",
    "Andy Bates",
    "Anthony Marney",
    "Carlo Dalla-Valle",
    "Clifford Lobb",
    "Dan Thorne",
    "Gavin Hingert",
    "Jaydip Patel",
    "Jim Georgiou",
    "Keith Todd",
    "Kunal Sondhi",
    "Luke Mitchell",
    "Lydia Payne",
    "Matt Day",
    "Matt Paterson",
    "MCSC",
    "Noel",
    "Paul",
    "Rocco Caia",
    "Tim Floyd"
]

lTeams = [
    "AFC Bournemouth",
    "Arsenal",
    "Brighton & Hove Albion",
    "Burnley",
    "Cardiff",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Huddersfield Town",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
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
