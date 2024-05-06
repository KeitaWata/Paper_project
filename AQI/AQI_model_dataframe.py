import pandas as pd

#データフレームを指定してAQIの値を追加する関数
def AQI_model_dataframe(data):
  df = data
  material = ["co","so2","pm25","pm10","o3","no2"]
  #この物質はppdからppmに変換が必要なため、一旦分ける
  material_ppd = ["so2","no2","o3"]
  index_low = [0,51,101,151,201,301,401]
  index_high = [50,100,150,200,300,400,500]
  list_title = ["aqi_co","aqi_so2","aqi_pm25","aqi_pm10","aqi_o3_1","aqi_no2"]
  aqi_co,aqi_so2,aqi_pm25,aqi_pm10,aqi_o3_1,aqi_no2 = [],[],[],[],[],[]
  lists = [aqi_co,aqi_so2,aqi_pm25,aqi_pm10,aqi_o3_1,aqi_no2]

  #material以外の項目を抽出し、後で結合する
  #取得したデータの詳しい情報などの記載がないため、感覚で計算を行う
  df_date = df.drop(material,axis=1)
  df = df[material]
  for x in material_ppd:
    df[x] = df[x] * 0.001
  df["co"] = df["co"] * 0.1
  
  for i in material:
    for element in df[i]:
      if i == "co":
        co_aqi_model(element,index_low,index_high,aqi_co)
      elif i == "so2":
        so2_aqi_model(element,index_low,index_high,aqi_so2)
      elif i == "pm25":
        pm25_aqi_model(element,index_low,index_high,aqi_pm25)
      elif i == "pm10":
        pm10_aqi_model(element,index_low,index_high,aqi_pm10)
      elif i == "o3":
        # o3_8_aqi_model(element,index_low,index_high,aqi_o3_8)
        o3_1_aqi_model(element,index_low,index_high,aqi_o3_1)
      elif i == "no2":
        no2_aqi_model(element,index_low,index_high,aqi_no2)
        

  for y,x in enumerate(list_title):
    df[x] = lists[y]
  
  
  df["AQI_total"] = df[["aqi_co","aqi_so2","aqi_pm25","aqi_pm10","aqi_o3_1","aqi_no2"]].max(axis='columns')
  df_all = pd.concat([df_date,df],axis=1)
  return df_all
  
  
#coのモデル
def co_aqi_model(value,index_low,index_high,aqi_co):
  if value == "NaN":
    aqi_co.append(0)
  elif value >= 0 and value < 4.5:
    aqi_co.append(round((index_high[0]-index_low[0])/(4.4)*(value) + index_low[0]))
  elif value >= 4.5 and value < 9.5:
    aqi_co.append(round((index_high[1]-index_low[1])/(9.4-4.5)*(value-4.5) + index_low[1]))
  elif value >= 9.5 and value < 12.5:
    aqi_co.append(round((index_high[2]-index_low[2])/(12.4-9.5)*(value-9.5) + index_low[2]))
  elif value >= 12.5 and value < 15.5:
    aqi_co.append(round((index_high[3]-index_low[3])/(15.4-12.5)*(value-12.5) + index_low[3]))
  elif value >= 15.5 and value < 30.5:
    aqi_co.append(round((index_high[4]-index_low[4])/(30.4-15.5)*(value-15.5) + index_low[4]))
  elif value >= 30.5 and value < 40.5:
    aqi_co.append(round((index_high[5]-index_low[5])/(40.4-30.5)*(value-30.5) + index_low[5]))
  elif value >= 40.5:
    if round((index_high[6]-index_low[6])/(50.4-40.5)*(value-40.5) + index_low[6]) > 500:
      aqi_co.append(500)
    else:
      aqi_co.append(round((index_high[6]-index_low[6])/(50.4-40.5)*(value-40.5) + index_low[6]))
  return aqi_co


