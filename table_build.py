import acquire_webpage as acquire
import requests as r
from bs4 import BeautifulSoup as bs
import prep_table as prep
import pandas as pd


def create_webpage_stats_table(): 
    url = 'https://keithgalli.github.io/web-scraping/webpage.html'
    webpage = acquire.get_webpage(url)
    column_names_list = prep.create_column_names_list(webpage)
    table_rows_list = prep.create_table_rows_list(webpage)
    seasons_list = prep.create_seasons_list(table_rows_list)
    (team_name_list, team_links_list) = prep.create_team_name_links_lists(table_rows_list)
    (league_list, league_link_list) = prep.create_league_name_link_lists(table_rows_list)
    regular_stats_list = prep.create_regular_stats_list(table_rows_list)
    postseason_link_list=prep.create_postseason_links_list(table_rows_list)
    post_stats_names_list = prep.create_post_stats_names_list(table_rows_list)
    postseason_stats_dictionary = prep.create_postseason_stats_dictionary(post_stats_names_list, table_rows_list)

    # we start with an empty dictionary 'table_row_dict'
    table_row_dict={}

    # use the column_names_list to fill in the keys of the dictionary.
    for x in column_names_list:
        table_row_dict[x]=[]

    # table_row_dict
    table_row_dict['season'] = seasons_list
    table_row_dict['team']=team_name_list
    table_row_dict['league_link_list']=league_link_list
    table_row_dict['league'] = league_list
    table_row_dict['post_season_links'] = postseason_link_list

    # create a list of the regular_stats_names for keys that come from the first dictionary keys of regular_stats_list[0]
    regular_stats_names_list=[]
    for k in regular_stats_list[0]:
        regular_stats_names_list.append(k)
        
    # regular_stats_names_list

    # post_season_names_list
    # create a list of post
    postseason_names_list=[]
    for x in regular_stats_names_list:
            postseason_names_list.append(x.replace('regular', 'postseason'))

    postseason_names_list.append('postseason')
    postseason_names_list.append('separator')

    # create the keys for regular_stats dictionaries that comes from the regular_stats_names_list
    regular_stats_dictionary={}
    for x in regular_stats_names_list:
        regular_stats_dictionary[x]=[]
    regular_stats_dictionary


    # create a range the is the length of 'regular_stats_values_list'. 
    # Go through each item in the range (0-4), to collect each dictionary and the corresponding key
    # to append to each key in regular_stats_dict.
    for r in range(len(regular_stats_list)):
        for k in regular_stats_dictionary:
            regular_stats_dictionary[k].append(regular_stats_list[r][k])
        
    #regular_stats_dictionary

    # append regular season stats dictionary to table_row_dict
    for k in regular_stats_dictionary:
        table_row_dict[k]=regular_stats_dictionary[k]

    # use postseason_stats_dictionary to fill in values for the 'postseason' and 'separator' keys
    for k in postseason_stats_dictionary:
        table_row_dict[k]=postseason_stats_dictionary[k]

    df=pd.DataFrame(table_row_dict)

    # clean up a little bit. join the column names with '_' i.e. 'regular_gp'.
    new_col_names_list = []
    for x in df.columns:
        x = x.replace(' ','_')
        x = x.replace('pm', '+/-')
        new_col_names_list.append(x)

    df.columns = new_col_names_list

    return(df)

