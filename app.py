import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
sns.dark_palette("#69d", reverse=True, as_cmap=True)

st.markdown("# Atomic Habits Compounding Effect")

x = st.slider('% Betterment', max_value=10)

y = st.slider('Days Spent Grinding', min_value=1, max_value=365)

better = 1 + float(x) * 0.01 if x > 0 else 0.9
num = better**y

st.write(' Marginal Gains by getting {}% better for {} days will be : '.format(x, y))

if len(str(num)) < 25:
    st.write(f'{num:,f}')
else:
    st.write(num)

# with compounding
i = np.linspace(1, 365)
j = better**i
k = (0.05)*i+1   # Random Gradual growth Equation

plt.plot(i, k, label='What we Think!')

plt.plot(i, j, label='What Actually Happens!')
plt.xlabel("Results")
plt.ylabel("% Growth")
plt.legend()
st.pyplot(plt)


# st.pyplot(plt)
