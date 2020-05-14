# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np
# fig = Figure()
# canvas = FigureCanvas(fig)

# x = np.random.randn(10000)

# ax = fig.add_subplot(111)
# ax.hist(x, 100)

# ax.set_title("normal distribution with $\mu=0, \sigma=1$")
# fig.savefig('matplotlib_histogram.png')

# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import numpy as np

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.randn(1000)
# plt.hist(x, 100)
# plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
# plt.savefig('matplotlib_histogram.png')
# plt.show()


# import matplotlib.pyplot as plt
# plt.plot(5, 5, 'o')
# plt.show()

import numpy as np
import pandas as pd

df_can = pd.read_excel(
    'https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2awomz9pu.xlsx.xlsx',
    sheetname="Canada by Citizenship",
    skiprows=range(20),
    skip_footer = 2
)
df_can.head()