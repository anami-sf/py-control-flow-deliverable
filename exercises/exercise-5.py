# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
fib_sequence = [0, 1]

print('term: 0 / number: 0\nterm: 1 / number: 1')
idx = 2
while idx < 51:
    prev = idx-2
    current = idx-1
    next_fib = fib_sequence[prev] + fib_sequence[current]
    fib_sequence.append(next_fib)
    print(f'term: {idx} / number: {next_fib}')
    idx += 1
