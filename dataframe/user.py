import pandas as pd
from dataframe.airtable import user
from datetime import datetime
import numpy as np

pd_user = pd.DataFrame(data=user, columns=['user', 'first day out', 'Age', 'Occupation', 'out day', 'out night', 'total out', 'total in', 'Picking 2'])
pd_user.drop(columns=[ 'out day', 'out night', 'total out', 'total in','Picking 2'], inplace=True)

# 'user', 'first day out', 'Age', 'Occupation'

pd_user['first day out'] = pd.to_datetime(pd_user['first day out'], format = '%Y-%m-%d %H:%M:%S').apply(lambda x: str(x.date()))

monthly_user = pd_user[pd_user['first day out'].apply(lambda x: int(x[5:7])) == datetime.now().month]

user_age = pd_user[['Age', 'user']].groupby(by='Age').count()
user_age = user_age.T.to_dict('split')

user_by_date = pd_user[['first day out', 'user']].groupby(by='first day out').count()
user_by_date = user_by_date.T.to_dict('split')

user_date_occu = pd_user[['first day out', 'Occupation', 'user']]
user_date_occu = pd.pivot_table(user_date_occu, values='user', index='Occupation',columns='first day out', aggfunc='count')
user_date_occu = user_date_occu.fillna(0).to_dict('split')

user_occu = pd_user[['Occupation', 'user']].groupby(by='Occupation').count()
user_occu = user_occu.T.to_dict('split')