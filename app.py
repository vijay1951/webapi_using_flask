from flask import Flask,request
from datetime import datetime
from database import api_controller
obj=api_controller()
app = Flask(__name__)

@app.route("/")
def Home():
    return "Try this api"

@app.route('/folders',methods=['GET'])   
def get_all_folder():
    return obj.get_all_folders()

@app.route('/folders/<id>',methods=['GET'])  
def get_folder_by_id(id):
    return obj.get_folders_byid(id)

@app.route('/folders/<folder_name>',methods=['POST'])  
def create_folders(folder_name):
    return obj.create_folder(folder_name) 

@app.route('/folder/<folder_id>',methods=['GET'])
def get_all_files(folder_id):
    return obj.get_file_inFolder(folder_id)

# @app.route('/folderName/<folder_id>/<file_id>',methods=['GET'])
# def get_allFiles_inFolders(folder_id,file_):
#     return obj.get_allFiles_inFolder(folder_id)   

@app.route('/folders_upload/<folder_id>',methods=['POST'])
def upload_files_inFolder(folder_id):
    file = request.files['file']
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    f1=file.filename            
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    content=file.content_type
    finalFilePath= f"uploads/{uniqueFileName}.{ext}"
    print(finalFilePath)
    file.save(finalFilePath)
    return obj.upload_files_inFolders(f1,content,finalFilePath,folder_id)

@app.route('/folders/<folder_name>/<folder_id>',methods=['PUT'])
def update_folder(folder_name,folder_id):
    print(folder_name,folder_id)
    return obj.update_folder(folder_name,folder_id)

@app.route('/folders/<folder_id>',methods=['DELETE'])
def delete_folder(folder_id):
    return obj.delete_folder(folder_id)   

@app.route('/folders/<folder_id>/<file_name>/<file_id>',methods=['PUT'])
def update_file(folder_id,file_name,file_id):
    return obj.update_files(folder_id,file_name,file_id) 

@app.route('/folders/<folder_id>/<file_id>',methods=['DELETE'])
def delete_file(folder_id,file_id):
    return obj.delete_files(folder_id,file_id)

if __name__=="__main__":
    app.run(debug=True)
