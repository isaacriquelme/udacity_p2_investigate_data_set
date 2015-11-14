import unicodecsv
from datetime import datetime as dt
from decimal import *


def read_csv_from_file(path):
    with open (path, "rb") as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

all_stars = read_csv_from_file("../dataset/lahman-csv_2015-01-24/AllstarFull.csv")
appearances = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Appearances.csv")
awards_managers = read_csv_from_file("../dataset/lahman-csv_2015-01-24/AwardsManagers.csv")
awards_players = read_csv_from_file("../dataset/lahman-csv_2015-01-24/AwardsPlayers.csv")
awards_share_managers = read_csv_from_file("../dataset/lahman-csv_2015-01-24/AwardsShareManagers.csv")
awards_share_players = read_csv_from_file("../dataset/lahman-csv_2015-01-24/AwardsSharePlayers.csv")
batting = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Batting.csv")
batting_post = read_csv_from_file("../dataset/lahman-csv_2015-01-24/BattingPost.csv")
college_playing = read_csv_from_file("../dataset/lahman-csv_2015-01-24/CollegePlaying.csv")
fielding = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Fielding.csv")
fielding_OF = read_csv_from_file("../dataset/lahman-csv_2015-01-24/FieldingOF.csv")
fielding_post = read_csv_from_file("../dataset/lahman-csv_2015-01-24/FieldingPost.csv")
hall_of_fame = read_csv_from_file("../dataset/lahman-csv_2015-01-24/HallOfFame.csv")
managers = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Managers.csv")
managers_half = read_csv_from_file("../dataset/lahman-csv_2015-01-24/ManagersHalf.csv")
master = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Master.csv")
pitching = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Pitching.csv")
pitching_post = read_csv_from_file("../dataset/lahman-csv_2015-01-24/PitchingPost.csv")
salaries = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Salaries.csv")
schools = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Schools.csv")
series_post = read_csv_from_file("../dataset/lahman-csv_2015-01-24/SeriesPost.csv")
teams = read_csv_from_file("../dataset/lahman-csv_2015-01-24/Teams.csv")
teams_franchises = read_csv_from_file("../dataset/lahman-csv_2015-01-24/TeamsFranchises.csv")
teams_half = read_csv_from_file("../dataset/lahman-csv_2015-01-24/TeamsHalf.csv")


def parse_date(date_string):
    if date_string == '':
        return None
    else:
        if'-' in date_string:
            return dt.strptime(date_string, '%Y-%m-%d')
        elif '/' in date_string:
            return dt.strptime(date_string, '%m/%d/%Y')
        else:
            return None


def parse_int(int_string):
    if (int_string == '') | (int_string is None):
        return None
    else:
        return int(int_string)


def parse_decimal(double_string):
    if (double_string == '') | (double_string is None):
        return None
    else:
        return Decimal(double_string)


for all_start in all_stars:
    all_start['yearID'] = parse_int(all_start['yearID'])
    all_start['gameNum'] = parse_int(all_start['gameNum'])
    all_start['startingPos'] = parse_int(all_start['startingPos'])
    all_start['GP'] = parse_int(all_start['GP'])


print 'all_stars Count = ' + str(len(all_stars))


for appearance in appearances:
    appearance['G_3b'] = parse_int(appearance['G_3b'])
    appearance['G_2b'] = parse_int(appearance['G_2b'])
    appearance['GS'] = parse_int(appearance['GS'])
    appearance['G_ph'] = parse_int(appearance['G_ph'])
    appearance['G_rf'] = parse_int(appearance['G_rf'])
    appearance['G_batting'] = parse_int(appearance['G_batting'])
    appearance['G_1b'] = parse_int(appearance['G_1b'])
    appearance['G_p'] = parse_int(appearance['G_p'])
    appearance['G_ss'] = parse_int(appearance['G_ss'])
    appearance['G_of'] = parse_int(appearance['G_of'])
    appearance['yearID'] = parse_int(appearance['yearID'])
    appearance['G_lf'] = parse_int(appearance['G_lf'])
    appearance['G_cf'] = parse_int(appearance['G_cf'])
    appearance['G_defense'] = parse_int(appearance['G_defense'])
    appearance['G_all'] = parse_int(appearance['G_all'])
    appearance['G_dh'] = parse_int(appearance['G_dh'])
    appearance['G_pr'] = parse_int(appearance['G_pr'])
    appearance['G_c'] = parse_int(appearance['G_c'])


print 'appearances Count = ' + str(len(appearances))


