import pandas as pd
df= pd.read_csv('./big-mac-full-index.csv')

#print(df.iloc[2])

print(df)

#country code = iso_a3

country_code = 'RUS'
print('HEREEE')
query_text = f"(iso_a3 == '{country_code}')"

print(len(df))
print('THISSS')

sub_df = df.query(query_text)

print(len(sub_df))

print(sub_df)

print(sub_df.loc[21])
print('\n')
print(sub_df.iloc[21])

print(sub_df['dollar_price'].mean())

new_query = f"date > '2012-01-01' and date <'2012-12-31'"

new_date_df = df.query(new_query)

print(new_date_df)