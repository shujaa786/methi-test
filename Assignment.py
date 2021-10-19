class Scrapping():

    def extract_word(self, filename, dataset, value):
        page = open(filename,'r', encoding='utf-8')
        for line in page.readlines():
            for word in line.split():
                word = word.replace(',','').replace('(','').replace(')','').replace('"','').replace(":",'').replace('.','').replace('/','').replace('-','')
                word = word.lower() if not word.isnumeric() else None
                if word:
                    if word in dataset:
                        dataset[word].add(value)
                    else:
                        dataset[word] = {value}
        page.close()
    
    def remove_stopwords(self, filename, dataset):
        page = open(filename,'r', encoding='utf-8')
        for line in page.readlines():
            for word in line.split():
                del dataset[word]
    
    def save_data(self, filename, dataset):
        with open(filename,'w') as file:
            for key,val in sorted(dataset.items()) :
                data = f"{key}: {','.join(list(map(str,val)))}\n"
                file.writelines(data)
        

dataset = {}
obj = Scrapping()
obj.extract_word('page1.txt',dataset,1)
obj.extract_word('page2.txt',dataset,2)
obj.extract_word('page3.txt',dataset,3)
obj.remove_stopwords('exclude-words.txt',dataset)
obj.save_data('output.txt',dataset)
