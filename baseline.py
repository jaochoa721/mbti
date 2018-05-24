import pandas as pd
import numpy as np
import re


df = pd.read_csv('mbti_1.csv')

# replace URLs

# replace MBTI
# https://stackoverflow.com/questions/16720541/python-string-replace-regular-expression/16720705
mbti_pat = r"ISFJ|ESFP|ISFP|ISTP|ENFP|ENFJ|INFJ|ESTP|ESFJ|ESTJ|ENTP|INFP|INTP|INTJ|ISTJ|ENTJ"
mbti_regex = re.compile(mbti_pat, re.IGNORECASE)
MBTI_REP = '$MBTI$'

# replace hashtags
hashtag_pat = r"(\#[a-zA-Z0-9]+\b)"
hashtag_regex = re.compile(hashtag_pat)
HASHTAG_REP = '$HASHTAG$'

# Replace links with $link$
# https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
link_pat = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
LINK_REP = '$LINK$'

df['posts'].apply(lambda x: re.sub(mbti_pat, MBTI_REP, x))
df['posts'].apply(lambda x: re.sub(hashtag_pat, HASHTAG_REP, x))
df['posts'].apply(lambda x: re.sub(link_pat, LINK_REP, x))


df['posts'].apply(lambda x: x.split('|||'))