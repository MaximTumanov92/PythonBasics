time = int(input("Input time in seconds"))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60
print("{0:=02}:{1:=02}:{2:=02}".format(hours, minutes, seconds))
