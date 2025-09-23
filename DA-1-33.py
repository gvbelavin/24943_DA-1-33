import seaborn as sns
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import numpy

def diabet_kde(dataFrame=None,target_column = "Progress",color = "green",save_path=None):
  
  #Загрузка данных если dataFrame не предоставлен
  if dataFrame is None:
    diabetes = load_diabetes()
    dataFrame = pd.DataFrame(data=diabetes.data,
                              columns=diabetes.feature_names)
    dataFrame['Progress'] = diabetes.target
    
  # Проверка наличия целевой колонки
  if target_column not in dataFrame.columns:
    avalible_columns = ','.join(dataFrame.columns)
    raise ValueError(f"Колонка {target_column} не найдена в dataFrame")
    print(f"Доступные колонки {avalible_columns}")

  #Построение KDE графика
  sns.kdeplot(data=dataFrame, x=target_column, color= color, fill=True)

  plt.title("Ядерная оценка плотности распределения прогресса диабета", fontsize=14)
  plt.xlabel("Уровень прогресса диабета",fontsize=12)
  plt.ylabel("Плотность вероятности",fontsize=12)
  sns.set_style("whitegrid")
  plt.show()
  
  #Сохранение графика если указан путь
  if save_path:
    plt.savefig(save_path)

if __name__ == "__main__":
  try:
    diabet_kde()
  except Exception as error:
    print(f"Произошла ошибка {error}")

