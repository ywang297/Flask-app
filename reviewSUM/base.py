from flask import Flask, render_template,session, redirect, url_for,flash, request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired
import pandas as pd
import numpy as np 
from reviewSUM import app


#completdat_new = pd.read_pickle('/Users/yishu/Documents/insight/completdat_new_1003.p')
#df2=pd.read_csv('data_final.csv')
data = pd.read_pickle('/Users/yishu/Documents/insight/app/reviewSUM/data_for_app_new.p')

data.loc[data['brand']=='NARS','p_id']

#app= Flask(__name__)

@app.route('/')
def index():
    
    products = data['brand_product'].tolist()

    return render_template('index.html', products=products)

@app.route('/results', methods= ["POST"])
def jono():

    product= request.form.get('product')
  
    summary= data.loc[data['brand_product']==product, 'summary'].tolist()[0]
    
    brand = data.loc[data['brand_product']==product, 'brand'].tolist()[0]
    
    pid = str(data.loc[data['brand_product']==product, 'p_id'].tolist()[0])
    
    productname = data.loc[data['brand_product']==product, 'product'].tolist()[0]
    
    rating = round(data.loc[data['brand_product']==product, 'p_star'].tolist()[0], 1)

    price = data.loc[data['brand_product']==product, 'p_price'].tolist()[0]
    
#    helpful1 = completdat_new.loc[completdat_new['product']==productname,'r_review'].tolist()[0]
#    
#    helpful2 = completdat_new.loc[completdat_new['product']==productname,'r_review'].tolist()[1]
#
#    helpful3 = completdat_new.loc[completdat_new['product']==productname,'r_review'].tolist()[2]
#
#    helpful4 = completdat_new.loc[completdat_new['product']==productname,'r_review'].tolist()[3]


    return render_template('output.html', summary=summary, brand=brand
                           , productname=productname, pid=pid
                           , price=price, rating=rating)
#                           helpful1=helpful1, helpful2=helpful2
#                           ,helpful3=helpful3, helpful4=helpful4)








#
#@app.route('/')
#def test():

#    return render_template('index.html', productT= productT)
#    print(strains[0])
#    print(competdat_new)

#@app.route('/index', methods= ["POST"])
#def jono():
#
#    productL= request.form.get('productL')
##    weight= request.form.get('weight')
#
#    print(strain)
##    print(weight)
##
##    def distance(row):
##        cols = ['Feat0','Feat1','Feat2','Feat3','Feat4','Feat5','Feat6','Feat7']
##        return(df[cols]-row[cols]).abs().sum(axis=1)
##
##    df.set_index('strain_list', inplace=True)
##    dist= df.apply(distance, axis=1)
#
##    recommendation= completdat_new.loc[completdat_new['product']==strain, 'summary'].tolist()[0]
#
##test= completdat_new.loc[completdat_new['product']=="Calendula Deep Clean Foaming Face Wash", 'summary'].tolist()[0]
#
#
##    first_choice= recommendation[0]
##    second_choice= recommendation[1]
##    third_choice= recommendation[2]
#
#    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)
    
    
    