#so2のモデル
def so2_aqi_model(value,index_low,index_high,aqi_so2):
  if value == "NaN":
    aqi_so2(0)
  elif value >= 0 and value < 0.035:
    aqi_so2.append(round((index_high[0]-index_low[0])/(0.034)*(value) + index_low[0]))
  elif value >= 0.035 and value < 0.145:
    aqi_so2.append(round((index_high[1]-index_low[1])/(0.144-0.035)*(value-0.035) + index_low[1]))
  elif value >= 0.145 and value < 0.225:
    aqi_so2.append(round((index_high[2]-index_low[2])/(0.224-0.145)*(value-0.145) + index_low[2]))
  elif value >= 0.225 and value < 0.305:
    aqi_so2.append(round((index_high[3]-index_low[3])/(15.4-0.225)*(value-0.225) + index_low[3]))
  elif value >= 0.305 and value < 0.605:
    aqi_so2.append(round((index_high[4]-index_low[4])/(0.604-0.305)*(value-0.305) + index_low[4]))
  elif value >= 0.605 and value < 0.805:
    aqi_so2.append(round((index_high[5]-index_low[5])/(0.804-0.605)*(value-0.605) + index_low[5]))
  elif value >= 0.805:
    if round((index_high[6]-index_low[6])/(1.004-0.805)*(value-0.805) + index_low[6]) > 500:
      aqi_so2.append(500)
    else:
      aqi_so2.append(round((index_high[6]-index_low[6])/(1.004-0.805)*(value-0.805) + index_low[6]))
  return aqi_so2

#pm25モデル
def pm25_aqi_model(value,index_low,index_high,aqi_pm25):
  if value == "0":
    aqi_pm25(0)
  elif value >= 0 and value < 15.5:
    aqi_pm25.append(round((index_high[0]-index_low[0])/(15.4)*(value) + index_low[0]))
  elif value >= 15.5 and value < 40.5:
    aqi_pm25.append(round((index_high[1]-index_low[1])/(40.4-15.5)*(value-15.5) + index_low[1]))
  elif value >= 40.5 and value < 65.5:
    aqi_pm25.append(round((index_high[2]-index_low[2])/(65.4-40.5)*(value-40.5) + index_low[2]))
  elif value >= 65.5 and value < 150.5:
    aqi_pm25.append(round((index_high[3]-index_low[3])/(150.4-65.5)*(value-65.5) + index_low[3]))
  elif value >= 150.5 and value < 250.5:
    aqi_pm25.append(round((index_high[4]-index_low[4])/(250.4-150.5)*(value-150.5) + index_low[4]))
  elif value >= 250.5 and value < 350.5:
    aqi_pm25.append(round((index_high[5]-index_low[5])/(350.4-250.5)*(value-250.5) + index_low[5]))
  elif value >= 350.5:
    if round((index_high[6]-index_low[6])/(500.4-350.5)*(value-350.5) + index_low[6]) > 500:
      aqi_pm25.append(500)
    else:
      aqi_pm25.append(round((index_high[6]-index_low[6])/(500.4-350.5)*(value-350.5) + index_low[6]))
  return aqi_pm25

#pm10モデル

def pm10_aqi_model(value,index_low,index_high,aqi_pm10):
  if value == "NaN":
    aqi_pm10(0)
  elif value >= 0 and value < 55:
    aqi_pm10.append(round((index_high[0]-index_low[0])/(54)*(value) + index_low[0]))
  elif value >= 55 and value < 155:
    aqi_pm10.append(round((index_high[1]-index_low[1])/(154-55)*(value-55) + index_low[1]))
  elif value >= 155 and value < 255:
    aqi_pm10.append(round((index_high[2]-index_low[2])/(254-155)*(value-155) + index_low[2]))
  elif value >= 255 and value < 355:
    aqi_pm10.append(round((index_high[3]-index_low[3])/(354-255)*(value-255) + index_low[3]))
  elif value >= 355 and value < 425:
    aqi_pm10.append(round((index_high[4]-index_low[4])/(424-355)*(value-355) + index_low[4]))
  elif value >= 425 and value < 505:
    aqi_pm10.append(round((index_high[5]-index_low[5])/(504-425)*(value-425) + index_low[5]))
  elif value >= 505:
    if round((index_high[6]-index_low[6])/(604-505)*(value-505) + index_low[6]) > 500:
      aqi_pm10.append(500)
    else:
      aqi_pm10.append(round((index_high[6]-index_low[6])/(604-505)*(value-505) + index_low[6]))
  return aqi_pm10