for award_managers in awards_managers:
    award_managers['yearID'] = parse_int(award_managers['yearID'])


print 'awards_managers Count = ' + str(len(awards_managers))


for awards_player in awards_players:
    awards_player['yearID'] = parse_int(awards_player['yearID'])


print 'awards_player Count = ' + str(len(awards_players))


for awards_share_manager in awards_share_managers:
    awards_share_manager['yearID'] = parse_int(awards_share_manager['yearID'])
    awards_share_manager['votesFirst'] = parse_int(awards_share_manager['votesFirst'])
    awards_share_manager['pointsWon'] = parse_int(awards_share_manager['pointsWon'])
    awards_share_manager['pointsMax'] = parse_int(awards_share_manager['pointsMax'])


print 'awards_share_managers Count = ' + str(len(awards_share_managers))


for awards_share_player in awards_share_players:
    awards_share_player['yearID'] = parse_int(awards_share_player['yearID'])
    awards_share_player['votesFirst'] = parse_decimal(awards_share_player['votesFirst'])
    awards_share_player['pointsWon'] = parse_decimal(awards_share_player['pointsWon'])
    awards_share_player['pointsMax'] = parse_decimal(awards_share_player['pointsMax'])


print 'awards_share_players Count = ' + str(len(awards_share_players))


for bat in batting:
    bat['yearID'] = parse_int(bat['yearID'])
    bat['2B'] = parse_int(bat['2B'])
    bat['BB'] = parse_int(bat['BB'])
    bat['HR'] = parse_int(bat['HR'])
    bat['IBB'] = parse_int(bat['IBB'])
    bat['3B'] = parse_int(bat['3B'])
    bat['HBP'] = parse_int(bat['HBP'])
    bat['GIDP'] = parse_int(bat['GIDP'])
    bat['stint'] = parse_int(bat['stint'])
    bat['AB'] = parse_int(bat['AB'])
    bat['G'] = parse_int(bat['G'])
    bat['H'] = parse_int(bat['H'])
    bat['R'] = parse_int(bat['R'])
    bat['RBI'] = parse_int(bat['RBI'])
    bat['CS'] = parse_int(bat['CS'])
    bat['SH'] = parse_int(bat['SH'])
    bat['SO'] = parse_int(bat['SO'])
    bat['SB'] = parse_int(bat['SB'])
    bat['SF'] = parse_int(bat['SF'])


print 'batting Count = ' + str(len(batting))


for bat in batting_post:
    bat['yearID'] = parse_int(bat['yearID'])
    bat['2B'] = parse_int(bat['2B'])
    bat['BB'] = parse_int(bat['BB'])
    bat['HR'] = parse_int(bat['HR'])
    bat['IBB'] = parse_int(bat['IBB'])
    bat['3B'] = parse_int(bat['3B'])
    bat['HBP'] = parse_int(bat['HBP'])
    bat['GIDP'] = parse_int(bat['GIDP'])
    bat['AB'] = parse_int(bat['AB'])
    bat['AB'] = parse_int(bat['AB'])
    bat['H'] = parse_int(bat['H'])
    bat['R'] = parse_int(bat['R'])
    bat['RBI'] = parse_int(bat['RBI'])
    bat['CS'] = parse_int(bat['CS'])
    bat['SH'] = parse_int(bat['SH'])
    bat['SO'] = parse_int(bat['SO'])
    bat['SB'] = parse_int(bat['SB'])
    bat['SF'] = parse_int(bat['SF'])


print 'batting_post Count = ' + str(len(batting_post))


for college in college_playing:
    college['yearID'] = parse_int(college['yearID'])


print 'college_playing Count = ' + str(len(college_playing))


for field in fielding:
    field['yearID'] = parse_int(field['yearID'])
    field['A'] = parse_int(field['A'])
    field['GS'] = parse_int(field['GS'])
    field['G'] = parse_int(field['G'])
    field['PO'] = parse_int(field['PO'])
    field['PB'] = parse_int(field['PB'])
    field['InnOuts'] = parse_int(field['InnOuts'])
    field['ZR'] = parse_int(field['ZR'])
    field['WP'] = parse_int(field['WP'])
    field['CS'] = parse_int(field['CS'])
    field['E'] = parse_int(field['E'])
    field['stint'] = parse_int(field['stint'])
    field['DP'] = parse_int(field['DP'])
    field['SB'] = parse_int(field['SB'])


print 'fielding Count = ' + str(len(fielding))


