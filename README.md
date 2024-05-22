# 卒論：大気汚染物質の地域別特徴抽出と⻑期的予測システムの構築

## 実行環境
- Google Colaboratory

## 準備
- コードやデータをダウンロードし、Google Drive内にアップロード(詳しい手順は以下で説明)

## 手順
1. github上のファイルを全てダウンロードし、ローカル上にダウンロードする
1. Google Driveにて[raw_data.zip](https://drive.google.com/file/d/19VXMgNU3YvfschJpmFBeVSQ2uTI6dlRS/view?usp=drive_link)をダウンロードする
1. Paper_project_master(ルートディレクトリ)/dataフォルダー内にてraw_data.zipを解凍
1. ディレクトリーをGoogle Drive上にアップロードする
1. Data_preprocessing_1.ipynb → Data_preprocessing_city&AQI_2.ipynb → Data _feature＆Missing _value _imputation_3.ipynbを動かしてデータを学習できる状態にする
1. 手順5を踏んだ状態でAutoregressive_model.ipynb、Prophet_model.ipynbを動かすことで大気汚染物質の予測を行う(※近日中にDeeplearningモデルを公開予定) 

## ファイルの説明
###  Data_preprocessing_1.ipynb
- raw_dataフォルダーにて収集されている大気汚染データを

###  Data_preprocessing_city&AQI_2.ipynb
- 


###  README.md
- 作成したコードと各ファイルの説明
