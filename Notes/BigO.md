# The Big O Notation:
>
### 1. Growth is with respect to the input
### 2. Constants are dropped
### 3. We consider The Worst Case
---
```python
somearr = [1,2,3,4,5]

def sum():
    sum = 0

    for i in somearr:
        sum += i

    for i in somearr:
        sum += i
```
**Whats the time complexity?**

Here, The time complexity wont be `2*O(n)`, instead we drop the constant and just say O(n). We are not trying to get the exact time, we are just trying to figure out how much it grows

say for this example,

```python
def sum(someString):
    sum = 0
    for i in someString:
        sum += ord(i)
        if i == 'E':
            return sum
    return sum
```
Whats the time complexity?

Well it depends on if 'E' is encountered. if the first letter of the `someString` is 'E' then its O(1) but we dont know that, so we just assume the worst case, we assume `E` is the last character in `someString`, thus making this O(n)

