import seaborn as sns
from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()
df = pd.DataFrame(data=diabetes.data,
                           columns=diabetes.feature_names)
df['Progress'] = diabetes.target
sns.kdeplot(data=df, x='Progress', color='green', fill=True)
