from typing import Collection
from ProjectsWindow import ProjectsWindow
from logging import log
from tkinter.constants import NO, W
import CreateWindow,BrowseWindow,StartWindow,AddWindow
import tkinter as tk
import DataBase

connString ='DRIVER={SQL Server};SERVER=.;DATABASE=I3308MSDB'

try:
    #testing the database if is exist
    dbm = DataBase.DatabaseManager(connString=connString)
    pass
#if not exist:
except :
    #Creating the database and the tables
    dbm = DataBase.DatabaseManager('DRIVER={SQL Server};SERVER=.;')
    dbm.createDatabase("I3308MSDB")
    dbm.createTables()
    pass

#creating the browse window with the buttons functions
def makebrowseWindow(rowID):
    #open button function
    def open():
        #get the selection
        row = browseWindow.collections.selection()
        #get the values
        item = browseWindow.collections.item(row,"values")
        #if nothing selected close
        if len(item)==0:
            return
        #get the max nb of std
        maxNbOfStd = int(item[3])
        #get the collection id
        col_id = str(item[0])
        #function for button add
        def addButtonFunc():
            #inserting in the database
            def addFunc():
                #craeeting the data array
                data = []
                #creating id
                count = 0
                id = item[0]+str(count)
                n = dbm.select("SELECT COUNT(*) FROM Project WHERE proj_id='"+id+"'")
                while n[0][0]>0:
                    count+=1
                    id = item[0]+str(count)
                    n = dbm.select("SELECT COUNT(*) FROM Project WHERE proj_id='"+id+"'")
                    pass
                data.append(id)
                #get the supervisorname
                if add.superVisorNameVar.get() == "":
                    add.superVisorVal.set("Please enter supervisor name")
                    return
                else:
                    add.superVisorVal.set("")
                superName = add.superVisorNameVar.get()
                data.append(superName)
                #get the title
                if add.titleVar.get() == "":
                    add.titleVal.set("Please enter the title")
                    return
                else:
                    add.titleVal.set("")
                title = add.titleVar.get()
                data.append(title)
                #spliting the stds in array
                stdsInfos = ""
                #counter to count the student
                count =0
                for i in range(len(add.stdsInfos)):
                    #if std not exist continue
                    if len(add.stdsInfos[i].get())==0:
                        continue
                    count+=1
                    stdsInfos+=add.stdsInfos[i].get()
                    #the stds is seperated by <->
                    stdsInfos+="<->"
                if count == 0:
                    add.stdVal.set("You should enter at least one student ")
                    return
                else:
                    add.stdVal.set("")
                data.append(count)
                #get th grade
                try:
                    float(add.gradeVar.get())
                    add.stdVal.set("")
                except:
                    add.gradeVal.set("grade must be numeric")
                    return
                grade = add.gradeVar.get()
                data.append(grade)
                #get students infos
                data.append(stdsInfos)
                #add th id
                data.append(col_id)
                #insert all data in the data base
                dbm.insert("INSERT INTO Project VALUES(?,?,?,?,?,?,?)",data=data)
                #converting the data to insert it to treeview
                row = data
                row.pop(-1)
                stds = row[-1]
                row.pop(-1)
                #concatinate stds infos in one string to insert it to data base
                stds = stds.split("<->")
                for j in range(len(stds)):
                    row.append(stds[j])
                    pass
                projetsWindow.data.append(row)
                #insert the data to treeview
                projetsWindow.projects.insert(parent='', index=-1 , text='',values=row)
                #close th window
                add.window.destroy()
                pass
            #create the add window
            add = AddWindow.AddWindow(start.window,title="Add",maxNbOfStd=maxNbOfStd,addFunc=addFunc,entrydata=None)
            pass
        def removeFunc():
            #get selection
            row = projetsWindow.projects.selection()
            item = projetsWindow.projects.item(row,"values")
            #if nothing selected
            if len(item)==0:
                return
            #get the index of the selected row
            index = projetsWindow.projects.index(row)
            #get id
            id = item[0]
            #delete from DB
            dbm.delete("DELETE FROM Project WHERE proj_id='"+id+"'")
            #delete from treeview
            projetsWindow.projects.delete(row)
            #delete from data
            projetsWindow.data.pop(index)
            pass
        def editFunc():
            #get selection
            row = projetsWindow.projects.selection()
            item = projetsWindow.projects.item(row,"values")
            #if nothing selected return
            if len(item)==0:
                return
            #edit logic
            def editWindowFunc():
                if edit.superVisorNameVar.get() == "":
                    edit.superVisorVal.set("Please enter supervisor name")
                    return
                else:
                    edit.superVisorVal.set("")
                if edit.titleVar.get() == "":
                    edit.titleVal.set("Please enter the title")
                    return
                else:
                    edit.titleVal.set("")
                #create new data array to insert the new value
                data = [item[0],edit.superVisorNameVar.get(),edit.titleVar.get()]
                #counting the student
                count =0
                stds = ""
                #concat stds infos
                for i in range(len(edit.stdsInfos)):
                    if not edit.stdsInfos[i].get()=="":
                        count+=1
                        stds+=edit.stdsInfos[i].get()+"<->"
                    pass
                if count == 0:
                    edit.stdVal.set("You should enter at least one student ")
                    return
                else:
                    edit.stdVal.set("")
                #insert stds nb
                data.append(count)
                #insert new grade
                try:
                    float(edit.gradeVar.get())
                    edit.stdVal.set("")
                except:
                    edit.gradeVal.set("grade must be numeric")
                    return
                data.append(edit.gradeVar.get())
                #insert new stds
                data.append(stds)
                #insert col_id
                data.append(item[-1])
                #update the database
                dbm.execute("UPDATE project SET supervisor = '"+data[1]+"',title ='"+data[2]+"',nb_of_stud ="+str(data[3])+",grade ="+str(data[4])+",stdsInfos ='"+data[5]+"' WHERE proj_id='"+data[0]+"'")
                #converting data to tree row
                data.pop(-1)
                stds = data[-1]
                data.pop(-1)
                stds = stds.split("<->")
                for j in range(len(stds)):
                    data.append(stds[j])
                    pass
                projetsWindow.data.append(data)
                #delete from tree
                projetsWindow.projects.delete(row)
                #delete from data
                for i in range(len(projetsWindow.data)):
                    if projetsWindow.data[i][0]==item[0]:
                        projetsWindow.data.pop(i)
                        break
                #insert data in tree
                projetsWindow.projects.insert(parent='', index=-1 , text='',values=data)
                edit.window.destroy()
                pass
            edit = AddWindow.AddWindow(start.window,title=item[0], maxNbOfStd=maxNbOfStd,addFunc=editWindowFunc,entrydata=item)
            pass
        #get selection
        row = browseWindow.collections.selection()
        item = browseWindow.collections.item(row,"values")
        # tree heading
        cols = ['ID', 'Supervisor','Title', 'Nb of Std',"Grade"]
        if len(item)==0:
            return
        #add stds tree heading
        for i in range(int(item[3])):
            cols.append("std "+str(i+1)+" Infos")
        cols = tuple(cols)
        #get data from data base
        data = dbm.select("SELECT * FROM Project where coll_id='"+col_id+"'")
        browseWindow.window.destroy()
        projetsWindow = ProjectsWindow(start.window,id=col_id,cols=cols,data=data,maxNbOfStd= int(item[3]),removeFunc=removeFunc,addFunc=addButtonFunc,editFunc=editFunc)
        pass
    def remove():
        #get selection
        row = browseWindow.collections.selection()
        item = browseWindow.collections.item(row,"values")
        if len(item)==0:
            return
        index = browseWindow.collections.index(row)
        id = item[0]
        #delete from database
        dbm.delete("DELETE FROM ProjectsCollection WHERE coll_id='"+id+"'")
        #delete from tree
        browseWindow.collections.delete(row)
        #delte from data
        browseWindow.data.pop(index)
        pass
    cols = ('ID', 'Branch','Year', 'Max Nb of Std','Class Lang')
    data = dbm.select("SELECT * FROM ProjectsCollection")
    browseWindow = BrowseWindow.BrowseWindow(start.window,cols,data,remove,open)
    if not rowID==None:
        for i in range(len(browseWindow.collections.get_children())):
            if browseWindow.data[i][0]==rowID:
                browseWindow.collections.selection_add(i)
                break
            pass
        open()
    pass

