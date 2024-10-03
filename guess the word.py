import random
words=['waste','ghost','host','poster','pig','donkey','angel']
word=random.choice(words)
g_word=[]
for i in word:
    g_word.append('_')
for i in g_word:
    print(i,end=" ")
print()
n=5
print("\nThere are only 5 chances")
while n>0:
    if(g_word==list(word)):
        print("\nCongratulations you gussed the word correctly!")
        break
    l=input("\nGuess a letter:")
    if l in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i]==l:
                g_word[i]=l
        for i in g_word:
            print(i,end=" ")
    else:
        n-=1
        for i in g_word:
            print(i,end=" ")
        print(f"\nWrong guess \nOnly {n} chances left")
        if(n==0):
            print("\nSorry\nYou are out of chances!")
            print(f"The answer is {word}")
