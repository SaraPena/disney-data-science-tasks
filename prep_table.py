# web scraping table data from: https://keithgalli.github.io/web-scraping/webpage.html
# created pages based on work in webpage_scraping_intro.ipynb

# import packages we will use
import acquire_webpage as acquire
from bs4 import BeautifulSoup as bs

# test variables
# url ='https://keithgalli.github.io/web-scraping/webpage.html'
# webpage = acquire.get_webpage(url)

# function: create_column_names_list(webpage)
def create_column_names_list(webpage):
    table_headers = webpage.find('table').find_all('th')
    column_names_list=[' '.join(th['class']) for th in table_headers]
    return(column_names_list)

# test function
# column_names_list=create_column_names_list(webpage)
# column_names_list

# function: create_table_rows_list(webpage)
def create_table_rows_list(webpage):
    table_rows_list =webpage.find('tbody').find_all('tr')
    return(table_rows_list)

# test function
# table_rows_list=create_table_rows_list(webpage)

# function: create_seasons_list(table_rows_list)
def create_seasons_list(table_rows_list):
    seasons_list = []
    for r in table_rows_list:
        season_string=r.find('td', attrs={'class':'season sorted'}).get_text()
        seasons_list.append(season_string.strip())
    return(seasons_list)

# test function
# seasons_list = create_seasons_list(table_rows_list)
# seasons_list

# function: create_team_name_links_list(table_rows_list)
def create_team_name_links_lists(table_rows_list):
    team_name_list=[]
    team_links_list=[]
    for r in table_rows_list:
        team_info=r.find('td', attrs={'class':'team'})
        if team_info.find('a'):
            team_name=team_info.find('a').get_text().strip()
            team_season_link=team_info.find('a')
            team_name_list.append(team_name)
            team_season_link = team_info.find('a')
            team_links_list.append(team_season_link['href'])
        else:
            team_name=team_info.get_text().strip()
            team_season_link= ""
            team_name_list.append(team_name)
            team_links_list.append(team_season_link)

    return(team_name_list, team_links_list)

# test function
# (team_name_list, team_links_list) = create_team_name_links_lists(table_rows_list)
# team_name_list, team_links_list

# function: create_league_name_link_lists(table_rows_list)
def create_league_name_link_lists(table_rows_list):
    league_list=[]
    league_link_list=[]
    for r in table_rows_list:
        league_info=r.find('td', attrs={'class':'league'})
        league_list.append(league_info.get_text().strip())
        league_link=league_info.find('a')
        league_link_list.append(league_link['href'])

    return(league_list, league_link_list)

# test function
# league_list, league_link_list=create_league_name_link_lists(table_rows_list)
# league_list, league_link_list

def create_regular_stats_list(table_rows_list):
    regular_stats_list=[]
    for r in table_rows_list:
        numeric_stats_names_list=['regular GP','regular G','regular A','regular TP','regular PIM', 'regular PM']
        numeric_stats_names_list=[str.lower(x) for x in numeric_stats_names_list]
        stats_dictionary={}
        for i in numeric_stats_names_list:
            if r.find('td', attrs={'class': f'{i}'}):
                info=r.find('td', attrs={'class': f'{i}'})
                if info.get_text()!='':
                    stats_dictionary[i]=(int(info.get_text()))
                else:
                    stats_dictionary[i]=''
            else:
                stats_dictionary[i]=''
        regular_stats_list.append(stats_dictionary)
    return(regular_stats_list)

# test function
# regular_stats_list=create_regular_stats_list(table_rows_list)

# function: create_postseason_stat_list(column_name, table_rows_list)

def create_postseason_stat_list(column_name,table_rows_list):
    column_list=[x.get_text().strip()for x in [r.find('td', attrs={'class':column_name}) for r in table_rows_list]]
    return(column_list)

# test function
# separator_list=create_postseason_stat_list('separator', table_rows_list)

# function: create_postseason_links(table_rows_list)

def create_postseason_links(table_rows_list):
    postseason_links= ['no link' if link=='no link' else link['href'] for link in [a_tag.find('a') if a_tag.find('a') else 'no link' for a_tag in [x.find('td', attrs={'class':'postseason'}) for x in table_rows_list]]]
    return(postseason_links)

# test function
# postseason_links=create_postseason_links(table_rows_list)

# function: create_post_stats_names_list(table_rows_list)

def create_post_stats_names_list(table_rows_list):
    regular_stats_values_list=create_regular_stats_list(table_rows_list)
    post_stats_names_list=[]
    for x in regular_stats_values_list[0]:
        post_stats_names_list.append(x.replace('regular', 'postseason'))
    post_stats_names_list.append('postseason')
    post_stats_names_list.append('separator')
    return(post_stats_names_list)
    
# test function
# post_stats_names_list = create_post_stats_names_list(table_rows_list)

# function: create_postseason_links(table_rows_list)

def create_postseason_links(table_rows_list):
    postseason_links= ['no link' if link=='no link' else link['href'] for link in [a_tag.find('a') if a_tag.find('a') else 'no link' for a_tag in [x.find('td', attrs={'class':'postseason'}) for x in table_rows_list]]]
    return(postseason_links)

# test function:
# postseason_links=create_postseason_links(table_rows_list)
# postseason_links


# function: create_postseason_stats_dictionary(post_stats_names_list, table_rows_list)

def create_postseason_stats_dictionary(post_stats_names_list, table_rows_list):
    post_stats_dictionary={}
    
    for x in post_stats_names_list:
        post_stats_dictionary[x]=create_postseason_stat_list(x, table_rows_list)
    return(post_stats_dictionary)

# test function
# postseason_stats_dictionary = create_postseason_stats_dictionary(post_stats_names_list, table_rows_list)
# postseason_stats_dictionary