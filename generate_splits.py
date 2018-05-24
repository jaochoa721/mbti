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

df['posts'] = df['posts'].apply(lambda x: re.sub(mbti_pat, MBTI_REP, x))
df['posts'] = df['posts'].apply(lambda x: re.sub(hashtag_pat, HASHTAG_REP, x))
df['posts'] = df['posts'].apply(lambda x: re.sub(link_pat, LINK_REP, x))


df['posts'] = df['posts'].apply(lambda x: x.split('|||'))


df['IE'] = df['type'].apply(lambda x: 'I' if x[0] == 'I' else 'E')
df['NS'] = df['type'].apply(lambda x: 'N' if x[1] == 'N' else 'S')
df['FT'] = df['type'].apply(lambda x: 'F' if x[2] == 'F' else 'T')
df['PJ'] = df['type'].apply(lambda x: 'P' if x[3] == 'P' else 'J')

train_pct = 0.6

# indicates the location to split the data along
# since dev/test are the same size
test_split_position = 1.0 - (1.0 - train_pct) / 2

train_ie, dev_ie, test_ie = np.split(df_ie.sample(frac=1), [int(train_pct*len(df_ie)), int(test_split_position*len(df_ie))])
train_ns, dev_ns, test_ns = np.split(df_ns.sample(frac=1), [int(train_pct*len(df_ns)), int(test_split_position*len(df_ns))])
train_ft, dev_ft, test_ft = np.split(df_ft.sample(frac=1), [int(train_pct*len(df_ft)), int(test_split_position*len(df_ft))])
train_pj, dev_pj, test_pj = np.split(df_pj.sample(frac=1), [int(train_pct*len(df_pj)), int(test_split_position*len(df_pj))])