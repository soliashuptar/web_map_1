def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    res = []
    with open(path, 'r') as file:
        for line in file:
            line_lst = []
            for let in line:
                line_lst.append(let)
            line_lst = line_lst[:-1]
            res.append(line_lst)
    return res

    
def row_extend(row):
    """
    list -> list

    Returns the extended row with sorted consonants by their frequency in the row.
    """
    trash = ["a", "e", "i", "o", "u", "y", " ", "A", "E", "I", "O", "U", "Y"]
    newrow = row
    lst = []
    for let in row:
        let = let.lower()
        if let not in trash and let.isalpha():
            lst.append(str(row.count(let)) + let)

    lst = list(set(lst))
    lst = sorted(lst, key=lambda x: x[0], reverse=True)
    for i in lst:
        newrow.append(i[1])

    return newrow



    
def column_extend(column):
    """
    list -> list

    Returns the extended column with sorted vowels without duplication.
    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    lst = []
    for el in column:
        el = el.lower()
        if el in vowels and el.isalpha():
            lst.append(el)

    lst = list(set(lst))
    lst.sort()

    return lst

def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and 
    outputs to the other file.
    """
    characters = input_data(in_path)
    max_len = max([len(i) for i in characters])
    result = []
    for i in range(max_len):
        col_lst = []
        for j in range(len(characters)):
            letter = characters[j][i]
            try:
                col_lst.append(letter)
            except:
                col_lst.append(" ")
        res = column_extend(col_lst)
        result.append(res)

    max_el = max(len(i) for i in result)
    for i in result:
        for j in range(max_el - len(i)):
            i.append(" ")

    text = ""
    for i in range(max_el):
        for j in range(len(result)):
            text += result[j][i]
        if i < max_el -1:
            text += '\n'
    newlst = []
    for i in characters:
        newlst.append(row_extend(i))
    fulltext = ""
    for i in newlst:
        fulltext += "".join(i) + "\n"
    fulltext += text
    print(fulltext)
    return result
print(characters_info("text.txt", "alo"))