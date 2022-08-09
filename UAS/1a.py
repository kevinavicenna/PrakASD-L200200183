import re

def RegexX(email):
    
    if(re.fullmatch('^[a-zA-Z]+@(?:[a-zA-Z]+\.)?ums\.ac.id$', email)):
        print("TRUE")
 
    else:
        print("FALSE")
 

if __name__ == '__main__':
    email = "kevin@ums.ac.id"
    RegexX(email)
 
    email = "kevin@student.ums.ac.id"
    RegexX(email)
 
    email = "kevin@ums.com"
    RegexX(email)