for field in fielding_OF:
    field['yearID'] = parse_int(field['yearID'])
    field['Gcf'] = parse_int(field['Gcf'])
    field['Glf'] = parse_int(field['Glf'])
    field['Grf'] = parse_int(field['Grf'])
    field['stint'] = parse_int(field['stint'])


print 'fielding_OF Count = ' + str(len(fielding_OF))


for field in fielding_post:
    field['yearID'] = parse_int(field['yearID'])
    field['A'] = parse_int(field['A'])
    field['GS'] = parse_int(field['GS'])
    field['G'] = parse_int(field['G'])
    field['TP'] = parse_int(field['TP'])
    field['PB'] = parse_int(field['PB'])
    field['InnOuts'] = parse_int(field['InnOuts'])
    field['PO'] = parse_int(field['PO'])
    field['SB'] = parse_int(field['SB'])
    field['CS'] = parse_int(field['CS'])
    field['E'] = parse_int(field['E'])
    field['DP'] = parse_int(field['DP'])


print 'fielding_post Count = ' + str(len(fielding_post))


for fame in hall_of_fame:
    fame['yearid'] = parse_int(fame['yearid'])
    fame['votes'] = parse_int(fame['votes'])
    fame['needed'] = parse_int(fame['needed'])
    fame['ballots'] = parse_int(fame['ballots'])


print 'hall_of_fame Count = ' + str(len(hall_of_fame))


for manager in managers:
    manager['yearID'] = parse_int(manager['yearID'])
    manager['W'] = parse_int(manager['W'])
    manager['G'] = parse_int(manager['G'])
    manager['rank'] = parse_int(manager['rank'])
    manager['L'] = parse_int(manager['L'])
    manager['inseason'] = parse_int(manager['inseason'])


print 'managers Count = ' + str(len(managers))


for manager in managers_half:
    manager['yearID'] = parse_int(manager['yearID'])
    manager['W'] = parse_int(manager['W'])
    manager['G'] = parse_int(manager['G'])
    manager['rank'] = parse_int(manager['rank'])
    manager['L'] = parse_int(manager['L'])
    manager['inseason'] = parse_int(manager['inseason'])


print 'managers_half Count = ' + str(len(managers_half))


for mas in master:
    mas['weight'] = parse_int(mas['weight'])
    mas['height'] = parse_int(mas['height'])
    mas['birthMonth'] = parse_int(mas['birthMonth'])
    mas['deathMonth'] = parse_int(mas['deathMonth'])
    mas['deathYear'] = parse_int(mas['deathYear'])
    mas['birthYear'] = parse_int(mas['birthYear'])
    mas['finalGame'] = parse_date(mas['finalGame'])
    mas['debut'] = parse_date(mas['debut'])
    mas['birthDay'] = parse_int(mas['birthDay'])
    mas['deathDay'] = parse_int(mas['deathDay'])


print 'master Count = ' + str(len(master))


for pitch in pitching:
    pitch['yearID'] = parse_int(pitch['yearID'])
    pitch['BB'] = parse_int(pitch['BB'])
    pitch['HR'] = parse_int(pitch['HR'])
    pitch['IBB'] = parse_int(pitch['IBB'])
    pitch['IPouts'] = parse_int(pitch['IPouts'])
    pitch['BK'] = parse_int(pitch['BK'])
    pitch['ERA'] = parse_decimal(pitch['ERA'])
    pitch['WP'] = parse_int(pitch['WP'])
    pitch['stint'] = parse_int(pitch['stint'])
    pitch['GIDP'] = parse_int(pitch['GIDP'])
    pitch['HBP'] = parse_int(pitch['HBP'])
    pitch['SH'] = parse_int(pitch['SH'])
    pitch['SHO'] = parse_int(pitch['SHO'])
    pitch['GS'] = parse_int(pitch['GS'])
    pitch['G'] = parse_int(pitch['G'])
    pitch['H'] = parse_int(pitch['H'])
    pitch['CG'] = parse_int(pitch['CG'])
    pitch['L'] = parse_int(pitch['L'])
    pitch['GF'] = parse_int(pitch['GF'])
    pitch['BFP'] = parse_int(pitch['BFP'])
    pitch['W'] = parse_int(pitch['W'])
    pitch['ER'] = parse_int(pitch['ER'])
    pitch['SV'] = parse_int(pitch['SV'])
    pitch['R'] = parse_int(pitch['R'])
    pitch['SO'] = parse_int(pitch['SO'])
    pitch['SF'] = parse_int(pitch['SF'])


print 'pitching Count = ' + str(len(pitching))


