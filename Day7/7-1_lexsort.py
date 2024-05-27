import numpy as np

ndarray1 = np.array([1, 5, 1, 4, 3])
ndarray2 = np.array([9, 4, 0, 4, 0])
# 0, 0, 4, 4, 9 -> 2, 0, 4, 3, 1
# ndarray2 배열을 기준으로 오름차순으로 정렬하고 동일한 값의 경우
# ndarray1 배열의 기준으로 오름차순 한 인덱스를 반환

result = np.lexsort((ndarray2, ndarray1))
print(result)

# ndarray1 정렬 : 1,1,3,4,5 -> 겹치는 1중 ndarray2순서로는 2가 더 큼
# 결과 2,0,4,3,1