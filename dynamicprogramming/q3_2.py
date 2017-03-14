'''
 Problem statement intentionally left out so that other students can't look
 answer up for class.
 @author: Hayden McParlane
'''

'''
Given this problem,
    (a) is confirmed by actually running the main program.
    The inductive formula is...
        c[i] =    | 1,          if i = length of start_times
                  | c[j] + 1    if c[i] < c[j]

    or  c[i] = max (as j goes from i to n) { c[i], c[j] + 1 }

    (b)
'''

def main():
    starting_times = sorted([2,3,5,6,7,9,10,12,13,14,16])
    finish_times = [6,5,7,10,8,13,16,14,14,18,20]
    print(largest_number_of_activities(starting_times, finish_times))

# This algorithm assumes starting times are ordered from least to greatest
def largest_number_of_activities(starting_times, finish_times):
    if len(starting_times) is not len(finish_times):
        raise ValueError()

    largest_numbers = []
    # Initialize matrix to 1 because all activities are, by default,
    # included in their own largest activity array
    for i in range(len(starting_times)):
        largest_numbers.append(1)

    for i in sorted(range(len(starting_times)), reverse=True):
        for j in range(i, len(starting_times)):
            if finish_times[i] <= starting_times[j] and largest_numbers[i] <= largest_numbers[j]:
                largest_numbers[i] = largest_numbers[j] + 1

    print(largest_numbers)
    return largest_numbers[0]

if __name__ == "__main__":
    main()