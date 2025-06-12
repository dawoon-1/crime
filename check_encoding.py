import chardet  # 여기서 chardet 라이브러리 임포트

filename = 'crime_data.csv'

with open(filename, 'rb') as f:
    rawdata = f.read(10000)  # 앞 10,000바이트 읽기

result = chardet.detect(rawdata)
encoding = result['encoding']

print(f"추측된 인코딩: {encoding}")
print(f"신뢰도: {result['confidence']}")
