# ass_python

array_input_data = []
wait_time = 0.0
index_of_process_name =0
index_arrival_time = 1
index_burst_time =2

def get_input(process_no, array_input_data):
    for i in xrange(process_no):
        array_input_data.append([])
        print ' '
        array_input_data[i].append(raw_input('Enter Process Name : ' ))
        array_input_data[i].append(int(raw_input('Enter Arrival Time ')))
        array_input_data[i].append(int(raw_input('Enter Burst Time :')))

process_no = int(raw_input(' No. of Process : '))
get_input(process_no,array_input_data)
array_input_data.sort(key = lambda array_input_data:array_input_data[index_arrival_time])
print 'ok this is your result of First come first serve '

wait = []
counter = 1
service = []
service.append(array_input_data[index_of_process_name][index_arrival_time])
wait.append(service[0] - array_input_data[index_of_process_name][index_arrival_time])

while (counter<process_no):
	service.append(service[counter-1] + array_input_data[counter-1][index_burst_time])
	wait.append(service[counter] - array_input_data[counter][index_arrival_time])
	wait_time += wait[counter]
	counter += 1

print '\n\tProcess Name \tArrival Time \t Burst Time \t Service Time \t Waiting Time'
for i in xrange(process_no):
	print '\t\t',array_input_data[i][index_of_process_name] ,'\t\t\t\t' ,array_input_data[i][index_arrival_time] ,'\t\t\t\t', array_input_data[i][index_burst_time], '\t\t\t\t',service[i],'\t\t\t\t',wait[i]


print 'Average Waiting Time : ',(wait_time/(process_no*1.0))
print 'Total Waiting Time : ',wait_time
print '\n............................................................'













#zaidi
