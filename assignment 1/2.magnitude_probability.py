from random import uniform
def pick_a_number_from_list(A):
    sum=0
    for i in A:
        sum+=i
    x=0
    sum_list=[]
    for i in A:
        x=x+i/sum
        sum_list.append(x)
    #sum_list contsins cumulative sum
    #print(sum_list)
    select=uniform(0,1)

    for i in range (len(sum_list)):
        if select<sum_list[i]:
            return(A[i])

def sampling_based_on_magnitued():
    A = [0,5,27,6,13,28,100,45,10,79]
    sampled_numbers = []
    for _ in range(100000):
        num = pick_a_number_from_list(A)
        sampled_numbers.append(num)
    
    sampled_number_of_times = [0]*len(A)
    for i in range(len(A)):
        sum_ = 0
        for j in range(len(sampled_numbers)):
            if(A[i]==sampled_numbers[j]):
                sum_ += 1
        sampled_number_of_times[i]=sum_

    for i in range(len(A)):
        print(A[i],":",sampled_number_of_times[i]) 
sampling_based_on_magnitued()