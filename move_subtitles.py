'''
Program that shifts subtitles forward or backward by a number of seconds.
Sometimes a subtitle file does not match well with a movie file, and the
video player you use may not support shifting. 
Does not support fractional seconds (milliseconds).

Subtitle files should be of type SRT and times should be in the format:
HH:MM:SS,mmm --> HH:MM:SS,mmm 
File should be in the same directory as this program when executed.
'''
import datetime
numseconds = int(input("Input a number of seconds to shift subtitles."))
in_file = open("test.srt","r")
out_file = open("output.srt","w")

for line in in_file:
    times = line.split(" --> ")
    if len(times) <= 1:
        out_file.write(line)
        print(line,end="")
        continue
    s_time = (times[0].split(":")[0],
                  times[0].split(":")[1],
                  times[0].split(":")[2][:-4],
                  times[0].split(":")[2][-3:])
    e_time = (times[1].split(":")[0],
                times[1].split(":")[1],
                times[1].split(":")[2][:-5],
                times[1].split(":")[2][-4:-1])
    new_start_time = datetime.datetime(100,1,1,int(s_time[0]),int(s_time[1]),int(s_time[2]))
    new_start_time = new_start_time + datetime.timedelta(0,numseconds)
    new_end_time = datetime.datetime(100,1,1,int(e_time[0]),int(e_time[1]),int(e_time[2]))
    new_end_time = new_end_time + datetime.timedelta(0,numseconds)
    out_file.write(str(new_start_time).split(" ")[1]+","+s_time[3]+" --> "+str(new_end_time).split(" ")[1]+","+e_time[3]+"\n")
    print(str(new_start_time).split(" ")[1]+","+s_time[3]+" --> "+str(new_end_time).split(" ")[1]+","+e_time[3])
out_file.close()
