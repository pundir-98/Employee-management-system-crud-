import sys 
sys.path.append('./')
from flask import *
import crud
import os

app = Flask(__name__)



app.add_url_rule('/hello',view_func=crud.hello, methods=['GET','POST'])
app.add_url_rule('/read',view_func=crud.view, methods=['GET'])
app.add_url_rule('/create',view_func=crud.add_employee, methods=['POST'])
app.add_url_rule('/update',view_func=crud.update_employee, methods=['PUT'])
app.add_url_rule('/delete',view_func=crud.delete_employee, methods=['DELETE'])




    

if __name__== "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(host='0.0.0.0', port=port)