def dl_funct(url):
	import urllib.request
	dl_data=urllib.request.urlopen(url)
	return dl_data
def proc_funct(data_var):
	import csv
	import re
	import datetime
	data_csv=[entry.decode('utf-8') for entry in data_var]
	data_test=(csv.reader(data_csv))
	data_dict={}
	for line in data_test:
		hit_time=datetime.datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
		data_dict[hit_time]=(line[0],line[2])
	return data_dict		




def main():
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('--url', type=str)
	args=parser.parse_args()
	pass_page=dl_funct(args.url)
	csv_proc=proc_funct(pass_page)
if __name__=="__main__":
	main()
	
