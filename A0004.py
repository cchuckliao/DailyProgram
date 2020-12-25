# 统计一个纯文本里面各个单词的出现次数


def count_words_from_text(file_dir):
    with open(file_dir) as text_file:
        text = text_file.readlines()
        words_list = []
        for line in text:
            a = line.replace('\n', '')  # replace不改变原内容
            b = a.replace(',', '')
            c = b.replace('.', '')
            d = c.replace('(', ' ')
            e = d.replace(')', ' ')
            line_words = e.split(' ')  # 没有考虑更多的其它符号的处理，可能需要用到re库。
            words_list += line_words
        words_set = set(words_list)
        words_set.remove('')
        words_count = {}

        for num, word in enumerate(words_set):  # enumerate会产生一个序号和元素，要用两个变量分开接，否则就会迭代到一个个元组。
            words_count[word] = words_list.count(word)
        print(words_count)


if __name__ == '__main__':
    file = 'A0004.txt'
    count_words_from_text(file)
