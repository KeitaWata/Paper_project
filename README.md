# 卒論：大気汚染物質の地域別特徴抽出と⻑期的予測システムの構築

## 研究の目的
- 下の図のような、将来的な大気汚染問題解決に向けての一つの指標となるための⻑期的な予測モデル構築を行うために, 複数の都市の7つの大気汚染に関する目的変数を用いて, 選抜した予測モデルにて予測した値と観測された値から予測精度を求め, 最適な予測モデルを構築することにより大気汚染に纏わる個人単位から、組織まで幅広い場所へと支援するようなモデルを作成することを目的とした。

<img width="849" alt="スクリーンショット 2024-05-26 15 47 25" src="https://github.com/KeitaWata/Paper_project/assets/74957678/160325fc-e85b-4121-8ef7-914246aad268">


## 予測方法
以下の３つカテゴリーごとに1週間単位と1日単位での予測を行う
> - 自己回帰モデル
> - Prophet
> - CNNとLSTM

また、予測精度を測る手法として2019年1月1日から2022年11月2日までのデータを訓練・検証データとし予測値を抽出し、2022年11月3日から2023年11月3日の1年間の過去のデータとMAPEという予測精度をはかる方法を用いる

## 実行環境
- Google Colaboratory

## 使用データ
- [The World Air Quality Index project](https://aqicn.org/contact/)によって提供されている,[Air Quality Open Data Platform Worldwide COVID-19 dataset](https://aqicn.org/data-platform/covid19/)から2019年1月1日から2023年11月3日までの、日本のTokyoとインドのDelhiの2都市に絞りつつ6つの大気汚染物質(PM2.5,PM10,SO2,CO,NO2,O3)と湿度、気圧、気温、降水量、風速のデータを用いる

## 使用ライブラリ
- pandas
- numpy
- os
- matplotlib
- statsmodels
- pmdarima
- sys
- seaborn
- increment_lineno
- optuna
- prophet

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
├── Deep_learning_model.ipynb(Non-public)
├── Prophet_model.ipynb
├── data
│   ├── city_aqi_data
│   │   ├── Delhi_AQI.csv
│   │   └── Tokyo_AQI.csv
│   ├── explanatory_variables
│   │   ├── Delhi_explanatory_variables.csv
│   │   └── Tokyo_explanatory_variables.csv
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
- ローカル上にてリモートリポジトリに反映させないファイルとフォルダを指定

## フォルダーの説明

### AQI
- AQI_model_dataframe.pyファイル(AQI値を算出するファイル)を入れたフォルダ

### data

- city_aqi_data・・Data_preprocessing_city&AQI_2.ipynbで作成したcsvデータを保存する場所
- explanatory_variables・・Data_feature＆Missing_value_imputation_3.ipynbで利用する説明変数データを保存する場所
- traninig_validation_test_data・・Data_feature＆Missing_value_imputation_3.ipynbで作成した予測する値を学習させるためのデータを保存する場所

### result

- data・・MAPE、Prophet、data_features、深層学習(CNN&LSTM)、自己回帰(Autoregressive)の５つのカテゴリーの出力結果をcsvデータとして保存する場所
- graph・・AQI、Prophet、data_features、深層学習(CNN&LSTM)、自己回帰(Autoregressive)の５つのカテゴリーのグラフを保存する場所
- parameta・・Autoregressive_model.ipynbで抽出したパラメータを保存する場所
