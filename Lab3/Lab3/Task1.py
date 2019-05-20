import numpy as np

ALPHA = np.random.randint(1, 200, size=100)
BETA = np.sort(ALPHA,kind="heapsort")[::-1][:15]

with open("result_task1.txt","w+") as destfile:
    destfile.writelines([x + ' ' for x in BETA.astype(str)])
    destfile.seek(0)
    print(destfile.read())
