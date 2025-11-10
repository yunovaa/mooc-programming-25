# Write your solution here

def find_words(search_term: str):
    with open('words.txt') as file:
        words = [word.strip() for word in file.readlines()]
        if '*' in search_term:
            if search_term.startswith('*'):
                return [word for word in words if word.endswith(search_term.split('*')[-1])]
            return [word for word in words if word.startswith(search_term.split('*')[0])]
        elif '.' in search_term:
            my_list = []
            for word in words:
                if len(word) == len(search_term):
                    for i in range(len(search_term)):
                        if search_term[i] == '.':
                            pass
                        elif word[i] != search_term[i]:
                            break
                        if i == len(search_term)-1:
                            my_list.append(word)
            return my_list

        elif search_term in words:
            return [search_term]
        return []


    
# print(find_words('ca..ot'))