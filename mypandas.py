# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)

import pandas as pd
import numpy as np
s1 = pd.Series(["akshat","aman","nischal"])
s2 = pd.Series(["akshat@gmai","aman@gmail.com","nischal@gmail.com"])
s3 = pd.Series(["99","22","33"])
mydataframe = pd.DataFrame({"StudentName":s1,"StudentEmail":s2,"StudentNumber":s3})
print(mydataframe)
mydataframe.index = ["studen1","studen2","student3"]
print(mydataframe)

# calories = pd.DataFrame({"day1":[1,2,3],"day2":[4,5,6]})
# calories.columns=["userA","userB"]
# print(calories["userA"][1])

# myvar = pd.Series(calories)
# print(myvar.index)

# print(calories) #libarary foldres in folders