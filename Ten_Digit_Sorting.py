def tens_place(num):
    return (num // 10) % 10

def ten_digit_sort(arr):
    arr.sort(key=lambda x: (tens_place(x), -x))
    return arr

print(ten_digit_sort([15, 11, 7, 19]))
print(ten_digit_sort( [2, 24, 22, 19]))
 