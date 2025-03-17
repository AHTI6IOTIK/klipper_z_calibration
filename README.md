<p align="center">
  <img src="https://repository-images.githubusercontent.com/365369551/ef2987a7-0faf-4844-91c9-f221e4112b4d" alt='Z-Calibration Logo' width='50%'>
  <h1 align="center">Automatic Z-Calibration</h1>
</p>

<p align="center">
It's like automatically baby-stepping on your 3D printer before every print, and the first layer will
always be perfect - no matter which nozzle or new flex-plate is being tested.
</p>

<p align="center">
  <a aria-label="Downloads" href="https://github.com/protoloft/klipper_z_calibration/releases">
    <img src="https://img.shields.io/github/release/protoloft/klipper_z_calibration?display_name=tag&style=flat-square">
  </a>
  <a aria-label="Stars" href="https://github.com/protoloft/klipper_z_calibration/stargazers">
    <img src="https://img.shields.io/github/stars/protoloft/klipper_z_calibration?style=flat-square">
  </a>
  <a aria-label="Forks" href="https://github.com/protoloft/klipper_z_calibration/network/members">
    <img src="https://img.shields.io/github/forks/protoloft/klipper_z_calibration?style=flat-square">
  </a>
  <a aria-label="License" href="https://github.com/protoloft/klipper_z_calibration/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/protoloft/klipper_z_calibration?style=flat-square">
  </a>
</p>

## Установка

Склонировать модуль рядом с исходниками klipper
```text
 git clone https://github.com/AHTI6IOTIK/klipper_z_calibration
```

Вызвать скрипт установки модуля
```bash
./klipper_z_calibration/install.sh 
```

## Пречеки

Для работы модуля необходимо определить конфигурация для датчика сопла Anycubic Kobra 2

```ini
[kobra_probe]
pin: PB12
```

## Конфигурация модуля calibrate_z

