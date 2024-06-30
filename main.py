def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    
    i = 0
    
    while i<5:
        num = int(input('Enter a number: '))
        total += num
        i += 1
    print('Your total is: ', total)
    
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
