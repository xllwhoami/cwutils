### Модуль time
*** 
```python
from cwutils import time

time.time_to_string(second)
```
> Конвертирует секунды(second) в недели, дни, часы, секунды (в зависимости сколько секунд вы написали в second.).

### Модуль memory
***
```python
from cwutils import memory

memory.memory_from_bytes('{{your number}} to {}KB, MB, GB, TB, PB, EB, ZB, UB}}'
```
> Конвентирует байты в KB, MB, GB, TB, PB, EB, ZB, UB (в зависимости от того что вы напишите после "to".).
```python
from cwutils import memory

memory.get_size_unit_in_bytes('{{{KB, MB, GB, TB, PB, EB, ZB, UB}}}')
```
> Возвращает размер 1 памятной единицы которую вы передали.
```python from cwutils import memory

memory.memory_from_string('(your number) KB, MB, GB, TB, PB, EB, ZB, UB')
```
> Тоже самое что и в 1. В "your number" напишите число, которые хотите конвертировать в KB, MB, GB, TB, PB, EB, ZB, UB.
 
```python 
from cwutils import memory
 
memory.get_size_unit(bytes)
```
> Возвращает макс.тип размерности кол-ва переданных байтов.

### Модуль nums
***
```python
from cwutils import nums

nums.num_to_string(your number)
```
> Конвертирует цифры в строчные цифры.
