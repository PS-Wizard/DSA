I swear people make this seem like its too hard

# Arrays:

### 268 Missing Number:
My Attempt:
```python
def missingNumber(nums):
    return list({i for i in range(0,len(nums)+1)}  - set(nums))[0]
```
Better alternative:
```python
def missingNumber(nums):
    return sum(range(len(nums)+1))-sum(nums)
```


