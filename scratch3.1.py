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
test_var=dl_funct('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')
import re
count=0
img_cnt=0
test_dict=(proc_funct(test_var))
for val in test_dict.values():
	count+=1
	val_txt=str(val)
	print(val_txt)
	if re.search(r"[/.png$][/.gif$]",val_txt):
		img_cnt+=1 
	

print(count)
print(img_cnt)
