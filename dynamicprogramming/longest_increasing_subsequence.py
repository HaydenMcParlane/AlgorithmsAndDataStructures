
def find_longest_increasing_subsequence():
    print(longest_increasing_subsequence([14, -23, 41, 2003, -123, 89, 2, 1, 90]))

def longest_increasing_subsequence(subject_sequence):
    longest_subsequences = []
    for i in range(len(subject_sequence)):
        longest_subsequences.append(1)
        for j in range(i):
            if subject_sequence[i] > subject_sequence[j] and is_longer(longest_subsequences, j, i):
                longest_subsequences[i] = longest_subsequences[j] + 1
    longest_subsequence = 1
    for i in range(len(longest_subsequences)):
        if longest_subsequence < longest_subsequences[i]:
            longest_subsequence = longest_subsequences[i]
    return longest_subsequence

def is_longer(sequence, subject_index, reference_index):
    return sequence[subject_index] >= sequence[reference_index]

if __name__ == "__main__":
    find_longest_increasing_subsequence()