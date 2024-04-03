import requests
import sqlite3

json_url = "https://www.mnpower.com/Environment/WaterTableJSON"
r = requests.get(json_url)

for dam in r.json()['reportData']:
    db_conn = sqlite3.connect('databse.db')
    dam_name = dam['tag']
    dam_last_updated = dam['time']
    dam_flow = dam['value']
    c = db_conn.cursor()
    print(f'inserting data for {dam_name}')
    c.execute("INSERT INTO flow_data (dam_name,last_updated,flow) VALUES (?,?,?)", (dam_name,dam_last_updated,dam_flow))
    db_conn.commit()
    db_conn.close()
