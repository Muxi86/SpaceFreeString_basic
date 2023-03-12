def remove_spaces(string: str)-> str:
    """
    Removes all spaces from a string of fixed length of 5 characters.

    Args:
        string (str): str
    Returns:
        str: string without spaces
    """
    # Your code here
    ans = ""
    idx = 0
    if string[0]!=" ":
        ans+=string[0]
    idx=+1
    if string[1]!=" ":
        ans+=string[1]
    idx+=1
    if string[2]!=" ":
        ans+=string[2]
    idx+=1
    if string[3]!=" ":
        ans+=string[3]
    idx=+1
    if string[4]!=" ":
        ans+=string[4]
    idx+=1
    return ans
print(remove_spaces('a b c'))