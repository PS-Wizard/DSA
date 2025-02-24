# Arrays:

**Reads:** Take O(1) Constant time cause well they just do

**Insertions:** These Take O(N+1), because say you insert at the very first index, this involves shifting every other element to the right by 1; thats N steps, and finally the insertion itself which is a constant time which we just say 1. So, Insertion Takes O(N+1)

**Deletion:** These Take O(N), because say you delete at the very first index, this is constant time, but now you gota shift every other element to the left by 1; thats N-1 steps. So, O( N-1 + 1) = O(N) 

**Linear Searching:** These Take O(N) in the worst case, this just makes sense As yk you gota loop through every element

---

# Sets: 
Sets and arrays are pretty similar, but sets can't contain duplicates. This single rule changes the complexity in the following ways:

==Reads and Deletions and Linear Searches remain the same==

**Insertions:** This now takes O(N+1) because now, we need to search the already existing elements in the set i.e O(N) and finally if the thing we are trying to insert isn't a duplicate it is inserted i.e O(1) thus, combined its O(N+1)

---

# Exercises:
1. For an array containing 100 elements, provide the number of steps the following operations would take:

    - Reading -> O(1)
    - Searching for a value not contained in the array -> O(N)
    - Insertion at the beginning of the array -> O(N + 1)
    - Insertion at the end of the array -> O(1)
    - Deletion at the beginning of the array -> O(N-1 + 1) -> O(N)
    - Deletion at the end of the array -> O(1)

2. For an *++array-based set++* containing 100 elements, provide the number of steps the following operations would take:

    - Reading -> O(1)
    - Searching for a value not contained in the array -> O(N)
    - Insertion at the beginning of the array -> O(N) to search + O(N) To shift + O(1) To actually insert -> O(2N+1)
    - Insertion at the end of the array -> O(N) to search + O(1) to insert -> O(N+1)
    - Deletion at the beginning of the array -> O( N-1 + 1) -> O(N)
    - Deletion at the end of the array -> O(1)

3. Count all the instance of a certain element in an array:

    - Thats just O(N)

