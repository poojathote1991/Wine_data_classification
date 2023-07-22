from flask import Flask,render_template,jsonify,request
from utils import WindData
import config



app=Flask(__name__)
@app.route('/')
def home():
    return render_template('wine_class.html')

@app.route('/predicted_class',methods=['GET','POST'])
def predicted_class():
    if request.method=='GET':
        data=request.args.get
        print("Data: ",data)
        Alcohol=eval(data('Alcohol'))
        Malic_acid=eval(data('Malic_acid'))
        Ash=eval(data('Ash'))
        Acl=eval(data('Acl'))
        Mg=eval(data('Mg'))
        Phenols=eval(data('Phenols'))
        Flavanoids=eval(data('Flavanoids'))
        Nonflavanoid_phenols=eval(data('Nonflavanoid_phenols'))
        Proanth=eval(data('Proanth'))
        Color_int=eval(data('Color_int'))
        Hue=eval(data('Hue'))
        OD=eval(data('OD'))
        Proline=eval(data('Proline'))
        wine=WindData(Alcohol,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids
                        ,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline)
        pred_class=wine.get_predicted_class()
        return render_template('wine_class.html',prediction=pred_class)
    
    if request.method=='POST':
        data=request.form
        print("Data: ",data)
        Alcohol=data['Alcohol']
        Malic_acid=data['Malic_acid']
        Ash=data['Ash']
        Acl=data['Acl']
        Mg=data['Mg']
        Phenols=data['Phenols']
        Flavanoids=data['Flavanoids']
        Nonflavanoid_phenols=data['Nonflavanoid_phenols']
        Proanth=data['Proanth']
        Color_int=data['Color_int']
        Hue=data['Hue']
        OD=data['OD']
        Proline=data['Proline']
        wine=WindData(Alcohol,Malic_acid,Ash,Acl,Mg,Phenols,Flavanoids
                        ,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline)
        pred_class=wine.get_predicted_class()
        return render_template('wine_class.html')
    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)

