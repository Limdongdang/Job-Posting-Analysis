import requests
import json
import pandas as pd

col = ['id','마감여부','공고주소','회사명','공고제목','업종명','지역코드','근무형태코드','상위직무코드','직무코드','직무키워드','경력코드','최소경력','최대경력','학력코드','학력','연봉코드','등록일','조회수','지원자수']
df = pd.DataFrame(columns = col) # 빈 데이터 프레임 생성
count = 0 # 항목 수 == 행의 개수
failc = 0 # 실패 항목
pageCount = 172 # 읽어 올 페이지 수 정하기
key = 'your-key-value' # api 키 값 설정
for j in range(0,pageCount):
    print('https://oapi.saramin.co.kr/job-search?access-key='+ key +'&start='+ str(j) +'&count=110&fields=posting-date,count,keyword-code,fields=keyword-code&job_mid_cd=2')
    response = requests.get('https://oapi.saramin.co.kr/job-search?access-key='+ key +'&start='+ str(j) +'&count=110&fields=posting-date,count,keyword-code,fields=keyword-code&job_mid_cd=2') # 오픈api 요청
    data = json.loads(response.text)
    if(j >= 400): # pageCount 변수로 일일 최대 호출 회수를 제한
        break
    for i in range(0, 110):
        try:
            df.loc[count] = [data['jobs']['job'][i]['id'],data['jobs']['job'][i]['active'],data['jobs']['job'][i]['url'],data['jobs']['job'][i]['company']['detail']['name'],data['jobs']['job'][i]['position']['title'],data['jobs']['job'][i]['position']['industry']['name'],
                  "'"+data['jobs']['job'][i]['position']['location']['code'],data['jobs']['job'][i]['position']['job-type']['code'],data['jobs']['job'][i]['position']['job-mid-code']['code'],"'"+data['jobs']['job'][i]['position']['job-code']['code'],
                  data['jobs']['job'][i]['keyword'],data['jobs']['job'][i]['position']['experience-level']['code'],data['jobs']['job'][i]['position']['experience-level']['min'],
                  data['jobs']['job'][i]['position']['experience-level']['max'],data['jobs']['job'][i]['position']['required-education-level']['code'],data['jobs']['job'][i]['position']['required-education-level']['name'],
                  data['jobs']['job'][i]['salary']['code'],data['jobs']['job'][i]['posting-date'],data['jobs']['job'][i]['read-cnt'],data['jobs']['job'][i]['apply-cnt']]
            count += 1
        except:
            failc += 1
            print("파싱 실패")
print(str(count)+"개 중 "+str(failc)+"개 실패 "+str(count-failc)+"개 파싱 완료")
df.to_csv('C:\\data\\testData1.csv',sep=',', encoding = 'UTF-8-sig',na_rep='NaN')


# name 은 값이 없는 경우가 있음
#data['jobs']['job'][0]['id']
#data['jobs']['job'][0]['active'] # 마감된 공고면 0
#data['jobs']['job'][0]['url'] # 공고 페이지
#data['jobs']['job'][0]['company']['detail']['name'] # 회사이름
#data['jobs']['job'][0]['position']['title'] # 공고 제목
#data['jobs']['job'][0]['position']['industry']['name'] # 업종 명
#data['jobs']['job'][0]['position']['location']['code'] # 지역 코드
#data['jobs']['job'][0]['position']['job-type']['code'] # 근무형태 코드
#data['jobs']['job'][0]['position']['job-mid-code']['code'] # 상위 직무 코드
#data['jobs']['job'][0]['position']['job-code']['code'] # 직무 코드
#data['jobs']['job'][0]['position']['experience-level']['name'] # 경력 이름 ** 없는 경우 때문에 삭제
#data['jobs']['job'][0]['position']['experience-level']['code'] # 경력 코드 예) 신입, 경력
#data['jobs']['job'][0]['position']['experience-level']['min'] # 최소 경력
#data['jobs']['job'][0]['position']['experience-level']['max'] # 최대 경력
#data['jobs']['job'][0]['position']['required-education-level']['code'] # 학력 코드
#data['jobs']['job'][0]['position']['required-education-level']['name'] # 학력
#data['jobs']['job'][0]['salary']['code'] # 연봉 코드
#data['jobs']['job'][0]['salary']['name'] # 연봉 ** 없는 경우 때문에 삭제
#data['jobs']['job'][0]['posting-date'] # 공고 등록일
#data['jobs']['job'][0]['read-cnt'] # 조회수
#data['jobs']['job'][0]['apply-cnt'] # 지원자
#data['jobs']['job'][0]['keyword'] # 직무 키워드
