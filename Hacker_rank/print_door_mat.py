def print_door_mat(N, M):
    
    for i in range(1, N, 2):
        pattern = (".|." * i).center(M, '-')
        print(pattern)
    
    print("WELCOME".center(M, '-'))
    
   
    for i in range(N-2, 0, -2):
        pattern = (".|." * i).center(M, '-')
        print(pattern)

N = int(input()) 

if N % 2 != 0: 
      
       M = int(input()) * N  
else: 
       print("Error: N must be an odd number.")
 

print_door_mat(N, M)