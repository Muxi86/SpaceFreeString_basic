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
    if string[idx]!=" ":
        ans+=string[idx]
    idx+=1
    if string[idx]!=" ":
        ans+=string[idx]
    idx+=1
    if string[idx]!=" ":
        ans+=string[idx]
    idx+=1
    if string[idx]!=" ":
        ans+=string[idx]
    idx+=1
    if string[idx]!=" ":
        ans+=string[idx]
    idx+=1

    return ans
print(remove_spaces('a b c'))