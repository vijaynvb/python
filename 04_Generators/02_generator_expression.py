
from time import sleep

para ="some content"

#declare a paragraph and print the paragraph in a typing style using generator
for char in para:
    sleep(0.1)
    print(char, end='', flush=True) 

