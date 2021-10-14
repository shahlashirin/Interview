import re
str = "shahlashahshahlashirinshahlamol"
pattern = r"shah"
res=len(re.findall(pattern, str))
print(res)