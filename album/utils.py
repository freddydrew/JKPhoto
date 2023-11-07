import re 

def slugfiy(str):
    #to lower case, lose trailing/leading whitespace
    str = str.lower().strip() 
    #go through regexp patterns and replaces with spaces and dash
    str = re.sub(r'[^\w\s-]', '', str)
    str = re.sub(r'[\s_-]+', '-', str)
    str = re.sub(r'^-+|-+$', '', str)
    return str
