import pandas as pd

# 데이터 불러오기
data = pd.read_csv("./data/data.csv")

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# 데이터프레임 확인
df.info()
