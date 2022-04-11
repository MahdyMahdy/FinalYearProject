import inspect, os, csv
import pyodbc
		
class DatabaseManager:
    def __init__(self,connString):
        self.connString=connString
        con = pyodbc.connect(self.connString)
        con.close()
        pass

    def select(self,query):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        data = cursor.execute(query)
        data = cursor.fetchall()
        cursor.commit()
        conn.commit()
        conn.close()
        return data

    def insert(self,query,data):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        data = cursor.execute(query,data)
        cursor.commit()
        conn.commit()
        conn.close()
        pass

    def delete(self,query):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        data = cursor.execute(query)
        cursor.commit()
        conn.commit()
        conn.close()
        pass

    def createDatabase(self,name):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE "+name)
        cursor.commit()
        conn.commit()
        conn.close()
        self.connString='DRIVER={SQL Server};SERVER=.;DATABASE=I3308MSDB'
        pass

    def createTables(self):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE ProjectsCollection (coll_id varchar(15) primary key,branch int,year int,nb_of_stud int,class_lang varchar(2))")
        cursor.execute("CREATE TABLE Project (proj_id varchar(15) primary key,supervisor varchar(20),title varchar(100),nb_of_stud int,grade DECIMAL(8,2),stdsInfos TEXT,coll_id varchar(15) references ProjectsCollection(coll_id) on delete cascade)")
        cursor.commit()
        conn.commit()
        conn.close()
        pass

    def execute(self,query):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.commit()
        conn.commit()
        conn.close()
        pass
    pass	