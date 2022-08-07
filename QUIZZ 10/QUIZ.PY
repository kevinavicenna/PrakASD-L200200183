import re
regex = r'\b[A-Za-z0-9._%+-]+@[\w]+\.[A-Z|a-z]{2,}\b'


#email = input("Masukan email : ")
def RegexX(email):
    
    if(re.fullmatch(regex, email)):
        print("TRUE")
 
    else:
        print("FALSE")
 

if __name__ == '__main__':
    
    email = "fajri@ums.ac.id"
    RegexX(email)
 
    email = "fajri@student.ums.ac.id"
    RegexX(email)
 
    email = "fajri@ums.com"
    RegexX(email)
    
