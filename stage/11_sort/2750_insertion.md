numbers = [5 2 3 4 1]

| cycle | cycle < 5 | key = numbers[cycle] | index = cycle - 1 | index > -1 | numbers[index] > key | numbers[index + 1] == numbers[index] | 
| else -> break | numbers[index + 1] == key
| 1 | T | key = 2 | index = 0  | T | 5 > 2 | numbers[1] = 5 |           |                 | [5 5 3 4 1]
| 1 | T | key = 2 | index = -1 | F |       |                |           | numbers[0] == 2 | [2 5 3 4 1]

| 2 | T | key = 3 | index = 1  | T | 5 > 3 | numbers[2] = 5 |           |                 | [2 5 5 4 1]
| 2 | T | key = 3 | index = 0  | T | 2 > 3 |                | break     | numbers[1] == 3 | [2 3 5 4 1]

| 3 | T | key = 4 | index = 2  | T | 5 > 4 | numbers[3] = 5 |           |                  | [2 3 5 5 1]
| 3 | T | key = 4 | index = 1  | T | 3 > 4 | numbers[3] = 5 | break     | numbers[2] == 4  | [2 3 4 5 1]

| 4 | T | key = 1 | index = 3  | T | 5 > 1 | numbers[4] = 5 |           |                  | [2 3 4 5 5]
| 4 | T | key = 1 | index = 2  | T | 4 > 1 | numbers[3] = 4 |           |                  | [2 3 4 4 5]
| 4 | T | key = 1 | index = 1  | T | 3 > 1 | numbers[2] = 3 |           |                  | [2 3 3 4 5]
| 4 | T | key = 1 | index = 0  | T | 2 > 1 | numbers[1] = 2 |           |                  | [2 2 3 4 5]
| 4 | T | key = 1 | index = -1 | F |       |                |           | numbers[0] == 1  | [1 2 3 4 5]






