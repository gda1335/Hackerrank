
#%%
string = "abracadabra"
pos=4
ch="g"
string=list(string)
string[4]="g"
a=""
a+="".join(string)
a
#%%

def mutate_string(string, position, character):
    a=""
    string=list(string)
    string[position]=character
    a+= "".join(string)
    return a
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)