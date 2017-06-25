import sqlite3
from utils import *
from constants import *

def load_taxi_to_db(dbname,directory,grid_height=20):
	db=sqlite3.connect(dbname)
	db.execute(TAXI_TABLE_CREATE_QUERY)
	data=process_data(directory,TAXI_FILENAME,grid_height)
	grid_width=get_width(grid_height)
	for date, time, grid in data:
		for y in range(grid_height+1):
			for x in range(grid_width+1):
				db.execute(TAXI_TABLE_INSERT_QUERY,(date,time,x,y,grid[y][x]))
	db.commit()
	db.close()

def fetch_grid_by_date(dbname,date):
	return fetch_from_db(dbname,TAXI_BY_DATE_QUERY,(date,))

def fetch_grid_by_time(dbname,time):
	return fetch_from_db(dbname,TAXI_BY_TIME_QUERY,(time,))

def fetch_grid_by_date_and_time(dbname,date,time):
	return fetch_from_db(dbname,TAXI_BY_DATE_AND_TIME_QUERY,(date,time))

def fetch_loc_by_date(dbname,date,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_DATE_QUERY_XY,(date,x,y))

def fetch_loc_by_time(dbname,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_TIME_QUERY_XY,(time,x,y))

def fetch_loc_by_date_and_time(dbname,date,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_DATE_AND_TIME_QUERY_XY,(date,time,x,y))

