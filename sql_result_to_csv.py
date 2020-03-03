import db_connect
import pandas as pd
from pprint import pprint


mydb = db_connect.connect_dbs()
mycursor = mydb.cursor(dictionary=True)
# With dictionary = True, cursor can return the field name

mycursor.execute(f"SELECT * FROM database.table")
temp_result = mycursor.fetchall()
df = pd.DataFrame(temp_result)
pprint(df)
df.to_csv('table.csv', index=False)

print('Done!')
