f =open("yesterday.txt",'r')
yesterday_lyric=""
while 1:
    line =f.readline()
    if not line:
            break
    yesterday_lyric=yesterday_lyric+line.strip()+"\n"
f.close()

Yesterday_count=yesterday_lyric.count("Yesterday")
yesterday_count=yesterday_lyric.count("yesterday")

print("Yesterday의 갯수는", Yesterday_count,"개 이고 yesterday의 갯수는", yesterday_count, "이다.")
