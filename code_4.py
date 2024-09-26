import csv
import pandas as pd
#queries and operattions only
#return data
#

big_mac_file = pd.read_csv('./big-mac-full-index.csv')

#print(big_mac_file.head())

#filter 2, year and country code
def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}' and date >='{year}-01-01' and  date <='{year}-12-31')"
    #query_text2 = f"(date == '{year}'')"
    sub_df1 = big_mac_file.query(query_text)

    sub_df1 = sub_df1['dollar_price'].mean()

    #print(type(sub_df1))

    rounded = round(sub_df1, 2)
    
    return rounded


def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}')"
    #query_text2 = f"(date == '{year}'')"
    sub_df1 = big_mac_file.query(query_text)

    sub_df1 = sub_df1['dollar_price'].mean()

    #print(type(sub_df1))

    rounded = round(sub_df1, 2)
    
    return rounded
#tricky idx.max
def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"(date >='{year}-01-01' and  date <='{year}-12-31')"
    #query_text2 = f"(date == '{year}'')"
    sub_df1 = big_mac_file.query(query_text)
    sub_df2 = big_mac_file.query(query_text)
    sub_df3 = big_mac_file.query(query_text)
    sub_df4 = big_mac_file.query(query_text)

    sub_df1 = sub_df1['dollar_price'].idxmin()
    this = sub_df2.loc[sub_df1, 'name']

    cc = sub_df3.loc[sub_df1, 'iso_a3']

    minval = sub_df4['dollar_price'].min()
    rounded = round(minval, 2)

    final = f"{this}({cc}): ${rounded}"

    #print(type(sub_df1))

    #rounded = round(sub_df1, 2)


    return final

def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"(date >='{year}-01-01' and  date <='{year}-12-31')"
    #query_text2 = f"(date == '{year}'')"
    sub_df1 = big_mac_file.query(query_text)
    sub_df2 = big_mac_file.query(query_text)
    sub_df3 = big_mac_file.query(query_text)
    sub_df4 = big_mac_file.query(query_text)

    sub_df1 = sub_df1['dollar_price'].idxmax()
    this = sub_df2.loc[sub_df1, 'name']

    cc = sub_df3.loc[sub_df1, 'iso_a3']

    minval = sub_df4['dollar_price'].max()
    rounded = round(minval, 2)

    final = f"{this}({cc}): ${rounded}"

    #print(type(sub_df1))

    #rounded = round(sub_df1, 2)


    return final

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2012,'arg')
    print(result_a)
    result_b = get_big_mac_price_by_country('mex')
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2012)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)