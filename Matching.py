import pandas as pd
from thefuzz import fuzz, process
from DataClass import Data
import numpy as np
import pandas as pd
import datetime
from os import getenv, path
import dotenv

Now = datetime.datetime.now()
ipro_csv_url = getenv('ipro_csv_url')
df = pd.read_csv('./comparison/Iprobooking.csv')
# df = pd.read_csv('../code/comparison/Iprobooking.csv')
iproarray = df.to_numpy()

sheet = np.array([["ipro hotels", "prix", "mygo hotels", "prix"]])
for iprocolum in iproarray:
    iproname = iprocolum[0]
    mygo_csv_url = getenv('mygo_csv_url')
    df = pd.read_csv('./comparison/MyGo.csv')
    # df = pd.read_csv('../code/comparison/MyGo.csv')
    mygoarray = df.to_numpy()
    oldratio = int(90)
    matching = ["/", "/"]
    for mygocolum in mygoarray:
        mygoname = mygocolum[0]
        ratio = int(fuzz.partial_ratio(iproname, mygoname))
        if ratio > oldratio:
            matching = mygocolum  # mygo rowe
            oldratio = ratio
            continue
        else:
            continue
    joined_list = [*iprocolum, *matching]
    sheet = Data.ClassData_comparison(sheet, joined_list)
    # print(joined_list)

df = pd.DataFrame(sheet, columns=["names1", "prix1", "names2", "prix2"])
# df.style.apply(lambda x: ['Background:red'if x > df. else 'Background:red'] for x in df.prix1, axis=0)
df.to_csv(
    f'./comparison/comparison_Mygo{Now}.csv', index=False, header=False)

####################################################################################################
ipro_csv_url = getenv('ipro_csv_url')
df = pd.read_csv('./comparison/Iprobooking.csv')
iproarray = df.to_numpy()

sheet = np.array([["ipro hotels", "prix", "clicngo hotels", "prix"]])
for iprocolum in iproarray:
    iproname = iprocolum[0]
    clicngo_csv_url = getenv('clicngo_csv_url')
    df = pd.read_csv('./comparison/clicngo.csv')
    # df = pd.read_csv('../code/comparison/clicngo.csv')
    clicarray = df.to_numpy()
    oldratio = int(90)
    matching = ["/", "/"]
    for cliccolum in clicarray:
        clicname = cliccolum[0]
        ratio = int(fuzz.partial_ratio(iproname, clicname))
        if ratio > oldratio:
            matching = cliccolum  # mygo rowe
            oldratio = ratio
            continue
        else:
            continue
    joined_list = [*iprocolum, *matching]
    sheet = Data.ClassData_comparison(sheet, joined_list)
    # print(joined_list)

df = pd.DataFrame(sheet, columns=["names1", "prix1", "names2", "prix2"])
# df.style.apply(lambda x: ['Background:red'if x > df. else 'Background:red'] for x in df.prix1, axis=0)
df.to_csv(f'./comparison/comparison_clicngo{Now}.csv',
          index=False, header=False)
