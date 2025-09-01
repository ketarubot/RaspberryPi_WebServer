import os
import platform
import datetime

print('=== Raspberry Pi System Info ===')
print(f'날짜: {datetime.datetime.now()}')
print(f'운영체제: {platform.system()} {platform.release()}')
print(f'아키텍처: {platform.machine()}')
print(f'파이썬 버전: {platform.python_version()}')
print(f'현재 사용자: {os.getlogin()}')
