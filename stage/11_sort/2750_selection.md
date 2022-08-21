numbers = [5 2 3 4 1 ]

| cycle | cycle < 4 | index = cycle + 1 | min_index = cycle | index < 5 | numbers[min_index] > numbers[index] | min_index = index | 
| mov_num = numbers[cycle] | was_min = numbers[min_index] | numbers[cycle] = was_min | numbers[min_index] = mov_num |

| 0 | T | index = 1 | min_index = 0 | T | 5 > 2 | T | min_index = 1 |
| 0 | T | index = 2 | min_index = 0 | T | 2 > 3 | F | min_index = 1 |
| 0 | T | index = 3 | min_index = 0 | T | 2 > 4 | T | min_index = 1 |
| 0 | T | index = 4 | min_index = 0 | T | 2 > 1 | T | min_index = 4 |
| mov_num = 5 | was_min = 1 | numbers[0] = 1 | numbers[4] = 5 | [1 2 3 4 5]

| 1 | T | index = 2 | min_index = 1 | T | 2 > 3 | F | min_index = 1 |
| 1 | T | index = 3 | min_index = 1 | T | 2 > 4 | F | min_index = 1 |
| 1 | T | index = 4 | min_index = 1 | T | 2 > 5 | F | min_index = 1 |
| mov_num = 2 | was_min = 2 | numbers[1] = 2 | numbers[1] = 2 | [1 2 3 4 5]

| 2 | T | index = 3 | min_index = 2 | T | 3 > 4 | F | min_index = 2 |
| 2 | T | index = 4 | min_index = 2 | T | 3 > 5 | F | min_index = 2 |
| mov_num = 3 | was_min = 3 | numbers[2] = 3 | numbers[2] = 3 | [1 2 3 4 5]

| 3 | T | index = 4 | min_index = 3 | T | 4 > 5 | F | min_index = 3 |
| mov_num = 4 | was_min = 4 | numbers[3] = 4 | numbers[3] = 4 | [1 2 3 4 5]