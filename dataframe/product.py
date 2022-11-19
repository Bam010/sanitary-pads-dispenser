import pandas as pd
from dataframe.airtable import product, transaction
from datetime import datetime
import numpy as np

pd_product = pd.DataFrame(data=product, columns=['Name', 'in', 'out', 'Picking', 'left', 'Vidva building 3', '100yrs building' ])
pd_product.drop(columns=[ 'Name', 'in', 'out', 'Picking', 'left'], inplace=True)

# 'Vidva building 3', '100yrs building'
prod = pd_product.to_dict('split')
prod['total']= [sum(padtype) for padtype in prod['data']]

loc = pd_product.T.to_dict('split')
loc['columns'] = ['Laurier', 'Sofie']

# set up
pd_trans = pd.DataFrame(data=transaction, columns=['num', 'user','user (from user)', 'Type', 'Type (from Type)', 'Date', 'Location','Location (from Location)', 'amount', 'amount_int','in/out'])
pd_trans.drop(columns=[ 'num', 'user', 'user (from user)', 'amount', 'Type', 'Location'], inplace=True)
pd_trans['Date'] = pd.to_datetime(pd_trans['Date'], format = '%Y-%m-%dT%H:%M:%S.%fZ').dt.date
pd_trans.columns = ['Type','Date', 'Location', 'amount', 'in_out']

# #  'Type','Date', 'Location', 'amount', 'in/out'
trans_total = pd_trans[['Type','Date','Location', 'in_out']]
trans_total['Type'] = trans_total['Type'].apply(lambda x: x[0])
trans_total['Location'] = trans_total['Location'].apply(lambda x: x[0])

row =[]
padtype = trans_total['Type'].unique()
places = trans_total['Location'].unique()

for i in padtype:
	sub_row = []
	for j in places:
		data = trans_total.loc[(trans_total['Type']==i) & (trans_total['in_out']=='in'), ['Date','Location']].loc[trans_total['Location']==j, 'Date'].sort_values(ascending=True).diff()
		sub_row.append(data.mean().days)
	row.append(sub_row)
# trans_total_prod = pd.DataFrame(data=row, columns=places, index=padtype)

trans_total = pd.DataFrame(data=row, columns=places, index=padtype)
trans_total_loc = trans_total.agg(np.mean).to_dict()
trans_total_prod = trans_total.T.agg(np.mean).to_dict()
# trans_total_loc = []
trans_total_prod['index']=['Laurier', 'Sofie']
trans_total_loc['index']=['Vidva 3rd building', '100yrs building']

# trans_total_loc = trans_total
# trans_total_prod = padtype

# trans_total_loc = trans_total_loc.to_dict('split')
# trans_total_prod = trans_total_prod.to_dict('split')
# trans_total_prod['index']=['Laurier', 'Sofie']
# trans_total_ =  trans_total.iloc[0,:]
# trans_total = {'padType': padtype,'meandate':meandate, 'mindate': mindate}

#  chane amount based on in_out
# trans_total['amount'] = pd.to_numeric(trans_total['amount'])
# trans_total.loc[trans_total['in_out']=='out', 'amount'] *= -1
# # create new colum for 'type-location'
# trans_total['padtype-loc'] = [str(trans_total['Type'][i]) +'-'+ str(trans_total['Location'][i]) for i in range(trans_total['amount'].shape[0])]
# trans_total.drop(columns=['in_out' , 'Type', 'Location'], inplace=True)

# # 'Date', 'amount', 'padtype-loc'
# data=trans_total[['Date', 'amount', 'padtype-loc']]
# # create total number of pad in each day, type, location
# trans_total_by_date_sum = pd.pivot_table(data, values='amount', index='Date' ,columns='padtype-loc', aggfunc=np.sum)
# trans_total_by_date = trans_total_by_date_sum.fillna(0).cumsum()
# trans_total_by_date_dict = trans_total_by_date.T.to_dict('split')
# trans_total_by_date_dict['columns'] = [str(x) for x in trans_total_by_date_dict['columns']]

# col = trans_total_by_date.columns
# arraydate = trans_total_by_date[col].T.apply(lambda x: x.between(1,6)).T
# arraydate['date'] = trans_total_by_date.index

# for col_name in col:
# 	idx = arraydate.index[arraydate[col_name]]
# 	datediff = [0]
# 	if len(idx)>1:
# 		datediff = [(arraydate['date'].loc[i]-arraydate['date'].loc[i+1]) for i in range(len(idx)-1)]
		
	

# trans_total_by_time = pd.DataFrame()
# trans_total_by_time['Date'] = pd.date_range(start=pd_trans['Date'].min(), end=pd_trans['Date'].max(), freq='D')
# trans_total_by_time = pd_trans['Date'].min()
