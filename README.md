# 서울집값예측모델

<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>  <img src="https://img.shields.io/badge/html-E34F26?style=flat-square&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/css-1572B6?style=flat-square&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=Heroku&logoColor=white"/>  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=PostgreSQL&logoColor=white"/> <img src="https://img.shields.io/badge/LigtGBM-F96F29?style=flat-square&logo=Microsoft&logoColor=white"/>  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a><a href="https://colab.research.google.com/github/MINED30/House_price_prediction_LGBM/blob/main/notebook/05_Summary.ipynb" target="_parent\">
  
![image](https://user-images.githubusercontent.com/73981982/108994263-e6af5680-76de-11eb-99db-5d48fcb65172.png)

### *Feature*         

:zap: Uses Light GBM 

:thumbsup: Low MAE, High R2 in test set (MAE = 2805.28, R2 = 0.9917)

:computer:  [WEB page](https://house-predction.herokuapp.com/)



## Dataset
![image](https://user-images.githubusercontent.com/73981982/116913564-9d522900-ac84-11eb-9f85-0919af5f92f9.png)
2018.01 ~ 2021.02, 약 245,000건의 데이터

## Schema
![schema](https://user-images.githubusercontent.com/73981982/112970972-b64d5300-9189-11eb-96ec-54df609c7be0.png)

## Visualization
Notebook 폴더에서 EDA를 통한 시각화자료를 볼 수 있습니다.

예시 :

<img src="https://user-images.githubusercontent.com/73981982/116913901-020d8380-ac85-11eb-99ca-09f7a7420a30.png" width="45%"/>
<img src="https://user-images.githubusercontent.com/73981982/116914333-91b33200-ac85-11eb-930c-2049432df032.png" width="45%"/>


## Page Intorduction
### Signin
![image](https://user-images.githubusercontent.com/73981982/112858672-0d511a80-90ed-11eb-88e3-58b6f6db118a.png)

### Home
![image](https://user-images.githubusercontent.com/73981982/112859018-66b94980-90ed-11eb-99e3-950eff378bff.png)

### House-Price-Prediction
#### Searching
![image](https://user-images.githubusercontent.com/73981982/112859396-c0217880-90ed-11eb-8072-175a9f24ac9c.png)
![image](https://user-images.githubusercontent.com/73981982/112859970-58b7f880-90ee-11eb-83f4-f14d8307625b.png)
![image](https://user-images.githubusercontent.com/73981982/112860012-64a3ba80-90ee-11eb-9dc9-75a0cc5fb5de.png)

### History
![image](https://user-images.githubusercontent.com/73981982/112860358-b5b3ae80-90ee-11eb-9b83-fd53b593ffaf.png)




## structure
<center><img src="https://user-images.githubusercontent.com/73981982/112858380-c400cb00-90ec-11eb-8bc0-8c1145a5b041.png" width="500"></center>


![image](https://user-images.githubusercontent.com/73981982/108994263-e6af5680-76de-11eb-99db-5d48fcb65172.png)


## 파일 설명
- 01_Data_Wrangling.ipynb : 데이터 수집하고 랭글링, 특성공학을 진행
- 02_Exploratory_Data_Analysis.ipynb : 데이터셋을 시각화
- 03_LightGBM_CV.ipynb : 모델선정 및 하이퍼파라미터 튜닝
- 04_Interpretation.ipynb : 모델 Interpretation
- 05_Summary.ipynb : 모델 Intrepretation에서 시각화 못한것만 다시 시각화

## 목차
1. Background
2. Introduction
3. Analysis
4. Modeling
5. Prediction
6. Interpretation

