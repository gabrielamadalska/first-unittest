import random
from unittest.mock import Mock, patch


with patch('random.randint') as mock_random:
    mock_random.return_value = 4
    for i in range(5):
        print(random.randint(1,6))

print("Bez mockowania")
for i in range(5):
    print(random.randint(1,6))