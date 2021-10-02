### Модуль time
*** 
```python
from cwutils import time

time.time_to_string(second)
```
> Конвертирует секунды(second) в недели, дни, часы, секунды (в зависимости сколько секунд вы написали в second.). **#1**

### Модуль memory
***
**#1**
```python
from cwutils import memory

memory.memory_from_bytes((your number) to (KB, MB, GB, TB, PB, EB, ZB, UB)
```
> Конвентирует байты в KB, MB, GB, TB, PB, EB, ZB, UB (в зависимости от того что вы напишите после "to".).
**#2**
```python
from cwutils import memory

memory.get_size_unit_in_bytes('KB, MB, GB, TB, PB, EB, ZB, UB')
```
> Конвертирует KB, MB, GB, TB, PB, EB, ZB, UB в байты. 
**#3**
```python from cwutils import memory

memory.memory_from_string('(your number) KB, MB, GB, TB, PB, EB, ZB, UB')
```
> Тоже самое что и #1. В "your number" напишите число, которые хотите конвертировать в KB, MB, GB, TB, PB, EB, ZB, UB.
