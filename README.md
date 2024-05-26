# 卒論：大気汚染物質の地域別特徴抽出と⻑期的予測システムの構築

## 研究の目的
- 下の図のような、将来的な大気汚染問題解決に向けての一つの指標となるための⻑期的な予測モデル構築を行うために, 複数の都市の7つの大気汚染に関する目的変数を用いて, 選抜した予測モデルにて予測した値と観測された値から予測精度を求め, 最適な予測モデルを構築することにより大気汚染に纏わる個人単位から、組織まで幅広い場所へと支援するようなモデルを作成することを目的とした。

<img width="849" alt="スクリーンショット 2024-05-26 15 47 25" src="https://github.com/KeitaWata/Paper_project/assets/74957678/160325fc-e85b-4121-8ef7-914246aad268">


## 実行環境
- Google Colaboratory

## 使用データ
- [The World Air Quality Index project](https://aqicn.org/contact/)によって提供されている,[Air Quality Open Data Platform Worldwide COVID-19 dataset](https://aqicn.org/data-platform/covid19/)から2019年1月1日から2023年11月3日までの、日本のTokyoとインドのDelhiの2都市に絞りつつ6つの大気汚染物質(PM2.5,PM10,SO2,CO,NO2,O3)と湿度、気圧、気温、降水量、風速のデータを用いる

## 使用ライブラリ
- Pandas
- Numpy
- os
- matplotlib
- statsmodels
- pmdarima

## 準備
- コードやデータをダウンロードし、Google Drive内にアップロード(詳しい手順は以下で説明)

## 手順
1. github上のファイルを全てダウンロードし、ローカル上にダウンロードする
1. Google Driveにて[raw_data.zip](https://drive.google.com/file/d/19VXMgNU3YvfschJpmFBeVSQ2uTI6dlRS/view?usp=drive_link)をダウンロードする
1. Paper_project_master(ルートディレクトリ)/dataフォルダー内にてraw_data.zipを解凍
1. ディレクトリーをGoogle Drive上にアップロードする
1. 以下の手順でipynbファイルを実行する
> 1. Data_preprocessing_1.ipynb
> 2. Data_preprocessing_city&AQI_2.ipynb
> 3. Data _feature＆Missing _value _imputation_3.ipynb
6. 手順5を踏んだ状態でAutoregressive_model.ipynb、Prophet_model.ipynbを動かすことで大気汚染物質の予測を行う(※近日中にDeeplearningモデルを公開予定)

   
※**github上のファイルにて、手順5の３つのファイルを実行した状態のデータは揃っているため、すぐに予測したい方は手順1から手順6に進むことも可能**


## ディレクトリ構成図
<pre>
  .
├──  Data _feature＆Missing _value _imputation_3.ipynb
├── AQI
│   └───AQI_model_dataframe.py
├── Autoregressive_model.ipynb
├── Data_preprocessing_1.ipynb
├── Data_preprocessing_city&AQI_2.ipynb
├── Deep_learning_model.ipynb(unpublic)
├── Prophet_model.ipynb
├── data
│   ├── city_aqi_data
│   │   ├── Delhi_AQI.csv
│   │   └── Tokyo_AQI.csv
│   ├── explanatory_variables
│   │   ├── Delhi_explanatory_variables.csv
│   │   └── Tokyo_explanatory_variables.csv
│   ├── raw_data
│   │   ├── 2019
│   │   ├── 2020
│   │   ├── 2021
│   │   └── 2022_2023
│   └── traninig_validation_test_data
│       ├── Delhi_paper.csv
│       └── Tokyo_paper.csv
└── result
    ├── data
    │   ├── MAPE
    │   ├── Prophet
    │   ├── data_features
    │   ├── 深層学習
    │   └── 自己回帰
    ├── graph
    │   ├── AQI
    │   ├── Prophet
    │   ├── data_features
    │   ├── 深層学習
    │   └── 自己回帰
    └── parameta
</pre>


## ファイルの説明
###  Data_preprocessing_1.ipynb
- raw_dataフォルダーにて収集されている大気汚染データを1つのcsvファイルとしてまとめる

###  Data_preprocessing_city&AQI_2.ipynb
- Data_preprocessing_1.ipynbで作成したcsvファイルから、使用する目的変数と説明変数に絞りつつ、AQI値を算出したデータフレームを指定した国の都市ごとにcsvファイルを作成する
- csvデータ作成と同時にAQI値を時系列のグラフとして表示する

### Data_feature＆Missing_value_imputation_3.ipynb
- Data_preprocessing_city&AQI_2.ipynbで作成したファイル(data/city_aqi_dataフォルダー内のファイル)の欠損値処理を行うと同時に、6つの大気汚染物質とAQI値の特徴を掴むために変動成分、定常性、自己相関と説明変数と共に相関関係を調べる

### Autoregressive_model.ipynb
- Data_feature＆Missing_value_imputation_3.ipynbで作成したcsvファイルを元に、目的変数を用いて自己回帰モデルであるARIMAとSARIMAモデルと説明変数を用いて、ARIMAXとSARIMAXモデルの4つのモデルを用いて将来の大気汚染物質の値を予測する  

※**自己回帰モデルでは、1週間単位での予測のみを行っている**  
※**SARIMAXモデルに関しては、莫大な時間が掛かってしまうため注意が必要**

### Prophet_model.ipynb
- Prophetモデルを用いて1日単位と1週間単位の２つの大気汚染物質の値を予測する

###  README.md
- 作成したコードと各ファイルの説明

### .gitignore
- ローカル上にてリモートリポジトリに反映させないファイルとフォルダーを指定

## フォルダーの説明

### AQI
- AQI_model_dataframe.py

### data

### result
