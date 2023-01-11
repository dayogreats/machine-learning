from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=(1000)), hist=False, kde=False)

plt.show()


# from numpy import random

# import matplotlib.pyplot as plt
# import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()