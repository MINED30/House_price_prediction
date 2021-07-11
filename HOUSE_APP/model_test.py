import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv('seoul_houses.csv')
df = data.copy()
df = df.drop(columns=['Unnamed: 0','거래일'])
num_feature = ['세대','인구','자동차등록','인구이동(전입지별)',
               '출생아수(명)', '사망자수(명)' ,'혼인건수(건)','이혼건수(건)']
for col in num_feature:
  df[col] = df[col].str.replace(",","").astype(int)
df['평당가'] = df['거래금액'] / df['전용면적']
df['거래횟수'] = [1]*len(df.index)

## 구별K 선정
from sklearn.cluster import KMeans
구별랭킹 = pd.concat([df.groupby('지역코드').mean()[['평당가','거래금액']].sort_values('평당가',ascending=False),                 
                      df.groupby('지역코드').sum()[['거래횟수']]],
                      axis = 1)
kmeans = KMeans(n_clusters=5)
kmeans.fit(구별랭킹)
구별랭킹['구별K'] = kmeans.labels_

## 매핑
gu_mapper = {gu:k for gu,k in zip(구별랭킹.index,구별랭킹.구별K)}
df['구별K'] = df['지역코드'].copy()
df['구별K'] = df['구별K'].replace(gu_mapper)

## 컬럼명 지정 및 drop
dataset = df.drop(columns=['거래횟수','평당가','지번','-\xa0집세'])
dataset.columns = ['지역코드', '법정동', '아파트', '전용면적', '층', '건축년도', '거래금액', '거래년도', '거래월일', '세대',
       '인구', '세대당인구', '자동차등록', '인구이동(전입지별)', '외국인증권투자', '국고채 3년(평균)',
       '국고채 5년(평균)', '국고채 10년(평균)', '회사채 3년(평균)', 'CD 91물(평균)', '콜금리(1일물,평균)',
       '소비자물가', '- 농축수산물', '- 공업제품', '- 공공서비스', '- 개인서비스', '근원물가', '출생아수(명)',
       '사망자수(명)', '혼인건수(건)', '이혼건수(건)', 'KS11', 'KQ11', 'DJI', 'IXIC', 'VIX',
       'CSI300', 'SSEC', 'DE30', 'FCHI', 'NG', 'GC', 'HG', 'CL', '구별K']

dataset = dataset.drop(columns=['세대당인구','국고채 3년(평균)','국고채 5년(평균)','- 개인서비스','콜금리(1일물,평균)','CSI300','HG'])

## engine함수
def engine(xxx):
  xxx['KRX'] = xxx.KS11 + xxx.KQ11
  xxx = xxx.drop(columns=['KS11','KQ11'])
  return xxx

## dataset에 적용
DF_1 = engine(dataset.copy())
DF_1.shape

dataset = DF_1

## 2021년 기준으로 분리
target='거래금액'
train = dataset[(dataset.거래월일 != '2021-01') | (dataset.거래월일 != '2021-02')].copy()
test = dataset[(dataset.거래월일 == '2021-01') | (dataset.거래월일 == '2021-02')].copy()
print(train.shape,test.shape)
print(test.거래월일.value_counts())

## 2021년 이전 데이터를 훈련, 검증셋으로 분리
X = train.drop(columns=target)
y = train[target]
X_test = test.drop(columns=target)
y_test = test[target]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

## 인코딩
encoder = OrdinalEncoder()
X_train_encoded = encoder.fit_transform(X_train)
X_val_encoded = encoder.transform(X_val)
X_test_encoded = encoder.transform(X_test)
