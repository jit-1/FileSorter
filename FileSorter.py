import os,re
try:
	fileName= sys.argv[1]
	eps = float(sys.argv[2])
	minpts = int(sys.argv[3])
	outputFile = sys.argv[4]
except Exception as e:
	with open('config','r') as inf:
			config = eval(inf.read())

	inputFolder= config["input_folder"]
	outputFile = config["output_file"]

x = [f for f in os.listdir(inputFolder) ]
file_wt=open(outputFile,'w')
for i in x:
	ori_node=re.split('_',i)
	temp=str(ori_node[5])+","+str(ori_node[6])+","+str(ori_node[2])
	print (temp)
	#p1.append(temp)
	file_wt.write(temp+"\n")
file_wt.close()



	
	
