
def translete(text):
    strl=text
    for i in 'ЁУЕЫАОЭЯИЮёуеыаоэяию.,;!?-:""()':
        strl = strl.replace(str(i),'')
        strl = strl.replace('  ',' ')
        if strl[1]==' ':
            strl = ''.join([strl[i] for i in range(len(strl)) if i != 0])
    return strl

print('Ввод:')
text = input()
translate_text = translete(text)
print('РЕЗУЛЬТАТ:',translate_text)
input('Press ENTER to exit')
