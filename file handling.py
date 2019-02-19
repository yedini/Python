"""
Created on Tue Feb 19 18:29:12 2019
Chapter 12. Exception and File Handling
  - File handling
@author: dcng
"""
#file 열기
f=open("i_have_a_dream.txt", "r")  #"r":파일을 읽기만 할때 사용
f.read()  #해당 파일 안에 모든 텍스트를 읽어들임.
f.close()

#with 구문과 함께 사용
with open("i_have_a_dream.txt", "r") as file:
    content=file.read()
    print(content)

#'한줄'씩 읽어 list type으로 반환하기 : readline함수
with open("i_have_a_dream.txt", "r") as file1:
    content_list=file1.readlines()
    print(type(content_list))
    for line in content_list[::5]:  #다섯줄만 읽어오기
        print(line, end="")  #하나 프린트할때마다 끝에 뭐 달기: end인자
    file1.close()


#단어의 통계정보 산출하기 (split함수:특정문자 기준으로 텍스트를 분리함)
with open("i_have_a_dream.txt", "r") as file1:
    contents=file1.read()
    word_list=contents.split(" ") #빈칸기준으로 단어분리
    line_list=contents.split("\n") #한줄씩 분리
    print("Total # of words:", len(word_list))
    print("Total # of lines:", len(line_list))


#file write
f=open("count_log.txt", "w", encoding='utf8')
for i in range(1, 11):
    data="%d번째 줄입니다.\n" % i
    f.write(data) #count_log 파일에 기록됨.


#directory 만들기
import os
os.mkdir("log_one")  #현재 디렉토리에 log_one이라는 파일이 생김
if not os.path.isdir("log"):  #현재 디렉토리 안에 log라는 이름의 파일이 없는 경우 만듦.
    os.mkdir("log")   