#Arnab Kumar Datta  (arnabkd) - Task 7.5
filename = "sample.txt"
f = open(filename, 'r')

for line in f:	
	x = line.strip('\n').strip('\r').strip().split(',')
	sum = 0.0
	for i in range (1, len(x)):
		sum += float(x[i])
	print "%s , %0.5f"%(x[0],sum)

f.close()

Runtime example
#arnabkd@stcroix ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke7 $ more sample.txt 
#"activity 1", 2376, 256, 87
#"activity 2", 27, 89, 12
#"activity 3", 199, 166.50, 0
#arnabkd@stcroix ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke7 $ python process_spreadsheet.py 
#"activity 1" , 2719.00000
#"activity 2" , 128.00000
#"activity 3" , 365.50000
