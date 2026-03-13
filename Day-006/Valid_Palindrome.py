def isValid(self, s):
        
    stack = []
    links = { ")" : "(" ,"}" : "{" ,"]" : "["}

    for ch in s :
        if ch in links :
            if stack and stack[-1] == links[ch] :
                stack.pop()
            else :
                return False
            
        else :
            stack.append(ch)
        
    return True if not stack else False
