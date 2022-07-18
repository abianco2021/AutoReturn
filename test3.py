import mysql.connector
import pandas as pd
import folium

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

def get_trucks_location(cursor, tow):
     args = ['2022-06-06', '2025-07-07', tow]
     cursor.callproc('sp_ds_ARCOMD0006_TowToZoneLocationAtDispatchTowId_New', args)
     for result in cursor.stored_results():
         details = result.fetchall()
     return details

select_stmt = (
"""
select 
a.towId
,b.latitude, b.longitude
,coalesce(c.vin, '') as vin
,c.license
,c.stateId
,m.make
,mm.model
,c.vehicleYear
from ads_tow a
join ads_location b
on b.locationid = a.originLocationId
join ads_vehicle c
on a.vehicleId = c.vehicleId
left join ref_make m
on c.makeId = m.makeId
left join ref_model mm
on c.modelId = mm.modelId
where a.towId = %s
"""
)

def get_tow_location(cursor, towid):
     cursor.execute(select_stmt, (towid,))
     myresult = cursor.fetchall()
     return myresult

# towid = '2268434' or '2246900'
# towid = input("Enter Tow ID: ")
towid = '2268434'

cursor = mydb.cursor()
car = get_tow_location(cursor, towid)
cursor.close()
car

