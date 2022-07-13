def content_validity(my_input):
    
    count = 0
    for value in my_input:
        if value.isalpha():
            count += 1
            
    if count >= len(my_input) // 2:
        return True
    else:
        return False


def sender_validity(my_input):
    
    for value in my_input:
        if value.isalpha():
            return True
        
    return False



if __name__ == '__main__':

    sender = input("ID:")
    content = input("content:")


    if sender_validity(sender) and content_validity(content):
        print("Not spam")
        
    elif sender_validity(sender) == False and content_validity(content) == True:
        print("Invalid sender")
        
    elif sender_validity(sender) and (not content_validity(content)):
        print("Invalid content")
        
    else:
        print("Invalid")