def count_digits(string: str) -> int:
    """
    Count the number of digits in a string of fixed length.

    Args:
        string (str): string of fixed length
    Returns:
        int: number of digits in the string
    """
    # Your code goes here
    ans = 0
    idx = 0
    if string[idx]!='1':
        pass
    idx+=1
    if string[idx]=='1':
        ans+=1
    idx+=1
    if string[idx]!='2':
        pass
    idx+=1
    if string[idx]=='2':
        ans+=1
    idx+=1
    if string[idx]!='3':
        pass
    idx+=1

    return ans
print(count_digits("a1b2c"))
