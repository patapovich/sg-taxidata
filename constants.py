FILENAME='data.json'
TSTAMP='%Y-%m-%dT%H:%M:%S%z'
DATE='%Y%m%d'
TABLE_CREATE_QUERY='create table if not exists taxis (id integer primary key autoincrement,date text, time text,x integer, y integer,value integer)'
TABLE_INSERT_QUERY='insert into taxis (date,time,x,y,value) values (%s,%s,%d,%d,%d)'


#Singapore bounds as taken from Google maps - includes From Tuas to Changi and 
#from Sentosa to Woodlands
min_lat=1.237831
max_lat=1.470989
min_lon=103.605713
max_lon=104.043019