# ass_python
array_data_input = []
wait_time = 0
index_of_process_name =0
index_arrival_time = 1
index_burst_time =2

process_no = int(raw_input('Enter the No. of Process : '))
for i in xrange(process_no):
	array_data_input.append([])
	print ' '
	array_data_input[i].append(raw_input('Enter Process Name : ' ))
	array_data_input[i].append(int(raw_input('Enter Arrival Time ')))
	array_data_input[i].append(int(raw_input('Enter Burst Time :')))


print ' '
array_data_input.sort(key = lambda array_data_input:array_data_input[2])


wait = []
loop_counter = 1
service = []
service.append(0)
wait.append(service[0] + array_data_input[index_of_process_name][index_arrival_time])

while (loop_counter <process_no):
	service.append(service[loop_counter-1] + array_data_input[loop_counter-1][index_burst_time])
	wait.append(service[loop_counter] - array_data_input[loop_counter][index_arrival_time])
	loop_counter += 1

print '\tProcess Name \tArrival Time \t Burst Time \t Service Time \t Waiting Time'
for i in xrange(process_no):
	print '\t\t',array_data_input[i][index_of_process_name] ,'\t\t\t\t' ,array_data_input[i][index_arrival_time] ,'\t\t\t\t', array_data_input[i][index_burst_time], '\t\t\t\t',service[i],'\t\t\t\t',wait[i]
	wait_time += wait[i]

print 'Total Waiting Time : ',wait_time
print 'Average Waiting Time : ',(wait_time/process_no)






#zaidi
