import MeCab

mecabTagger = MeCab.Tagger()

def morphological(mail_list):
    print('morphological開始...')
    morphological_list = []
    pass_hinshi = ["BOS/EOS", "補助記号", "助詞", "記号", "助動詞"]

    for contents in mail_list:
        sentence = str(contents)

        node = mecabTagger.parseToNode(sentence)
        noun_cnt = {}

        while node:
            word = node.surface
            hinshi = node.feature.split(",")[0]
            if hinshi in pass_hinshi:
                pass
            elif word in noun_cnt.keys():
                noun_freq = noun_cnt[word][0]
                noun_cnt[word] = (noun_freq + 1, hinshi)
            else:
                noun_cnt[word] = (1, hinshi)
            node = node.next
        noun_cnt = sorted(noun_cnt.items(), key=lambda x:x[1], reverse=True)
        morphological_list.append(noun_cnt)

    return morphological_list

def convert_to_list(data):
    print('convert_to_list開始...')
    result = []
    for contents in data:
        result_content = []
        for word, (count, pos) in contents:
            result_content.append([word, count, pos])
        result.append(result_content)
    return result

"""
テスト用
test = ["私はPythonを学習しています。", "hello world"]
print(morphological(test))

test = [[('Python', (1, '名詞')), ('学習', (1, '名詞')), ('し', (1, '動詞')), ('い', (1, '動詞')), ('私', (1, '代名詞'))], [('hello', (1, '名詞')), ('world', (1, '名詞'))]]
print(convert_to_list(test))
"""