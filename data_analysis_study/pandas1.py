# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:35:24 2019

@author: dcng
"""

import pandas as pd



##데이터 입출력

#csv 파일 불러오기 - read_csv함수.
cctv_seoul=pd.read_csv("cctv_in_seoul.csv", encoding='utf-8')
cctv_seoul.head()   #df의 일부 데이터 출력. default 5개


#이름변경 - rename함수.
#inplace 인자: default=False - 원본은 바뀌지 않고 출력만 바꿔서 함.
#inplace=True면 원본 df의 column name이 바뀜.
cctv_seoul.rename(columns={cctv_seoul.columns[0]:'구별'}, inplace=True)
cctv_seoul.head()


#엑셀 파일 불러오기 - read_excel()함수
import xlrd
#pandas에서는 read_excel함수 사용
pop_seoul=pd.read_excel('population_in_seoul.xls', encoding='utf-8')
pop_seoul.head()

#header=2 : 3번째 줄부터 행으로 인식.
#usecols:원하는 column만 인식(ppt에는 parse_cols인데 usecols로 바뀜)
pop_seoul=pd.read_excel('population_in_seoul.xls', header=2,
                        usecols='B,D,G,J,N', encoding='utf-8')
pop_seoul.head()
#column name 바꾸기 (dictionary?!)
pop_seoul.rename(columns={"자치구":"구별", "계":"인구수", "계.1":"한국인",
                          "계.2":"외국인", "65세이상고령자":"고령자"}, inplace=True)
'''
pop1=xlrd.open_workbook('population_in_seoul.xls')
print(pop1.sheet_names())
worksheet=pop1.sheet_by_index(0)
'''



##데이터 정렬
#sort_values 함수
#cctv데이터를 소계 기준으로 오름차순 정렬하기
cctv_seoul.sort_values(by="소계", ascending=False).head(6)
#이 때 인덱스는 원래 테이블대로 출력됨
#  -> 새롭게 인덱스를 부과할 때 : reset_index(drop=True) 사용

#최근 3년간 cctv 증가율 계산
cctv_seoul['최근증가율']=(cctv_seoul['2016년']+cctv_seoul['2015년']+
          cctv_seoul['2014년'])/cctv_seoul['2013년도 이전']*100
cctv_seoul.sort_values(by="최근증가율", ascending=False).head(5)



##dataframe에서 특정 column, row 삭제
#drop함수 : 디폴트는 행, axis=1로 지정하면 열을 삭제함   df2=df.drop('행번호')
#del함수: column 삭제할때만 활용. 영구적으로 열을 삭제함

#인구현황 자료에서 합계 행 삭제
pop_seoul.drop([0], inplace=True)
pop_seoul.head()

#null데이터 찾기
pop_seoul[pop_seoul['구별'].isnull()]
#외국인과 고령자 비율 찾기
pop_seoul.drop([26], inplace=True)
pop_seoul['외국인비율']=pop_seoul['외국인']/pop_seoul['인구수']
pop_seoul['고령자비율']=pop_seoul['고령자']/pop_seoul['인구수']
pop_seoul.head()




##데이터프레임 병합: merge함수
#   공통 열/인덱스 기준으로 두 개의 테이블을 합침.(on인자)
# cctv와 population 데이터를 구별 기준으로 합치기
data_result=pd.merge(cctv_seoul, pop_seoul, on="구별")
data_result.head()
#의미없는 칼럼 삭제
data_result.drop(['2013년도 이전', '2014년','2015년','2016년'], 
                 axis=1, inplace=True)

##데이터프레임 병합: merge함수
#   공통 열/인덱스 기준으로 두 개의 테이블을 합침.(on인자)
# cctv와 population 데이터를 구별 기준으로 합치기
data_result=pd.merge(cctv_seoul, pop_seoul, on="구별")
data_result.head()
#의미없는 칼럼 삭제
data_result.drop(['2013년도 이전', '2014년','2015년','2016년'], 
                 axis=1, inplace=True)



##데이터프레임 인덱스 설정
#  set_index: 기존 행 인덱스 제거하고 column중 하나를 인덱스로 설정.
#  reset_indx: 기존 행 인덱스 제거하고 인덱스를 마지막 column으로 추가.
data_result.set_index("구별", inplace=True)
data_result.head()
