import re
str1="As published in the Journal of the Royal Society of Arts dated Aug. 27, 1848. The House of Tata - Sixty Years Industrial Development in India by Sir Frederick James, O.B.E. - “Jamshedji Nusserwanji Tata was born in 1839, just after Macaulay had left India to write his famous history of England… he passed out of Elphinstone College in Bombay in 1858. Shortly afterwards he joined his father’s trading firm, whose business was general merchandise. He took special interest in"
l=re.findall('[1-9]{4}',str1)
print(l)
m=re.findall('[A-Za-z]{3}\.\s[1-9]{2},\s[1-9]{4}\.',str1)
print(m)
n=re.findall('[A-Za-z]{4}\s\-\s[A-Za-z]{5}',str1)
print(n)