import serial  # импорт библиотеки для работы с последовательным портом
import time  # импорт библиотеки для работы с временными задержками
import serial.tools.list_ports  # импорт инструментов для получения списка доступных COM-портов
# список стандартных скоростей передачи данных
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
# получение списка доступных COM-портов на устройстве
ports = [p.device for p in serial.tools.list_ports.comports()]
# выбор первого доступного порта из списка
port_name = ports[0]
# выбор максимальной скорости передачи данных из списка speeds
port_speed = int(speeds[-1])
# установка таймаута для чтения данных из порта
port_timeout = 10
# инициализация последовательного порта с указанными параметрами
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)
# задержка на 1 секунду для стабилизации соединения
time.sleep(1)
# очистка входного буфера порта
ard.flushInput()
try:
    # чтение данных из порта
    msg_bin = ard.read(ard.inWaiting())
    # повторное чтение данных
    msg_bin += ard.read(ard.inWaiting())
    # ещё одно чтение данных
    msg_bin += ard.read(ard.inWaiting())
    # ещё одно чтение данных
    msg_bin += ard.read(ard.inWaiting())
    # декодирование бинарных данных в строку
    msg_str_ = msg_bin.decode()
    # вывод количества считанных байт
    print(len(msg_bin))
except Exception as e:
    # обработка исключений: вывод сообщения об ошибке
    print('Error!')
# закрытие последовательного порта
ard.close()
# задержка на 1 секунду перед завершением программы
time.sleep(1)
# вывод декодированной строки с данными
print(msg_str_)