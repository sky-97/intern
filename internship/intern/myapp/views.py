from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd


def main(df_a,df_b):
	column_name='CustomerID'
	join_type='inner'
	sorting_type_value = 0

	def Transform_join(df_a,df_b,column_name,join_type):
		df_c=pd.merge(df_a, df_b,on=column_name,how=join_type)
		return df_c

	def Transform_sort(df,column_name,sorting_type_value):
		df_d = df.sort_values(by=column_name, ascending=sorting_type_value)
		return df_d

	df_c = Transform_join(df_a,df_b,column_name,join_type)
	df_d = Transform_sort(df_c,column_name,sorting_type_value)
	
	return df_c,df_d


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.FILES['myfile_second']:
        myfile = request.FILES['myfile']
        myfile_second = request.FILES['myfile_second']

        print("file runing")
        if myfile.name == 'orders.csv':
        	df_orders = pd.read_csv(myfile)
        	df_customers = pd.read_csv(myfile_second)
        else:
        	df_orders = pd.read_csv(myfile_second)
        	df_customers = pd.read_csv(myfile)

        df_join,df_sort = main(df_orders,df_customers)

        # orders = df_orders[0:10].to_html(index=False)
        # customers = df_customers[0:10].to_html(index=False)
        # join = df_join[0:10].to_html(index=False)
        # sort = df_sort[0:10].to_html(index=False)

        return render(request, 'myapp/home.html',{ 
        	'orders' : df_orders[0:10].to_html(index=False) ,
        	'customers' : df_customers[0:10].to_html(index=False),
        	'join':df_join[0:10].to_html(index=False),
        	'sort':df_sort[0:10].to_html(index=False)  
        })
    return render(request, 'myapp/home.html',{ 
    	'orders':'nothing',
    	'customers':'nothing', 
    	'join':'nothing',
    	'sort':'nothing'
    })

