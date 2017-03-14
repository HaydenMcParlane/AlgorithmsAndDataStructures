# Problem statement intentionally left out so that other students can't look
# answer up for class.
# @author: Hayden McParlane

def main():
    starting_times = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])
    finish_times = [1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 7.9, 8.9, 10]
    print(largest_number_of_activities(starting_times, finish_times))

# This algorithm assumes starting times are ordered from least to greatest
def largest_number_of_activities(starting_times, finish_times):
    largest_numbers = []

    # Initialize matrix to 1 because all activities are, by default,
    # included in their own largest activity array
    for i in range(len(starting_times)):
        largest_numbers.append(1)

    for i in sorted(range(len(starting_times)), reverse=True):
        for j in range(i, len(starting_times)):
            if finish_times[i] < starting_times[j] and largest_numbers[i] <= largest_numbers[j]:
                largest_numbers[i] = largest_numbers[j] + 1

    print(largest_numbers)
    return largest_numbers[0]

if __name__ == "__main__":
    main()