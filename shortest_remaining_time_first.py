# ass_python
arrival_time = [];
burst_time = [];
rem_time = [];
process_name =[]
turn_around_total = 0
sum_wait = 0;

def get_input(process_no):
	count = 0
	while count< process_no:
		process_name.append(raw_input("Enter process name  :"))
		arrival_time.append(int(raw_input("Enter arrival time  :")))
		burst_time.append(int(raw_input("Enter burst time  :")))
		rem_time.append(burst_time[count])
		count += 1
	return 


process_no = int(raw_input("Enter number of Process(es) : "))
get_input(process_no);
print "\nProcess name\t|Turnaround Time| Waiting Time\n"

rem_time.append(99999)
time = 0;
remain = 0;

while remain != process_no:
    smallest = process_no -1
    counter = 0;
    while counter < process_no:
        if arrival_time[counter] <= time and rem_time[counter] < rem_time[smallest] and rem_time[counter] > 0:
            smallest = counter
        counter += 1
    rem_time[smallest] -= 1
    if rem_time[smallest] == 0:
        remain += 1
        endTime = time + 1
        print process_name[smallest], "\t", "\t", endTime - arrival_time[smallest], "\t", "\t", endTime - burst_time[smallest] - arrival_time[smallest]
        sum_wait += endTime - burst_time[smallest] - arrival_time[smallest]
        turn_around_total += endTime - arrival_time[smallest]
    time += 1
print "\nAverage waiting time = ", sum_wait * 1.0 / process_no
print "Average Turnaround time = ", turn_around_total * 1.0 / 5












#zaidi