#function for create button in Start Window
def makeCreateWindow():
    #function for create button in Create Window
    def Create():
        #inserting a new project collection
        data = [" "]
        #testing if branch number is selected
        try:
            data.append(int(createWindow.branchVar.get()[0]))
            createWindow.branchVal.set("")
        #if not exist display error message
        except:
            createWindow.branchVal.set("Please Select Branch Number")
            return
        #testing if year is numeric
        try:
            data.append(int(createWindow.firstYear.get()))
            #removing error message
            createWindow.yearVal.set("")
            #testing if year is fomed by 4 digit
            if not len(str(data[2])) == 4:
                createWindow.yearVal.set("must be formed from 4 digit only")
                return
        #if not numeric display error message
        except:
            createWindow.yearVal.set("must be numeric")
            return
        #getting other values
        data.append(createWindow.groupVar.get())
        data.append(createWindow.lang.get())
        #creating id by branch+lang+year+count
        count = 0
        id = str(data[1])+str(data[2])+data[4]+str(count)
        n = dbm.select("SELECT COUNT(*) FROM ProjectsCollection WHERE coll_id='"+id+"'")
        while n[0][0]>0:
            count+=1
            id = str(data[1])+str(data[2])+data[4]+str(count)
            n = dbm.select("SELECT COUNT(*) FROM ProjectsCollection WHERE coll_id='"+id+"'")
            pass
        data[0]=id
        #inserting in the database
        dbm.insert("INSERT INTO ProjectsCollection VALUES(?,?,?,?,?) ",data)
        #closing thw window
        createWindow.window.destroy()
        makebrowseWindow(id)
        pass
    def Cancel():
        #close create window
        createWindow.window.destroy()
        pass
    #creating the create window with the buttons functions
    createWindow=CreateWindow.CreateWindow(start.window,Create,Cancel)
    pass

#creating the start window with the buttons functions
start = StartWindow.StartWindow(makeCreateWindow,lambda :makebrowseWindow(None))
#show the start window
start.show()