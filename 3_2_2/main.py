from prob_random import ProbRandom

dataset = [1,2,3,4]
prob_list = [0.3, 0.1, 0.2, 0.4]

pr = ProbRandom(dataset, prob_list)

randomP = [0] * len(pr.dataset)
probRandomP = [0] * len(pr.dataset)

N = 1000
for i in range(N):

    # call random_data method 1000 times and count the number of occurences saved in the list randomP.
    value = pr.random_data()
    index = pr.dataset.index(value)
    randomP[index] += 1

    # call prob_random_data 
    value = pr.prob_random_data()
    index = pr.dataset.index(value)
    probRandomP[index] += 1

print(randomP)
print(probRandomP)