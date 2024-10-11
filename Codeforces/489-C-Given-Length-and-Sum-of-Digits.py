m, s = map(int, input().split())

# Case 1: Impossible to have a valid number
if s == 0 and m > 1 or s > 9 * m:
    print(-1, -1)
else:
    # Special case: when m == 1 and s == 0, the only valid number is 0
    if s == 0 and m == 1:
        print(0, 0)
    else:
        # Create the largest number
        largest = []
        sum_digits = s
        for i in range(m):
            digit = min(9, sum_digits)
            largest.append(str(digit))
            sum_digits -= digit

        # Create the smallest number by reversing largest
        smallest = largest[::-1]

        # Ensure no leading zero in smallest if m > 1 and s > 0
        if smallest[0] == '0':
            smallest[0] = '1'
            for i in range(1, m):
                if smallest[i] != '0':
                    smallest[i] = str(int(smallest[i]) - 1)
                    break

        print("".join(smallest), "".join(largest))
