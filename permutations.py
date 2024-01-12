def permute_ls(data, length, i): 
    if i==length: 
        perm_ls.append(''.join(data))
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            permute_ls(data, length, i+1) 
            data[i], data[j] = data[j], data[i]  
  
def permute_str(str1):
    string = str1
    n = len(string) 
    data = list(string)
    global perm_ls
    perm_ls = []
    permute_ls(data,n,0)
    return perm_ls