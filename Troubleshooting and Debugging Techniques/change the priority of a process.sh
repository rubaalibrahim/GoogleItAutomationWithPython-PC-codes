''' bash script to automate the task of changing the priority of processes that are running synchronously (for example ffmpeg) and are taking up too much RAM and slowing down the server, i used pidof command to get the PID and then changed the priority of the processes to 19 which is the lowest priority by using the renice command

for pid in $(pidof ffmpeg);
do renice 19 $pid;
done
