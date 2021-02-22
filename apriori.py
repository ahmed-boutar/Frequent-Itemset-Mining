import csv
from operator import or_
from functools import reduce
import itertools
from itertools import combinations, chain

with open('adult.csv', 'r', encoding='utf-8-sig') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    dictionnary = {}
    arr = []
    rows = []
    for row in filereader:
        l = []
        for item in row:
            str_item = str(item).strip()
            l.append(str_item)
        rows.append(set(l))
        for i in range(len(row)):
            arr.append(str(row[i]).strip())

        # arr.append(str(row[0]).strip())
        # arr.append(str(row[1]).strip())
        # arr.append(str(row[2]).strip())
        # arr.append(str(row[3]).strip())
        # arr.append(str(row[4]).strip())
        # arr.append(str(row[5]).strip())
        # arr.append(str(row[6]).strip())
        # arr.append(str(row[7]).strip())
        # arr.append(str(row[8]).strip())
        # arr.append(str(row[10]).strip())
        # arr.append(str(row[11]).strip())

    # Getting the support count for all the other items of the other attributes
    for elem in arr:
        curr_elem = elem
        if curr_elem not in dictionnary.keys():
            dictionnary[curr_elem] = 0
        if curr_elem == elem:
            dictionnary[curr_elem] = dictionnary[curr_elem] + 1

    cleaned_dict = {}
    clean_dict_hpw = {}
    # Transaction reduction so that only items that have a support_count > 1000 are taken into consideration
    for item in dictionnary:
        if dictionnary[item] > 1000:
            cleaned_dict[item] = dictionnary[item]

    print(cleaned_dict)
    # frequent itemset Lk-1
    L_k = []
    L_kk = []
    for key in cleaned_dict.keys():
        if key != '?':
            L_k.append(set((key,)))
            L_kk.append(key)
    L_k_set = set(L_kk)
    # print(L_k_set)
    # print(L_k)




    def find_subsets(candidate, size_candidate):
        return list(map(set, itertools.combinations(candidate, size_candidate)))


    def has_infrequent_subset(candidate, L_k_set):
        subsets = find_subsets(candidate, len(candidate) - 1)
        for s in subsets:
            if not (s.issubset(L_k_set)):
                return True
        return False


    def apriori_gen(L_k, k):
        c = set()
        candidate_k = set()
        for sets in L_k:
            for sets2 in L_k:
                if sets != sets2:
                    candidate = (reduce(or_, [sets, sets2]))
                    if len(candidate) == k:
                        c = candidate
                        if has_infrequent_subset(c, L_k_set):
                            c = c.clear()
                        else:
                            candidate_k.add(frozenset(c))
        return candidate_k


    def subsets(candidate_k, r_set, dict_f):
        for candidate in candidate_k:
            if candidate.issubset(r_set):
                str_candidate = str(candidate)
                if str_candidate not in dict_f.keys():
                    dict_f[str_candidate] = 0
                dict_f[str_candidate] = dict_f[str_candidate] + 1
        return dict_f

    k = 2
    print('1-frequent itemsets = ', L_k)
    while len(L_k) != 0:
        dict_f = {}
        candidate_k = apriori_gen(L_k, k)
        # print('candidate_',k,' = ',candidate_k)
        for r_set in rows:
            dict_temp = subsets(candidate_k, r_set, dict_f)
            dict_f.update(dict_temp)
        temp = []
        # print('dict_f = ', dict_f)
        for key_f in dict_f:
            if dict_f[key_f] >= 1000:
                temp.append(key_f)
        temp_Lk = set()
        for cand in candidate_k:
            for set_str in temp:
                if str(cand)==set_str:
                    temp_Lk.add(cand)
        L_k = temp_Lk
        print(k,'-frequent itemsets = ',L_k)
        k = k+1
