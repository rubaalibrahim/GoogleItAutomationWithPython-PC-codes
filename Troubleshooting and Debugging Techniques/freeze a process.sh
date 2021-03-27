''' this is a bash script to automate the process of getting the PID of processes that are running synchronously (for example ffmpeg) and are taking up too much RAM and slowing down the server, i used pidof command to get the PID and then puased all the ffmpeg processes by using the kill command and then let the processes run one by one and after each process executes the server stops for 1 second and then executes the next process and so on '''


for pid in $(pidof ffmpeg);
do while kill -CONT $pid;
do sleep 1;
done;
done
