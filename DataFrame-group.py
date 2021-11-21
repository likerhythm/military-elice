import pandas as pd
import numpy as np


def fuc_filter(x):
    # x그룹의 'day'의 평균이 250 초과면 True 반환
    return x['day'].mean() > 250

# 딕셔너리로 DF(soldier_df) 바로 만들기
soldier_dict = {
    'name': ['이재준', '최정민', '홍창호', '박지웅', '전대경'],
    'start': ['01/11', '02/01', '02/15', '02/15', '02/15'],
    'day': [314, 293, 279, 279, 279],
    'total': [545, 545, 548, 548, 548]
}

soldier_df = pd.DataFrame(soldier_dict)
# name을 인덱스로 설정
soldier_df = soldier_df.set_index('name')

print("딕셔너리로 바로 만든 DF\n", soldier_df)

# 명시적 인덱싱
print("\n", soldier_df.loc['최정민'])

# day 컬럼이 290보다 큰 행 출력
print("\nday 컬럼이 290보다 큰 행 출력\n", soldier_df[soldier_df['day'] > 290])
# 출력
# 이재준 01/11 314
# 최정민 02/01 293

# query 함수 이용해서 출력
print("\nquery 함수 이용해서 출력\n", soldier_df.query("day > 290"))

# DF에 데이터 추가
soldier_df.loc['조상우'] = ['11/10', 650, 650]
soldier_df.loc['이원재'] = ['03/21', 640, 640]
print(soldier_df)

# 시리즈도 연산자 사용 가능
soldier_df['percentage'] = soldier_df['day'] / soldier_df['total'] * 100
print(soldier_df['percentage'])

# 전역자 삭제
soldier_df.drop('이원재', axis = 0, inplace = True)
soldier_df.drop('조상우', axis = 0, inplace = True)
print(soldier_df)

# 각 열의 value 개수
print('\n각 열의 value 개수\n', soldier_df.count(axis = 0))

# 행 더 추가
soldier_df.loc['조상우'] = ['11/10', 650, 650, 100]
soldier_df.loc['이원재'] = ['03/21', 640, 640, 100]
soldier_df.loc['김건우'] = ['03/15', 240, 640, 240/640*100]
soldier_df.loc['유현준'] = ['05/29', 190, 610, 190/610*100]
soldier_df.loc['박근범'] = ['07/10', 105, 640, 105/640*100]
soldier_df['percentage'] = soldier_df['day'] / soldier_df['total'] * 100
print(soldier_df)

# 육해공 컬럼 추가
soldier_df['육해공'] = ['육군', '육군', '육군', '육군', '육군', '공군', '공군', '공군', '해군', '공군']
print(soldier_df)

# 육해공별로 그룹 나누기
print(soldier_df.groupby('육해공').sum())
# 육해공별로 묶고 그 중에서 컬럼별로 가장 작은 값과 가장 큰값을 출력
print(soldier_df.groupby('육해공').aggregate([min, max]))
# 육해공별로 묶고 각 그룹이 fuc_filter 함수를 만족하면 출력
print(soldier_df.groupby('육해공').filter(fuc_filter))
