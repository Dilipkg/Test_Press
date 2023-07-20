'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Q1.
def reverse(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    input_str = input("Input: ")
    if 1 <= len(input_str) <= 100 and input_str.islower():
        output_str = reverse(input_str)
        print("Output:", output_str)
    else:
        print("Invalid input. The string must contain only lowercase characters and have a length between 1 and 100.")
        

#Q2
num = 12
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
 
    
#Q3
def largest_number(nums):
    nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
    return ''.join(nums)
if __name__ == "__main__":
    input = [54, 546, 548, 60]
    output = largest_number(input)
    print(output)    
    
#Q4.    
def reverse_number(n):
    return int(str(n)[::-1])
if __name__ == "__main__":
    N = int(input("Input: "))
    if 1 <= N <= 10000:
        reversed_number = reverse_number(N)
        print("Output:", reversed_number)
    else:
        print("Invalid input. N must be between 1 and 10000.")
        
        
#Q5.        
def minmax(nums):
     max = min = nums[0]
     for i in range(1, len(nums)):
         if nums[i] > max:
            max = nums[i]
         elif nums[i] < min:
            min = nums[i]
    print('The minimum element in the list is', min)
    print('The maximum element in the list is', max)
 if __name__ == '__main__':
    nums = [5, 7, 2, 4, 9, 6]
     minmax(nums)