import re
str1="Russia-Ukraine war news LIVE updates February 27: Ukrainian forces put up fierce resistance to slow the advance of the Russian military closing in on capital Kyiv, which is taking heavy artillery fire and airstrikes. As Russians close in, curfew has been imposed in Kyiv and residents have been asked to stay indoors until Monday. With his country under siege, Ukraine President Volodymyr Zelensky on Saturday rejected a US offer to evacuate, saying he needs ammunition, not a ride. On the other hand, thousands of Ukrainians are fleeing the country amid a war that has reportedly claimed the lives of 198 countrymen. France, the US and Germany have pledged military assistance to Ukraine to bolster its chances of stymying the Russian invasion. Stay with Indiatoday.in for LIVE updates."
words=re.findall('\w+\s\d{2}',str1)
print(words)
str2="measure to conceal their purpose (see etymology)"
allword=re.findall('\([A-Za-z\s]+\)',str2)
print(allword)
