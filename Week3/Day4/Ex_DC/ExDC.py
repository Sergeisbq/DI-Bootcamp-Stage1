from collections import Counter
text = "A good book would sometimes cost as much as a good house."
text_2 = text.lower()

split_text = text_2.split()
split_text_list = list(split_text)


class Text_analize():
        split_text = text_2.split()
        Counter = Counter(split_text)
        most_common_w = Counter.most_common(4)
        print(most_common_w)


        def uniq_words():
                uniq_words_list = {}
                for i in range(len(split_text)):
                    if split_text[i] not in uniq_words_list:
                        uniq_words_list[split_text[i]] = 1
                    elif split_text_list[i] in uniq_words_list:
                        uniq_words_list[split_text[i]] += 1
                uniq_words_list_sorted = dict(sorted(uniq_words_list.items(), key=lambda item: item[1], reverse=True))
                print(uniq_words_list_sorted)
                uniq_words_list_output = []
                uniq_words_list_output = list(uniq_words_list.keys())
                print(uniq_words_list_output)
        
Text_analize.uniq_words()  


filename = 'the_stranger.txt'

with open(filename, 'r') as file:
    text = file.read()
    text_lines = file.readlines()

def get_words_from_file():
    with open(filename, 'r') as file:
        text_lines = file.readlines()
    return text_lines

get_words_from_file()

                    
                        
        