for pitch in pitching_post:
    pitch['yearID'] = parse_int(pitch['yearID'])
    pitch['BB'] = parse_int(pitch['BB'])
    pitch['HR'] = parse_int(pitch['HR'])
    pitch['IBB'] = parse_int(pitch['IBB'])
    pitch['IPouts'] = parse_int(pitch['IPouts'])
    pitch['BK'] = parse_int(pitch['BK'])
    pitch['ERA'] = parse_decimal(pitch['ERA'])
    pitch['WP'] = parse_int(pitch['WP'])
    pitch['GIDP'] = parse_int(pitch['GIDP'])
    pitch['HBP'] = parse_int(pitch['HBP'])
    pitch['SH'] = parse_int(pitch['SH'])
    pitch['SHO'] = parse_int(pitch['SHO'])
    pitch['GS'] = parse_int(pitch['GS'])
    pitch['G'] = parse_int(pitch['G'])
    pitch['H'] = parse_int(pitch['H'])
    pitch['CG'] = parse_int(pitch['CG'])
    pitch['L'] = parse_int(pitch['L'])
    pitch['GF'] = parse_int(pitch['GF'])
    pitch['BFP'] = parse_int(pitch['BFP'])
    pitch['W'] = parse_int(pitch['W'])
    pitch['ER'] = parse_int(pitch['ER'])
    pitch['SV'] = parse_int(pitch['SV'])
    pitch['R'] = parse_int(pitch['R'])
    pitch['SO'] = parse_int(pitch['SO'])
    pitch['SF'] = parse_int(pitch['SF'])


print 'pitching_post Count = ' + str(len(pitching_post))


for salary in salaries:
    salary['yearID'] = parse_int(salary['yearID'])
    salary['salary'] = parse_int(salary['salary'])


print 'salaries Count = ' + str(len(salaries))


print 'schools Count = ' + str(len(schools))


for series in series_post:
    series['yearID'] = parse_int(series['yearID'])
    series['losses'] = parse_int(series['losses'])
    series['wins'] = parse_int(series['wins'])
    series['ties'] = parse_int(series['ties'])


print 'series_post Count = ' + str(len(series_post))


for team in teams:
    team['yearID'] = parse_int(team['yearID'])
    team['FP'] = parse_decimal(team['FP'])
    team['W'] = parse_int(team['W'])
    team['BB'] = parse_int(team['BB'])
    team['BPF'] = parse_int(team['BPF'])
    team['HR'] = parse_int(team['HR'])
    team['IPouts'] = parse_int(team['IPouts'])
    team['Ghome'] = parse_int(team['Ghome'])
    team['ERA'] = parse_decimal(team['ERA'])
    team['3B'] = parse_int(team['3B'])
    team['HA'] = parse_int(team['HA'])
    team['HBP'] = parse_int(team['HBP'])
    team['DP'] = parse_int(team['DP'])
    team['SOA'] = parse_int(team['SOA'])
    team['attendance'] = parse_int(team['attendance'])
    team['PPF'] = parse_int(team['PPF'])
    team['RA'] = parse_int(team['RA'])
    team['SHO'] = parse_int(team['SHO'])
    team['AB'] = parse_int(team['AB'])
    team['E'] = parse_int(team['E'])
    team['G'] = parse_int(team['G'])
    team['H'] = parse_int(team['H'])
    team['CG'] = parse_int(team['CG'])
    team['L'] = parse_int(team['L'])
    team['BBA'] = parse_int(team['BBA'])
    team['R'] = parse_int(team['R'])
    team['2B'] = parse_int(team['2B'])
    team['CS'] = parse_int(team['CS'])
    team['HRA'] = parse_int(team['HRA'])
    team['ER'] = parse_int(team['ER'])
    team['SV'] = parse_int(team['SV'])
    team['Rank'] = parse_int(team['Rank'])
    team['SO'] = parse_int(team['SO'])
    team['SB'] = parse_int(team['SB'])
    team['SF'] = parse_int(team['SF'])


print 'teams Count = ' + str(len(teams))


print 'teams_franchises Count = ' + str(len(teams_franchises))


for team in teams_half:
        team['yearID'] = parse_int(team['yearID'])
        team['G'] = parse_int(team['G'])
        team['Rank'] = parse_int(team['Rank'])
        team['L'] = parse_int(team['L'])
        team['W'] = parse_int(team['W'])
        team['Half'] = parse_int(team['Half'])


print 'teams_half Count = ' + str(len(teams_half))