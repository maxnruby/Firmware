# zz_check_import.py
import sys
print("PYTHON:", sys.executable)

try:
    import serial, inspect
    print("IMPORT OK  | pyserial:", getattr(serial, "__version__", "?"),
          "| from:", inspect.getfile(serial))
except Exception as e:
    print("IMPORT FAIL:", repr(e))
    print("HINT: 이 파이썬에 pyserial 설치 필요 -> py -3.11 -m pip install --user pyserial")
    sys.exit(1)

try:
    sp = serial.Serial('COM4', 115200, timeout=1)
    print("OPEN OK    | COM4 opened")
except Exception as e:
    print("OPEN FAIL  |", repr(e))
