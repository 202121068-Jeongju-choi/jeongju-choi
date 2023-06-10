pip install control
import numpy as np
import matplotlib.pyplot as plt
import control

# 전달함수 G(s) 정의
num = [100] # 분자 계수
den = [1, 5, 6] # 분모 계수: s^2 + 5s + 6
G = control.TransferFunction(num, den)

# 폐루프 전달함수 T(s) 계산
H = 1  # 피드백 루프의 전달함수 (1이면 피드백이 없는 상태)
T = control.series(G, H)
T = control.minreal(T)  # 최소 실수화

print(T)

# 시간 벡터 생성
t = np.linspace(0, 10, 1000)

# Unit step 입력 생성
u = np.ones_like(t)

# 시스템 응답 계산
t, y = control.step_response(T, T=t, input=u)

# 응답곡선 그리기
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

# 주파수 응답 계산
omega, mag, phase = control.bode(T)

# 보드선도 그리기
plt.figure()
plt.semilogx(omega, mag)  # 주파수 응답의 크기
plt.xlabel('Frequency')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot - Magnitude')
plt.grid(True)

plt.figure()
plt.semilogx(omega, phase)  # 주파수 응답의 위상
plt.xlabel('Frequency')
plt.ylabel('Phase (degrees)')
plt.title('Bode Plot - Phase')
plt.grid(True)

plt.show()
