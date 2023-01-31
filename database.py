import mysql.connector
class api_controller():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="1951",database="folder_container2")
            self.cur=self.con.cursor(dictionary=True)
            print("succesful")
        except:
            print("Not SUccessful") 
    
    #Getting all the folders -- Read
    def get_all_folders(self):                        
        self.cur.execute("SELECT * FROM folders")
        res=self.cur.fetchall()
        if len(res):
            self.con.commit()
            return res
        else:
            return "No data"      
    
    #Getting Folder By Id  -- Read
    def get_folders_byid(self,id):
        self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(id,))
        id1=self.cur.fetchall()
        if len(id1):
            self.cur.execute("SELECT * FROM folders f Where f.folder_id=%s",(id,))
            res=self.cur.fetchall()
            self.con.commit()
            return res 
        else:
            return "Invalid id"     
    
    #Creating a folder -- Create   
    def create_folder(self,folder_name):
        self.cur.execute("SELECT folder_name FROM folders")
        id1=self.cur.fetchall()
        if folder_name not in id1:
            self.cur.execute("INSERT INTO folders (folder_name) VALUES(%s)",(folder_name,))  
            self.con.commit()
            return "created Folder"  
        else:
            return "Already folder name exist"    
    
    #update a folder -- update
    def update_folder(self,folder_name,folder_id):
        self.cur.execute("SELECT folder_name FROM folders")
        id2=self.cur.fetchall()
        if folder_name not in id2:
            self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(folder_id,))
            id1=self.cur.fetchall()
            if len(id1):
                self.cur.execute("UPDATE folders SET folder_name = %s WHERE folder_id=%s",(folder_name,folder_id))
                self.con.commit()
                return "folder updated"
            else:
                return "folder not updated due to bad id"   
        else:
            return "folder name already exist"         

    #delete a folder --delete
    def delete_folder(self,folder_id):
        self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(folder_id,))
        id1=self.cur.fetchall()
        if len(id1):
            self.cur.execute("DELETE FROM files WHERE folder_id = %s", (folder_id,)) 
            self.con.commit()
            self.cur.execute("DELETE FROM folders WHERE folder_id = %s", (folder_id,)) 
            self.con.commit()
            return "folder deleted"
        else:
            return "folder not deleted"    
    
    #Getting all files in a folder -- Read    
    def get_allFiles_inFolder(self,folder_id):
        self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(folder_id,))
        id1=self.cur.fetchall()
        if len(id1):
            self.cur.execute("SELECT * FROM files f WHERE f.folder_id=%s ",(folder_id,))  
            res=self.cur.fetchall()
            self.con.commit()
            return str(res)  
        else:
            return "No file to display"       
    
    #Getting files by id  --Read       
    def get_file_inFolder(self,folder_id):
        self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(folder_id,))
        id1=self.cur.fetchall()
        if len(id1):
            self.cur.execute("SELECT * FROM files f WHERE f.folder_id=%s",(folder_id,))  
            res=self.cur.fetchall()
            self.con.commit()
            return str(res)   
        else:
            return "Bad id"     

    #Uploading a file --create
    def upload_files_inFolders(self,file_name,file_content,filepath,folder_id):
        self.cur.execute("SELECT file_name FROM files")
        id2=self.cur.fetchall()
        if file_name not in id2:
            self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s",(folder_id,))
            id1=self.cur.fetchall()
            if len(id1):
                self.cur.execute("INSERT INTO files (file_name,file_type,fileaddr,folder_id) VALUES(%s,%s,%s,%s)",(file_name,file_content,filepath,folder_id))
                self.con.commit()
                return "file uploaded"
            else:
                return "file not uploaded"   
        else:
            return "file already exist"         

    #updating a file   -- update
    def update_files(self,folder_id,file_name,file_id):
        self.cur.execute("SELECT file_name FROM files")
        id2=self.cur.fetchall()
        if file_name not in id2:
            self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s and file_id=%s",(folder_id,file_id))
            id1=self.cur.fetchall()
            if len(id1):
                self.cur.execute("UPDATE files SET file_name = %s WHERE file_id=%s and folder_id=%s",(file_name,file_id,folder_id))
                self.con.commit()
                return "file updated"
            else:
                return "file not updated"  
        else:
            return "file name already exist"          

    #delete a files --delete
    def delete_files(self,folder_id ,file_id):
        self.cur.execute("SELECT folder_id FROM folders Where folder_id=%s and file_id=%s",(folder_id,file_id))
        id1=self.cur.fetchall()
        if len(id1):
            self.cur.execute("DELETE FROM files WHERE file_id = %s and folder_id=%s", (file_id,folder_id)) 
            self.con.commit()
            return "file deleted"
        else:
            return "file not deleted"    

        