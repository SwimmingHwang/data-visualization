import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

accold = pd.read_excel('C:/Users/박범진/Desktop/accold.xls', index_col='시군구', encoding='cp949')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 차 대 사람 노인 교통사고 발생건수

carvsold= accold.loc[:, ['서초구', '영등포구', '강남구','강서구','송파구']]
plt.figure()
plt.xlabel('연도')
plt.ylabel('발생빈도')
plt.title('차 대 사람 노인 교통사고 발생건수')
carvsold.plot()