#!/usr/bin/env python3
# -*- config: utf-8 -*-

# 2. Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, содержащие введенное с клавиатуры слово.

if __name__ == '__main__':
    a = input("Введите слово для поиска")

    with open('ind1.txt', 'r') as f:
        text = f.read()

        text = text.replace("!", ".")
        text = text.replace("?", ".")

        while ".." in text:
            text.replace("..", ".")

        sentences = text.split(".")

        for sentence in sentences:
            if a in sentence:
                with open('text.txt', 'r')as s:
                    f_text = s.read()
                    if sentence in f_text:
                        print(f'{sentence}{f_text[f_text.rfind(sentence) + len(sentence)]}')
