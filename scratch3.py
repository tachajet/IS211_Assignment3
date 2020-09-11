def dl_funct(page):
	import urllib.request
	dl_data=urllib.request.urlopen(page)
	return dl_data





def main():
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('--url', type=str)
	args=parser.parse_args()
	pass_page=dl_funct(args.page)
if __name__="__main__":
	main()

	
