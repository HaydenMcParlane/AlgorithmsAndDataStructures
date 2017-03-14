# NOTE: !!! NOT COMPLETE YET !!!

def find_longest_common_subsequence():
    sequence1 = "underqualified"
    sequence2 = "turboventilator"
    print(longest_common_subsequence(sequence1, sequence2))

def longest_common_subsequence(sequence1, sequence2):

    longest_common_subsequences = list()
    # Zero result matrix
    for i in range(len(sequence1)):
        longest_common_subsequences.append(list())
        for j in range(len(sequence2)):
            longest_common_subsequences[i].append(0)

    for i in range(len(sequence1)):
        for j in range(len(sequence2)):
            if is_match(sequence1[i], sequence2[j]):
                longest_common_subsequences[i][j] = longest_common_subsequences[i - 1][j - 1] + 1
            else:
                possibility_one = longest_common_subsequences[i - 1][j]
                possibility_two = longest_common_subsequences[i][j - 1]
                longest_common_subsequences[i][j] = max(possibility_one, possibility_two)
    print(longest_common_subsequences)
    return longest_common_subsequences[len(sequence1) - 1][len(sequence2) - 1]



def is_match(value1, value2):
    return value1 is value2

if __name__=="__main__":
    find_longest_common_subsequence()