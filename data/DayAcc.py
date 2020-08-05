import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

dayold = pd.read_excel('C:/Users/박범진/Desktop/dayold2.xls', index_col='시군구', encoding='cp949')
daychild = pd.read_excel('C:/Users/박범진/Desktop/daychild2.xls', index_col='시군구', encoding='cp949')

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 노인 요일별
dayold2015 = dayold.loc['일요일':'토요일', ['서초구', '영등포구', '강남구','강서구','송파구']]
dayold2016 = dayold.loc['일요일.1':'토요일.1', ['서초구', '영등포구', '강남구','강서구','송파구']]
dayold2017 = dayold.loc['일요일.2':'토요일.2', ['서초구', '영등포구', '강남구','강서구','송파구']]
dayold2018 = dayold.loc['일요일.3':'토요일.3', ['서초구', '영등포구', '강남구','강서구','송파구']]
dayold2019 = dayold.loc['일요일.4':'토요일.4', ['서초구', '영등포구', '강남구','강서구','송파구']]

fig = plt.figure()
fig, ax = plt.subplots(2,3)

ax[0, 0].plot(dayold2015)
ax[0, 1].plot(dayold2016)
ax[0, 2].plot(dayold2017)
ax[1, 0].plot(dayold2018)
ax[1, 1].plot(dayold2019)

ax[0, 0].set_title('2015 노인 사고 건수')
ax[0, 1].set_title('2016 노인 사고 건수')
ax[0, 2].set_title('2017 노인 사고 건수')
ax[1, 0].set_title('2018 노인 사고 건수')
ax[1, 1].set_title('2019 노인 사고 건수')

ax[0, 0].set_ylabel('발생 건수')
ax[0, 1].set_ylabel('발생 건수')
ax[0, 2].set_ylabel('발생 건수')
ax[1, 0].set_ylabel('발생 건수')
ax[1, 1].set_ylabel('발생 건수')

# 어린이 요일별

daychild2015= daychild.loc['일요일':'토요일', ['서초구', '영등포구', '강남구','강서구','송파구']]
daychild2016= daychild.loc['일요일.1':'토요일.1', ['서초구', '영등포구', '강남구','강서구','송파구']]
daychild2017= daychild.loc['일요일.2':'토요일.2', ['서초구', '영등포구', '강남구','강서구','송파구']]
daychild2018= daychild.loc['일요일.3':'토요일.3', ['서초구', '영등포구', '강남구','강서구','송파구']]
daychild2019= daychild.loc['일요일.4':'토요일.4', ['서초구', '영등포구', '강남구','강서구','송파구']]

fig = plt.figure()
fig, ax = plt.subplots(2,3)

ax[0, 0].plot(daychild2015)
ax[0, 1].plot(daychild2016)
ax[0, 2].plot(daychild2017)
ax[1, 0].plot(daychild2018)
ax[1, 1].plot(daychild2019)

ax[0, 0].set_title('2015 어린이 사고 건수')
ax[0, 1].set_title('2016 어린이 사고 건수')
ax[0, 2].set_title('2017 어린이 사고 건수')
ax[1, 0].set_title('2018 어린이 사고 건수')
ax[1, 1].set_title('2019 어린이 사고 건수')

ax[0, 0].set_ylabel('발생 건수')
ax[0, 1].set_ylabel('발생 건수')
ax[0, 2].set_ylabel('발생 건수')
ax[1, 0].set_ylabel('발생 건수')
ax[1, 1].set_ylabel('발생 건수')

ax[1, 1].set_('발생 건수')