```ini
[z_calibration]
nozzle_xy_position: 60, 238
# по умолчанию из home_xy_position из safe_z_home
# Координаты X, Y (например, 100,100) сопла, нажимающего на ограничитель z.
switch_xy_position: 110,110 
# необязательно, если используется switch_xy_offsets
# координата X, Y (например, 100,100) корпуса переключателя зонда, щелчок по
# конечную точку z.

#switch_xy_offsets: 
#необязательно, если используется switch_xy_position
# Вместо абсолютного положения (switch_xy_position) эта конфигурация
# добавляет смещение по X, Y (например, -6,-18) к положению сопла.
bed_xy_position: 110, 110
#по умолчанию от нулевой_справочной_позиции (или относительного_справочного_индекса) bed_mesh
# Координаты X, Y (например, 100,100), по которым зондируется поверхность печати (например, центральная
# точка). Эти координаты корректируются
# смещениями зонда по X и Y. По умолчанию используется нулевая_справочная_позиция, которая
# заменяет устаревший индекс relative_reference_index
# сконфигурированной сетки bed_mesh, если она настроена. Можно изменить нулевую
# ссылочную позицию во время выполнения или использовать GCode-аргумент BED_POSITION из CALIBRATE_Z.
wiggle_xy_offsets: 0,1
# После зондирования сопла и втягивания переместите x на некоторое расстояние в сторону и
# обратно. Это полезно для предотвращения прилипания концевого штифта z к соплу и
# вытягивания из сборки. Может быть отрицательным. По умолчанию равно нулю, чтобы
# отключить его. Может быть объединен по x и y для перемещения по диагонали. Будьте осторожны
# чтобы не вывести сопло за пределы диапазона!
switch_offset: 0.02
# Смещение точки срабатывания используемого переключателя маг-зонда.
# При большем значении сопло будет располагаться ближе к станине.
# Это необходимо определить вручную. Подробнее об этом позже
# в этом разделе.
offset_margins: -2.0,4.0
# Минимальные и максимальные поля, допустимые для вычисленного смещения.
# Если смещение выходит за пределы этих значений, оно остановится!
# Поле может быть задано как "min,max", например "-0.5,1.5", или только одним
# значением, например "1.0", что переводится как "-1.0,1.0" (это также значение по умолчанию).
#max_deviation: 1,0
#DEPRECATED - пожалуйста, используйте вместо этого offset_margins!
# Максимально допустимое отклонение вычисленного смещения.
# Если смещение превысит это значение, оно остановится!
# По умолчанию 1,0 мм.
samples: 3
#по умолчанию из секции "probe:samples"
# Количество раз для зондирования каждой точки. Полученные значения z
# будут усреднены. По умолчанию задано в конфигурации зонда.
samples_tolerance: 1
#по умолчанию из раздела "probe:samples_tolerance"
# Максимальное расстояние по Z (в мм), на которое образец может отличаться от других
# образцов. По умолчанию задается в конфигурации датчика.
samples_tolerance_retries: 3
#по умолчанию из раздела "probe:samples_tolerance_retries"
# Количество повторных попыток, если найден образец, превышающий
# samples_tolerance. По умолчанию задается в конфигурации зонда.
samples_result: median
#default из раздела "probe:samples_result"
# Метод расчета при выборке более одного раза - либо
# "медиана" или "среднее" "median" or "average". По умолчанию из конфигурации зонда.
safe_z_height: 5
#по умолчанию 2 * z_offset из раздела "probe:z_offset"
# Абсолютное положение по оси z в мм, на которое следует переместиться перед переходом к следующей
# позицию. По умолчанию - двукратное значение z_смещения из конфигурации зонда
# конфигурации. Минимальная безопасная высота по z составляет 3 мм.



#clearance:
# УДАЛЕНО - вместо него используйте safe_z_height!
# Расстояние в мм, на которое нужно переместиться вверх перед переходом к следующей
# позицию. По умолчанию это расстояние в два раза больше, чем z_смещение от конфигурации зонда.
# конфигурации.
position_min:  -2
#значение по умолчанию из раздела "stepper_z:position_min".
# Минимальное допустимое расстояние (в мм), используемое для перемещения зонда. На
# по умолчанию из конфигурации Z-рейки.
speed: 50
# Скорость перемещения по X и Y. По умолчанию 50 мм/с.
lift_speed: 8
#значение по умолчанию из раздела "probe:lift_speed"
# Скорость (в мм/с) оси Z при подъеме зонда между
# образцами и перемещениями на просвет. По умолчанию задается в
# конфигурации.
probing_speed: 100
#по умолчанию из раздела "stepper_z:homing_speed".
# Быстрая скорость зондирования (в мм/с), используемая, когда функция probing_first_fast
# включена. По умолчанию используется конфигурация шины Z.
probing_second_speed: 2
#значение по умолчанию из раздела "stepper_z:second_homing_speed".
# Более медленная скорость (в мм/с) для зондирования записанных образцов.
# По умолчанию используется значение second_homing_speed для конфигурации Z-рейки.

probing_retract_dist: 3
#значение по умолчанию из раздела "stepper_z:homing_retract_dist".
# Расстояние для втягивания (в мм) перед зондированием следующего образца.
# По умолчанию используется значение homing_retract_dist из конфигурации Z-рейки.
# Внимание: если на оси Z используется бессенсорное самонаведение с
# homing_retract_dist, это значение должно быть больше нуля.
probing_first_fast: false
# Если значение равно true, то первое зондирование будет происходить быстрее на величину скорости зондирования.
# Это нужно для того, чтобы быстрее спуститься и не записывать результат как
# пробы зондирования. По умолчанию установлено значение false.

#start_gcode:
# Список команд G-Code для запуска перед каждой командой калибровки.
# Формат G-кода см. в файле docs/Command_Templates.md. Это может быть использовано для того, чтобы
# присоединения зонда.

#before_switch_gcode:
# Список команд G-кода для выполнения перед каждой калибровкой на
# mag-probe. Формат G-кода см. в файле docs/Command_Templates.md. Это может
# можно использовать для присоединения зонда после зондирования сопла и перед зондированием
# на маг-зонде.
#end_gcode:
# Список команд G-кода для выполнения после каждой команды калибровки.
# Формат G-кода см. в файле docs/Command_Templates.md. Это может быть использовано для того, чтобы
# отсоединения зонда после калибровки.
```

## Использование

В базовом варианте использования достаточно вызвать команду
```text
CALIBRATE_Z
```

Если датчик сопла отрегулирован в 0 с постелью и при тесте бумагой ее зажимает или сопло не касается бумаги.
То можно добавить смещение в + или в - до 1, пока не будет достигнут желаемый резултат.
```text
CALIBRATE_Z SWITCH_OFFSET=-0.02
```


## Благодарности

05tangens: за предоставленную конфигурацию исходного модуля z_calibrate

## Documentation

Visit the [Wiki](https://github.com/protoloft/klipper_z_calibration/wiki) to view the full documentation for this Klipper plugin.

The latest release notes are [here](https://github.com/protoloft/klipper_z_calibration/wiki/Changelog).

:pushpin: **And remember:** The smaller the switch-offset, the further the
 nozzle is away from the bed! :wink:

## Further Resources

A great how-to video by Kapman: [https://youtu.be/oQYHFecsTto](https://youtu.be/oQYHFecsTto)

### And if you are looking for an RRF version of this automatic z-offset calibration

You can find one [here](https://github.com/pRINTERnOODLE/Auto-Z-calibration-for-RRF-3.3-or-later-and-Klicky-Probe) from pRINTERnOODLE - This is really fantastic to see :tada:

## Thanks for all your feedback and support!

And if you like my work and want to support me, you can do so here:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X8X1C0DTD)

## Disclaimer

You use it at your onw risk! I'm not responsible for any damage that might result. Although,
this extension works rock solid for me and many others for years now. Always be careful
and double check everything when configuring or working with your printer. And as always,
never leave unattended while printing!
