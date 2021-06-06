def freq_counter(num):
    count = {}
    
    for c in num:
        count[c] = count.get(c, 0) + 1
    
    return count
    
freq_counter([1,2,3,2,5,4,4])
    # {1:1.2:2.3:1.5:1,4:2}

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    return freq_counter(str(num1)) == freq_counter(str(num2))
    
same_frequency(551122, 221515)
    # True
    
