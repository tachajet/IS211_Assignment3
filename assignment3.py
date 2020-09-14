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
def metric_funct(dict_var):
	import re
	count=0
	img_cnt=0
	ie_cnt=0
	ff_cnt=0
	ch_cnt=0
	sf_cnt=0
	for val in dict_var.values():
        	count+=1
        	if re.search(r"png$|png$|gif$|jpe?g$",val[0],re.IGNORECASE):
                	img_cnt+=1
        	if re.search(r"msie[/\s]([\d.]+)",val[1],re.IGNORECASE):
                	ie_cnt+=1
        	if re.search(r"firefox[/\s]([\d.]+)",val[1],re.IGNORECASE):
                	ff_cnt+=1
        	if re.search(r"chrome[/\s]([\d.]+)",val[1],re.IGNORECASE):
                	ch_cnt+=1
        	if re.search(r"version[/\s]([\d.]+)",val[1],re.IGNORECASE):
                	sf_cnt+=1
	image_ratio=((float(img_cnt/count))*100)
	browser_dict={ch_cnt:"Chrome",ie_cnt:"Internet Explorer",ff_cnt:"FireFox",sf_cnt:"Safari"}
	return browser_dict[max(browser_dict.keys())], str(image_ratio)


def main():
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('--url', type=str)
	args=parser.parse_args()
	pass_page=dl_funct(args.url)
	csv_proc=proc_funct(pass_page)
	metric_proc=metric_funct(csv_proc)
	print("The most popular browser for the day is", metric_proc[0])
	print("The ratio of image requests to all others is", str(metric_proc[1])+"%")
if __name__=="__main__":
	main()	
