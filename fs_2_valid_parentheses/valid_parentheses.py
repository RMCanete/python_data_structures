def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    count = 0
    
    for p in parens:
        if p =='(' or p == ')':
            count += 1
    if count % 2 == 0:
        return True
    elif count % 2 != 0:
        return False
        
valid_parentheses("()()")
    # True
valid_parentheses("()(")
    # False
    
