input = open('ActualInput.txt', 'r')
output = open('ActualOutput.txt', 'w')
for j in input:
    clock= j.split(':')
    hours=int(clock[0])
    if len(clock) > 1:
        mins = int(clock[1])
        secs = int(clock[2])
    #print type(hours)
        hourang=(12-hours)*30.0-(60.0*mins+secs)*30.0/3600
        minang=(mins)*6.0 +secs/10.0
        secang=secs*6
        angle1= hourang +minang
        if angle1>360:
            angle1=(angle1-360)
        if angle1<360 and angle1>180:
            angle1=360-angle1
        if angle1>180:
            angle1=angle1-180
        #print angle1
        angle2=hourang+secang
        if angle2>360:
            angle2=(angle2-360)
        if angle2<360 and angle2>180:
            angle2=360-angle2
        if angle2>180:
            angle2=angle2-180

        #print angle3
        #angle3=minang+secang
        if minang>secang:
            angle3=minang-secang
        else:
            angle3=secang-minang
        if angle3>360:
            angle3=(angle3-360)
        if angle3<360 and angle3>180:
            angle3=360-angle3
        if angle3>180:
            angle3=angle3-180
        prin=str(round(angle1,2))+', '+str(round(angle2,2))+', '+str(round(angle3,2))
        print prin
    else:
        prin=str(hours)
    output.write(prin+'\n')