# #o3_8hバージョンのモデル
# def o3_8_aqi_model(value,index_low,index_high,aqi_o3_8):
#   value = value/8
#   if value >= 0 and value < 0.060:
#     aqi_o3_8.append(round((index_high[0]-index_low[0])/(0.059)*(value) + index_low[0]))
#   elif value >= 0.060 and value < 0.076:
#     aqi_o3_8.append(round((index_high[1]-index_low[1])/(0.075-0.060)*(value-0.060) + index_low[1]))
#   elif value >= 0.076 and value < 0.096:
#     aqi_o3_8.append(round((index_high[2]-index_low[2])/(0.095-0.076)*(value-0.076) + index_low[2]))
#   elif value >= 0.096 and value < 0.116:
#     aqi_o3_8.append(round((index_high[3]-index_low[3])/(0.115-0.096)*(value-0.096) + index_low[3]))
#   elif value >= 0.116 and value < 0.375:
#     aqi_o3_8.append(round((index_high[4]-index_low[4])/(0.374-0.116)*(value-0.116) + index_low[4]))
#   elif value >= 0.375:
#     aqi_o3_8.append(0)
#   return aqi_o3_8

#o3_1hバージョンのモデル
def o3_1_aqi_model(value,index_low,index_high,aqi_o3_1):
  if value == "NaN":
    aqi_o3_1(0)
  if value >= 0 and value < 0.125:
    aqi_o3_1.append(0)
  elif value >= 0.125 and value < 0.165:
    aqi_o3_1.append(round((index_high[2]-index_low[2])/(0.164-0.125)*(value-0.125) + index_low[2]))
  elif value >= 0.165 and value < 0.205:
    aqi_o3_1.append(round((index_high[3]-index_low[3])/(0.204-0.165)*(value-0.165) + index_low[3]))
  elif value >= 0.205 and value < 0.405:
    aqi_o3_1.append(round((index_high[4]-index_low[4])/(0.404-0.205)*(value-0.205) + index_low[4]))
  elif value >= 0.405 and value < 0.505:
    aqi_o3_1.append(round((index_high[5]-index_low[5])/(0.504-0.405)*(value-0.405) + index_low[5]))
  elif value >= 0.505:
    if round((index_high[6]-index_low[6])/(0.604-0.505)*(value-0.505) + index_low[6]) > 500:
      aqi_o3_1.append(500)
    else:
      aqi_o3_1.append(round((index_high[6]-index_low[6])/(0.604-0.505)*(value-0.505) + index_low[6]))
  return aqi_o3_1

#no2モデル
def no2_aqi_model(value,index_low,index_high,aqi_no2):
  if value == "NaN":
    aqi_no2(0)
  elif value >= 0 and value < 0.65:
    aqi_no2.append(0)
  elif value >= 0.65 and value < 1.25:
    aqi_no2.append(round((index_high[4]-index_low[4])/(1.24-0.65)*(value-0.65) + index_low[4]))
  elif value >= 1.25 and value < 1.65:
    aqi_no2.append(round((index_high[5]-index_low[5])/(0.204-1.25)*(value-1.25) + index_low[5]))
  elif value >= 1.65:
    if round((index_high[6]-index_low[6])/(2.04-1.65)*(value-1.65) + index_low[6]) > 500:
      aqi_no2.append(500)
    else:
      aqi_no2.append(round((index_high[6]-index_low[6])/(2.04-1.65)*(value-1.65) + index_low[6]))
  return aqi_no2