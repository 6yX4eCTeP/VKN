#1.  Файл  story.txt  містить  фрагмент  книги  на  англійській  мові.  Програма повинна: 1) підрахувати кількість слів у тексті;
#  2) підрахувати кількість речень у  тексті;  3)  вивести  4  слова,  які  зустрічаються  найчастіше;
#   4)  зберегти результати роботи в окремі текстові файли. 
from collections import Counter
f1 = open('story.txt', 'r')
f2 = open('output.txt', 'w')
s = f1.read()
bar=s.split()
bar2=str(len(bar))
bar3=str(len([i for i in s.split('. ')]))
print(bar2, bar3)    

word_counts= Counter()
for word in bar:
    word_counts[word]+=1

for word in word_counts.most_common(4):
    print(word[0], word[1])
    f2.write(word[0]+' ')
    f2.write(str(word[1])+' ')

f2.write(" "+bar2+' ') 
f2.write(bar3+' ') 



f1.close()
f2.close()