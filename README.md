# 서울집값예측모델

<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>  <img src="https://img.shields.io/badge/html-E34F26?style=flat-square&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/css-1572B6?style=flat-square&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=Heroku&logoColor=white"/>  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=PostgreSQL&logoColor=white"/> <img src="https://img.shields.io/badge/LigtGBM-F96F29?style=flat-square&logo=Microsoft&logoColor=white"/>   <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a><a href="https://colab.research.google.com/github/MINED30/House_price_prediction_LGBM/blob/main/notebook/05_Summary.ipynb" target="_parent\">
  

### *Feature*         

:zap: Used XGBoost to predict house price

:thumbsup: Tried 3 Models (Randomforest, XGBoost, LGBM)
  
:thumbsup: Low MAE, High R2 in test set (MAE = 1937.82, R2 = 0.9915)

:bar_chart: Various visualization for EDA & Model Intepretation

:computer:  Distribution with Flask & Heroku
  
:computer:  Database with SQL

:computer:  [WEB page](https://house-predction.herokuapp.com/)

:computer:  [Report](https://house-predction.herokuapp.com/)

  
최근 모든 자산가격이 상승하면서 집이 없던 사람들은 벼락거지가 되었다라는 말이 나오고 있습니다. 부동산에 많은 관심이 쏠린 지금, 집을 사고 파는 과정에서 생기는 부작용을 방지하고자 적정가를 제안하는 모델을 만들었습니다. 개인에게는 사기를 당하지 않도록하는 것이 이 서비스의 목적이며, 정부 및 기관에게는 집값담합을 방지하고 다운계약서가 작성된 거래를 색출해서 탈세를 막는데 목적이 있습니다.
  
### *Datasets* 
  
| 정보            | 수집한 지표                                                          | 출처                             |
|-----------------|----------------------------------------------------------------------|----------------------------------|
| 부동산관련 정보 | 지역코드, 법정동, 아파트, 전용면적, 층, 건축년도, 거래년도, 거래월   | 국토교통부 아파트매매 실거래자료 |
| 유동성관련지표  | 외국인증권투자, 국고채 10년(평균) , 회사채 3년(평균) , CD 91물(평균) | E-나라지표                       |
| 유동성관련지표  | DJI , IXIC , VIX , SSEC , DE30 , FCHI , NG, GC , CL , KRX            | FinanceData.KR                   |
| 물가관련지표    | 소비자물가 , 농축수산물 , 공업제품 , 공공서비스 , 근원물가           | E-나라지표, KOSIS 국가통계포털   |
| 인구관련지표    | 세대, 인구, 자동차등록, 인구이동(전입)                               | 서울 열린 데이터광장             |
| 인구관련지표    | 출생아수(명), 사망자수(명), 혼인건수(건), 이혼건수(건)               | KOSIS 국가통계포털               |
  

### Notebook
|filename|contents|
|---|---|
|House_price_prediction_01_DataCollection&Wrangling.ipynb | 데이터 수집 및 가공, 준비 |
|House_price_prediction_02_Exploratory_Data_Analysis.ipynb | 탐색적 데이터 분석|
|House_price_prediction_03_Model_CV.ipynb | 베이스라인 및 최종모델 선정 (LinearRegression, RandomForest, XGBoost, LightGBM)|
|House_price_prediction_04_Model_Interpretation.ipynb | 시각화를 통한 모델의 이해 (Feature Importance, PDP & ICE Curve, SHAP) |


## Schema
<img src="https://user-images.githubusercontent.com/73981982/112970972-b64d5300-9189-11eb-96ec-54df609c7be0.png" width="90%"/>

## Visualization
Notebook 폴더에서 EDA를 통한 시각화자료를 볼 수 있습니다.

예시 :

<img src="https://user-images.githubusercontent.com/73981982/116913901-020d8380-ac85-11eb-99ca-09f7a7420a30.png" width="45%"/> <img src="https://user-images.githubusercontent.com/73981982/116914333-91b33200-ac85-11eb-930c-2049432df032.png" width="45%"/>


## Page Intorduction
### Signin
<img src="https://user-images.githubusercontent.com/73981982/112858672-0d511a80-90ed-11eb-88e3-58b6f6db118a.png" width="60%"/>

Landing page는 로그인창입니다.

### Home
<img src="https://user-images.githubusercontent.com/73981982/112859018-66b94980-90ed-11eb-99e3-950eff378bff.png" width="60%"/>

로그인을 하면 Home으로 들어갑니다. 이 페이지에서는 댓글시스템을 구현하였습니다.

### House-Price-Prediction
<img src="https://user-images.githubusercontent.com/73981982/112859396-c0217880-90ed-11eb-8072-175a9f24ac9c.png" width="60%"/>

아파트 이름을 적으면 다음페이지로 가게 됩니다. (클릭시 확대)

<img src="https://user-images.githubusercontent.com/73981982/112859970-58b7f880-90ee-11eb-83f4-f14d8307625b.png" width="60%"/>

추가적인 사항을 기재하면 돌아가는 고양이화면이 뜨면서 모델이 예측을 수행합니다.

<img src="https://user-images.githubusercontent.com/73981982/112860012-64a3ba80-90ee-11eb-9dc9-75a0cc5fb5de.png" width="60%"/>

예측한 결과입니다.

### History
<img src="https://user-images.githubusercontent.com/73981982/112860358-b5b3ae80-90ee-11eb-9b83-fd53b593ffaf.png" width="60%"/>

히스토리 페이지는 예측을 했던 기록을 담는 페이지입니다.


## structure
<center><img src="https://user-images.githubusercontent.com/73981982/112858380-c400cb00-90ec-11eb-8bc0-8c1145a5b041.png" width="500"></center>



