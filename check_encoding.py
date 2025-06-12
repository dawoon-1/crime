import check_encoding

filename = 'crime_data.csv'

with open(filename, 'rb') as f:
    rawdata = f.read(10000)  # 앞 10,000바이트 정도만 읽음

result = check_encoding.detect(rawdata)
encoding = result['encoding']

print(f"추측된 인코딩: {encoding}")
print(f"신뢰도: {result['confidence']}")
