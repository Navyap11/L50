class pair_elements:

    def sumoftwo(self, nums, target):
        up= {}

        for i, num in enumerate(nums):
            if target- num in up:
                return(up[target-num],i)
            up[num]=i


value= int(input("Enter the sum of whih you want to make this search: "))
print("index1=%d, index2=%d "%
pair_elements().sumoftwo((10,20,30,40,50,60,70),value))