from django.shortcuts import render
import pandas as pd
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
def Home(request):
     if(request.method=="POST"):
        data=request.POST
        Temperature=data.get('Temperature')
        Humidity=data.get('Humidity')
        TVOC=data.get('TVOC')
        eCO2=data.get('eCO2')
        Raw_H2=data.get('Raw_H2')
        Raw_Ethanol=data.get('Raw_Ethanol')
        Pressure=data.get('Pressure')
        PM1=data.get('PM1')
        PM2=data.get('PM2')
        NC0=data.get('NC0')
        NC1=data.get('NC1')
        NC2=data.get('NC2')
        CNT=data.get('CNT')
       
        
        path="C:\\Users\\abhis\\Desktop\\ML-fracture\\Basics\\train_dataset.csv"
        data=pd.read_csv(path)
        
    

        inputs=data.drop(['UTC','Fire Alarm'],'columns')
        outputs=data.drop(['UTC','Temperature','Humidity','TVOC','eCO2','Raw_H2','Raw_Ethanol','Pressure','PM1','PM2','NC0','NC1','NC2','CNT'],'columns')
        x_train,x_test,y_train,y_test= train_test_split(inputs,outputs,train_size=0.8)

        model=GaussianNB()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        result=model.predict([[Temperature,Humidity,TVOC,eCO2,Raw_H2,Raw_Ethanol,Pressure,PM1,PM2,NC0,NC1,NC2,CNT]])
        if len(result)!=0:
            return render(request,"Home.html",context={'result':result})
        
        
     return render(request,'Home.html')