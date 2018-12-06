def armStrong(num):
    """armStrong(num) --> it will return True if num is an armstrong number.
        else it will return False."""
            
    #num = int(input("Enter a number : ")) #123456
    num_copy = num 
    num_of_digits = 0 
    while num_copy : #1
        num_of_digits += 1 #num_of_digits = 6
        num_copy = num_copy // 10  #0
    #print(f"Total num of digits in {num} are {num_of_digits}")  

    num_copy = num #123456
    arg_num = 0
    while num_copy :#123456
        last_digit = num_copy  % 10  #123456 % 10 --> 6
        arg_num = arg_num + last_digit ** num_of_digits # 0 + 6 ** 6 
        num_copy = num_copy // 10 #123456 // 10 --> 12345

    #print(f"Original Number {num} ")
    #print(f"Resulted Number {arg_num}")

    if num == arg_num : 
        #print(f"Congratulations number {num} an armstrong number")
        return True
    else : 
        #print(f"Given number {num} is not an armstrong number ")
        return False
