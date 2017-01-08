# ass_python

array_input_data = []
wait_time = 0
index_of_process_name =0
index_arrival_time = 1
index_burst_time =2
index_pirority =3

process_no = int(raw_input('Enter the No. of Process : '))
for i in xrange(process_no):
	array_input_data.append([])
	print ' '
	array_input_data[i].append(raw_input('Enter Process Name : ' ))
	array_input_data[i].append(int(raw_input('Enter Arrival Time :')))
	array_input_data[i].append(int(raw_input('Enter Burst Time :')))
	array_input_data[i].append(int(raw_input('Enter Priority :')))

print ' '
time_slice = int(raw_input('Enter the time slice for Process : '))
print ' '
array_input_data.sort(key = lambda array_input_data:(array_input_data[index_arrival_time], array_input_data[index_pirority]))

total = 0
wait = []
finish = []
duplicate_array = []

for i in xrange(process_no):
	finish.append(index_of_process_name)
	total += array_input_data[i][index_burst_time]
	duplicate_array.append(array_input_data[i][index_burst_time])
	wait.append(index_of_process_name)


index = 0
counter = 0

while (counter < total):
	index = index % process_no
	for k in xrange(time_slice):
		if(duplicate_array [index] != 0):
			duplicate_array [index] -= 1
			counter += 1
			if (duplicate_array [index] == 0):
				finish[index] = counter + array_input_data [index][index_arrival_time]
				break
	index += 1

for i in xrange(process_no):
	wait[i]  = finish[i] - array_input_data[i][index_arrival_time] - array_input_data[i][index_burst_time]

print 'Process Name \tArrival Time \t Burst Time \t  Waiting Time'
for i in xrange(process_no):
	print '\t', array_input_data[i][index_of_process_name] ,'\t\t' ,array_input_data[i][index_arrival_time] ,'\t\t', array_input_data[i][index_burst_time], '\t\t',wait[i]
	wait_time += wait[i]

print 'Total Waiting Time : ',wait_time
print 'Average Waiting Time : ',(wait_time/process_no)

raw_input()















#Zaidi
