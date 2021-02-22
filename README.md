In this project, I implemented the Apriori algorithm with one improvement. I chose to implement it while taking into account transaction reduction, where the program would ignore any itemset that has a support_count less than the minimum support_count, which I have set to be 1000 based on the count the 1-itemsets displayed. 
The database the code focuses on contains data about different workers in the U. The Apriori algorithm finds the most frequent item-sets in the database. In our case, it means finding the most common type of worker in the given database.


The algorithm works as follows:
1)	Generate the 1-frequent itemset by looping through all the elements of the database, storing their respective support counts in a dictionary, then store the keys (the itemsets) in an array after deleting elements that have a support count < 1000
2)	The rest of the algorithm follows what the textbook mentions
      a.	I have included a couple of other functions in order to facilitate the work. For example, the function find_subsets takes returns all the subsets of a candidate, whose lengths are less than that of the candidate’s. The other function is subsets, which checks if a candidate is a subset of a transaction, increments the count in a dictionary, and returns it back to the main function. 


After running this algorithm on the database adult.csv, we can conclude that the frequent type of workers is a worker that is white, male, earns over 50K, from the US, married, has a spouse that is alive, high-school grads, and work in the private sector. I think that these conclusions are not surprising except for the level of education as we would expected white males (statistically more resourceful) to have gone through some college. 
