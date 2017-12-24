import pandas as pd
import numpy as np 
import os
import xlrd
import tushare as ts

# 获取report
def Get_report():
	# 创建空的dataframe
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	# 创建2007-2016年的财务报表
	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_report_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)


		# 创建2017年的财务报表
	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_report_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_report.xlsx',encoding='utf-8')

# 获取盈利能力报表
def Get_profit():
	# 创建空的dataframe
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	# 创建2007-2016年的财务报表
	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_profit_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)


		# 创建2017年的财务报表
	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_profit_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_profit.xlsx',encoding='utf-8')

	

# 获取营运能力报表
def Get_operation():
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_operation_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)



	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_operation_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_operation.xlsx',encoding='utf-8')



# 获取成长能力报表
def Get_growth():
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_growth_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)



	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_growth_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_growth.xlsx',encoding='utf-8')



# 获取偿债能力报表
def Get_debtpaying():
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_debtpaying_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)



	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_debtpaying_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_debtpaying.xlsx',encoding='utf-8')


# 获取现金流量能力报表
def Get_cashflow():
	jieguo_old=pd.DataFrame()
	jieguo_new=pd.DataFrame()

	for i in range(2007,2017):
		for j in range(1,5):

			so=ts.get_cashflow_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_old=jieguo_old.append(All)



	for i in range(2017,2018):
		for j in range(1,4):

			so=ts.get_cashflow_data(i,j)
			xx=so.iloc[:,1].size
			df_n=pd.DataFrame({'date':[(str(i)+'-'+str(j))]*xx
								# 'name':so.loc[:,'name']
									})

			All=pd.concat([so,df_n],axis=1,join='outer')
			jieguo_new=jieguo_new.append(All)


	jieguo=jieguo_old.append(jieguo_new)
	jieguo=jieguo.drop_duplicates()
	jieguo.to_excel('E:\\blog数据\\stock_cashflow.xlsx',encoding='utf-8')

	

def Get_basics():
	df=ts.get_stock_basics()
	df=df.drop_duplicates()
	df.to_excel('E:\\blog数据\\stock_basics.xlsx',encoding='utf-8')



# 合并报表
def Merge():
	# sp=pd.read_excel('E:\\blog数据\\stock_profit.xlsx',encoding='utf-8')
	# so=pd.read_excel('E:\\blog数据\\stock_operation.xlsx',encoding='utf-8')
	# sg=pd.read_excel('E:\\blog数据\\stock_growth.xlsx',encoding='utf-8')
	# sd=pd.read_excel('E:\\blog数据\\stock_debtpaying.xlsx',encoding='utf-8')
	# sc=pd.read_excel('E:\\blog数据\\stock_cashflow.xlsx',encoding='utf-8')
	# sr=pd.read_excel('E:\\blog数据\\stock_report.xlsx',encoding='utf-8')
	# # 创建用于做模型的数据总表
	# stock_all = pd.merge(sp,so, on=['name','date'])
	# stock_all = pd.merge(stock_all,sg, on=['name','date'])
	# stock_all = pd.merge(stock_all,sd, on=['name','date'])
	# stock_all = pd.merge(stock_all,sc, on=['name','date'])
	# stock_all = pd.merge(stock_all,sr, on=['name','date'])


	# stock_all.to_excel('E:\\blog数据\\stock_all.xlsx',encoding='utf-8')

	# 建立用于创建ECharts的数据集
	# 读取总数据，缺失值处理后，创建主键name，

	df=pd.read_excel('E:\\blog数据\\stock_all.xlsx',encoding='utf-8')
	df=df.fillna(value='-')

	names=list(set(df.loc[:,'name']))

	# 选定需要的变量名，如下进行循环创建所需要的list格式

	ALL=pd.DataFrame()

	ks=['roe','eps','date','epcf','net_profits','business_income','bips','net_profit_ratio','bvps','eps_yoy','profits_yoy','distrib','report_date',
			'gross_profit_rate','bips','arturnover','inventory_turnover','currentasset_turnover',
			'mbrg','nprg','nav','targ','epsg','seg',
			'currentratio','quickratio','cashratio','icratio','adratio','sheqratio','cf_sales','rateofreturn','cf_nm','cf_liabilities','cashflowratio']

	for i in names:
		df_x=pd.DataFrame({'name':[i]})
		df_n=df[df.name == i]

		for k in ks:
			df_k=df_n.loc[:,k]
			list_k=[]

			for line in df_k:
				list_k.append(line)
			df_nk=pd.DataFrame({k:str(list_k),
								'name':[i]})
			print(df_nk)
			df_x=pd.merge(df_x,df_nk)

		ALL=ALL.append(df_x)

	ALL.to_excel('E:\\blog数据\\stock_all_for_Echarts.xlsx',encoding='utf-8')
	df1=pd.read_excel('E:\\blog数据\\stock_basics.xlsx',encoding='utf-8')
	df2=pd.read_excel('E:\\blog数据\\stock_all_for_Echarts.xlsx',encoding='utf-8')

	df_x=pd.merge(df1,df2,on=['name'])
	print(df_x.head(5))
	df_x.to_excel('E:\\blog数据\\stock_all_for_Echarts2.xlsx',encoding='utf-8')



	return ALL

	

def main():
	# Get_report()
	# Get_profit()
	# Get_operation()
	# Get_growth()
	# Get_debtpaying()
	# Get_cashflow()
	# Get_basics()
	Merge()





if __name__ == '__main__':
	main()

	

