n = int(input())  
k = set(range(1, n + 1))  

while True:
   a = input()  
   if a == "HELP":
        break  
    
   a_set = set(map(int,a.split()))  
    
   if len(k &a_set) > len(k) / 2:
        answer = "YES"  
   else:
        answer = "NO"
    
   print(answer)   
    
   if answer == "YES":
        k &=a_set  
   else:
        k -=a_set  

result = sorted(k)  
print(" ".join(map(str, result)))  
