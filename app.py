import random
from sklearn import svm
from textblob import TextBlob
from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
#1 = rock
#2 = paper
#3 = scissors
input_data = [  
[1, 1, 2],

[1, 2, 3],

[3, 1, 2],

[2, 1, 2]]

output_data = [3, 2, 1, 1]

model = svm.SVC()

model.fit(input_data, output_data)

history = [1, 1, 2]

def getAI():

  data_record = [history[-3], history[-2], history[-1]]

  current = model.predict([data_record])[0]

  if current == 1:

    return 2

  elif current == 2:

    return 3

  else:

    return 1


@app.route("/rps/<userInput>")

def rps(userInput):
  user = int(userInput)
  comp = getAI()
  history.append(user)
  input_data.append([history[-4], history[-3], history[-2]])
  output_data.append(history[-1])
  model.fit(input_data, output_data)

  if comp == 1 and user == 1:
    return "It’s a tie!"

  elif comp == 1 and user == 2:
    return "The user wins!"

  elif comp == 1 and user == 3:
    return "The comp wins!"  

  elif comp == 2 and user == 1:
    return "The comp wins!"

  elif comp == 2 and user == 2:
    return "It’s a tie!"

  elif comp == 2 and user == 3:
    return "The user wins!"

  elif comp == 3 and user == 1:
    return "The user wins!"

  elif comp == 3 and user == 2:
    return "The comp wins!"

  elif comp == 3 and user == 3:
    return "It’s a tie!!"


app.run(host="0.0.0.0")










# from flask import Flask, jsonify, render_template
# from flask_cors import CORS
# import pandas as pd
# import numpy as np
# import requests

# app = Flask(__name__)
# CORS(app)

# #Reading data
# data_df = pd.read_csv("churn_data.csv")
# churn_df = data_df[(data_df['Churn']=="Yes").notnull()]

# # @app.route('/')
# # def index():
# #    return render_template('index.html')

# def calculate_percentage(val, total):
#    """Calculates the percentage of a value over a total"""
#    percent = np.round((np.divide(val, total) * 100), 2)
#    return percent

# def data_creation(data, percent, class_labels, group=None):
#    for index, item in enumerate(percent):
#        data_instance = {}
#        data_instance['category'] = class_labels[index]
#        data_instance['value'] = item
#        data_instance['group'] = group
#        data.append(data_instance)

# @app.route('/get_piechart_data')
# def get_piechart_data():
#    contract_labels = ['Month-to-month', 'One year', 'Two year']
#    _ = churn_df.groupby('Contract').size().values
#    class_percent = calculate_percentage(_, np.sum(_)) #Getting the value counts and total

#    piechart_data= []
#    data_creation(piechart_data, class_percent, contract_labels)
#    return jsonify(piechart_data)

# @app.route('/get_barchart_data')
# def get_barchart_data():
#    tenure_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
#    churn_df['tenure_group'] = pd.cut(churn_df.tenure, range(0, 81, 10), labels=tenure_labels)
#    select_df = churn_df[['tenure_group','Contract']]
#    contract_month = select_df[select_df['Contract']=='Month-to-month']
#    contract_one = select_df[select_df['Contract']=='One year']
#    contract_two =  select_df[select_df['Contract']=='Two year']
#    _ = contract_month.groupby('tenure_group').size().values
#    mon_percent = calculate_percentage(_, np.sum(_))
#    _ = contract_one.groupby('tenure_group').size().values
#    one_percent = calculate_percentage(_, np.sum(_))
#    _ = contract_two.groupby('tenure_group').size().values
#    two_percent = calculate_percentage(_, np.sum(_))
#    _ = select_df.groupby('tenure_group').size().values
#    all_percent = calculate_percentage(_, np.sum(_))

#    barchart_data = []
#    data_creation(barchart_data,all_percent, tenure_labels, "All")
#    data_creation(barchart_data,mon_percent, tenure_labels, "Month-to-month")
#    data_creation(barchart_data,one_percent, tenure_labels, "One year")
#    data_creation(barchart_data,two_percent, tenure_labels, "Two year")
#    return jsonify(barchart_data)

# if __name__ == '__main__':  #app.run(debug=True)
#   app.run(host="0.0.0.0")
