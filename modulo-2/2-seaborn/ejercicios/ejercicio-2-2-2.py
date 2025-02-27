import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    'x': np.random.rand(100),
    'y': np.random.rand(100)*10,
    'z': np.random.rand(100)*100,
    'categoria': np.random.choice(['A', 'B', 'C'], size=100)
}

df = pd.DataFrame(data)

sns.pairplot(df, hue='categoria', diag_kind='hist')

plt.savefig('./tmp/pairpplot2.png')

print(df)
