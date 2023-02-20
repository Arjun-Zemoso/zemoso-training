def solve(document,keyword,thesaurus):
    synonym_list=[]
    count=0
    synonym_flag=True
    def search_word(key,document):
        for word in document.split(" "):
            if (key == word):
                if(synonym_flag == True):
                    nonlocal synonym_list
                    synonym_list.append(key)
                    return
                else:
                    nonlocal count
                    count += 1
    for synonym in thesaurus[keyword]:
        search_word(synonym, document)
    synonym_flag = False
    search_word(keyword,document)
    print(count)
    print(synonym_list)
