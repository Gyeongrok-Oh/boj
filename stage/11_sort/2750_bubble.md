N = 5
numbers = [5 2 3 4 1]

| cycle | cycle < 5 | index = cycle-1 | change_index = cycle | change_index < 5 | if numbers[index] > numbers[change_index] | numbers[index] , numbers[change_index] = numbers[change_index], numbers[index] |

| 1 | T | index = 1-1 = 0 | change_index = 1 | T | numbers[0] > numbers[1] -> 5 > 2 -> T | 5,2,3,4,1 -> 2,5,3,4,1 |
| 1 | T | index = 1-1 = 0 | change_index = 2 | T | numbers[0] > numbers[2] -> 2 > 3 -> F | 2,5,3,4,1 |
| 1 | T | index = 1-1 = 0 | change_index = 3 | T | numbers[0] > numbers[3] -> 2 > 4 -> F | 2,5,3,4,1 |
| 1 | T | index = 1-1 = 0 | change_index = 4 | T | numbers[0] > numbers[4] -> 2 > 1 -> T | 2,5,3,4,1 -> 1,5,3,4,2 |

| 2 | T | index = 2-1 = 1 | change_index = 2 | T | numbers[1] > numbers[2] -> 5 > 3 -> T | 1,5,3,4,2 -> 1,3,5,4,2 |
| 2 | T | index = 2-1 = 1 | change_index = 3 | T | numbers[1] > numbers[3] -> 3 > 4 -> F | 1,3,5,4,2 |
| 2 | T | index = 2-1 = 1 | change_index = 4 | T | numbers[1] > numbers[4] -> 3 > 2 -> T | 1,3,5,4,2 -> 1,2,5,4,3 |

| 3 | T | index = 3-1 = 2 | change_index = 3 | T | numbers[2] > numbers[3] -> 5 > 4 -> T | 1,2,5,4,3 -> 1,2,4,5,3 |
| 3 | T | index = 3-1 = 2 | change_index = 4 | T | numbers[2] > numbers[4] -> 4 > 3 -> T | 1,2,4,5,3 -> 1,2,3,5,4 |

| 4 | T | index = 4-1 = 3 | change_index = 4 | T | numbers[3] > numbers[4] -> 5 > 4 -> T | 1,2,3,5,4 -> 1,2,3,4,5 |


