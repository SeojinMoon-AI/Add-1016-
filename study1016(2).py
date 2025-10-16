import matplotlib.pyplot as plt
import numpy as np

# 1. 그래프를 그릴 x값의 범위를 생성합니다.
# -10부터 10까지 100개의 점을 생성합니다.
x = np.linspace(-10, 10, 100)

# 2. y = x^2 함수를 계산합니다.
# Python에서 제곱은 ** 연산자를 사용합니다.
y = x**2
# 2. y = x^3 함수를 계산합니다.
# Python에서 세제곱은 ** 연산자를 사용합니다.
y = x**3

# 3. 그래프를 생성하고 크기를 조절합니다.
plt.figure(figsize=(8, 6))

# 4. plot 함수를 사용하여 x, y 데이터를 그래프에 그립니다.
# 'color' 인자를 'red'로 설정하여 선 색상을 빨간색으로 지정합니다.
plt.plot(x, y, color='red', label='y = x^2')
plt.plot(x, y, color='red', label='y = x^3')

# y=x 함수를 파란색 점선으로 추가합니다.
# linestyle='--'는 점선을 의미합니다.
plt.plot(x, x, color='blue', linestyle='--', label='y = x')

# 5. 그래프의 제목과 축 레이블을 추가합니다.
plt.title('Graph of y = x^2 and y = x')
plt.title('Graph of y = x^3')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True) # 가독성을 위해 그리드를 추가합니다.
plt.legend()   # 범례를 표시합니다.

# 6. 그래프 창을 화면에 보여줍니다.
plt.show()
