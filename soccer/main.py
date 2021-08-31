from match import Match
from team import Team

team_1 = Team("el colo", "Santiago", "blanco")
team_2 = Team("la chile", "Santiago", "azul")
match = Match(team_1, team_2)
print(match)
print(match.team_1)
print(match.team_2)
print(match.day)
match.print_scores()
match.day = "Hoydía"
match.goal(team_1)
match.print_scores()