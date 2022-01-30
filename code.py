import pandas as pd
import statistics

df=pd.read_csv("StudentsPerformance.csv")

math_score=df["math score"].tolist()
reading_score=df["reading score"].tolist()

maths_mean=statistics.mean(math_score)
maths_median=statistics.median(math_score)
maths_mode=statistics.mode(math_score)

reading_score_mean=statistics.mean(reading_score)
reading_score_median=statistics.median(reading_score)
reading_score_mode=statistics.mode(reading_score)

maths_std=statistics.stdev(math_score)
reading_score_std=statistics.stdev(reading_score)

# math_score
one_sigma_start=maths_mean-maths_std
one_sigma_end=maths_mean+maths_std

one_sigma_count=0

for i in math_score:
    if (i>one_sigma_start) and (i<one_sigma_end):
        one_sigma_count=one_sigma_count+1

one_sigma_value=one_sigma_count*100/len(math_score)
print(one_sigma_value,"% of data lies within one_sigma_interval")
 
two_sigma_start=maths_mean-2*maths_std
two_sigma_end=maths_mean+2*maths_std

two_sigma_count=0

for i in math_score:
    if (i>two_sigma_start) and (i<two_sigma_end):
        two_sigma_count=two_sigma_count+1

two_sigma_value=two_sigma_count*100/len(math_score)
print(two_sigma_value,"% of data lies within two_sigma_interval")

three_sigma_start=maths_mean-3*maths_std
three_sigma_end=maths_mean+3*maths_std

three_sigma_count=0

for i in math_score:
    if (i>three_sigma_start) and (i<three_sigma_end):
        three_sigma_count=three_sigma_count+1
three_sigma_value=three_sigma_count*100/len(math_score)
print(three_sigma_value,"% of data lies within three_sigma_interval")



# reading_score

one_sigma_start=reading_score_mean-reading_score_std
one_sigma_end=reading_score_mean+reading_score_std

one_sigma_count=0

for i in reading_score:
    if (i>one_sigma_start) and (i<one_sigma_end):
        one_sigma_count=one_sigma_count+1

one_sigma_value=one_sigma_count*100/len(reading_score)
print(one_sigma_value,"% of data lies within one_sigma_interval")
 
two_sigma_start=reading_score_mean-2*reading_score_std
two_sigma_end=reading_score_mean+2*reading_score_std

two_sigma_count=0

for i in reading_score:
    if (i>two_sigma_start) and (i<two_sigma_end):
        two_sigma_count=two_sigma_count+1

two_sigma_value=two_sigma_count*100/len(reading_score)
print(two_sigma_value,"% of data lies within two_sigma_interval")

three_sigma_start=reading_score_mean-3*reading_score_std
three_sigma_end=reading_score_mean+3*reading_score_std

three_sigma_count=0

for i in reading_score:
    if (i>three_sigma_start) and (i<three_sigma_end):
        three_sigma_count=three_sigma_count+1
three_sigma_value=three_sigma_count*100/len(reading_score)
print(three_sigma_value,"% of data lies within three_sigma_interval")

