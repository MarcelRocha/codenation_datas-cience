#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[2]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[3]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# **A coluna normal do dataframe foi criada a partir de uma distribuição normal com média 20 e desvio padrão 4 tendo 1000 valores.**

# ## Inicie sua análise a partir da parte 1 a partir daqui

# In[4]:


# Sua análise da parte 1 começa aqui.
 
dataframe.head(5)


# In[5]:


dataframe.describe().round(3)


# In[6]:


sns.distplot(dataframe['normal'])
plt.show()


# In[7]:


norm = dataframe['normal']
q1_norm = sct.norm.ppf(0.25, loc=20, scale= 4).round(3)
q2_norm = sct.norm.ppf(0.5, loc=20, scale= 4).round(3)
q3_norm = sct.norm.ppf(0.75, loc=20, scale= 4).round(3)

print(q1_norm, q2_norm, q3_norm)


# Usei a variável norm para receber só a coluna 'normal' do dataframe e, em seguida, caculei o quartil 25%, 50% e 75%, para a distribuição normal da variável norm arredondando os valores para 3 casas decimais. 

# In[8]:


sns.distplot(dataframe['binomial'], kde=False, hist_kws={"alpha":0.5})
plt.show()


# In[9]:


binom = dataframe['binomial']


# In[10]:


np.quantile(norm, [0.25, 0.50, 0.75])


# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[11]:


def q1():
    # Retorne aqui o resultado da questão 1.
    q_norm = np.quantile(norm, [0.25, 0.50, 0.75])
    q_binom = np.quantile(binom, [0.25, 0.50, 0.75])
    q_result = (q_norm - q_binom).round(3)
    return tuple(q_result)
    pass
q1()


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# Sim, vito que a distribuição binomial se aproxima da distribuição normal para **n** grandes e que **p** não esteja muito próximo nem de 0 nem de 1.

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[12]:


def q2():
    # Retorne aqui o resultado da questão 2.
    left_limit =sct.norm.cdf((norm.mean()-norm.std()), loc=20, scale=4)
    right_limit = sct.norm.cdf((norm.mean()+norm.std()), loc=20, scale=4)
    return (right_limit - left_limit).round(3)
    pass
q2()


# In[13]:


left_s2 =right_limit =sct.norm.cdf((norm.mean()-norm.std()*2), loc=20, scale=4)
right_s2 =right_limit =sct.norm.cdf((norm.mean()+norm.std()*2), loc=20, scale=4)
left_s3 =right_limit =sct.norm.cdf((norm.mean()-norm.std()*3), loc=20, scale=4)
right_s3 =right_limit =sct.norm.cdf((norm.mean()+norm.std()*3), loc=20, scale=4)

print(right_s2 - left_s2, right_s3 - left_s3)


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# * Sim, o valor é próximo d valor teórico porém erra em uma casa decimal.
# * Os valores também estão bem próximos para os outros intervalos.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[14]:


def q3():
    # Retorne aqui o resultado da questão 3.
    mean_result = (binom.mean() - norm.mean()).round(3)
    var_result = (binom.var() - norm.var()).round(3)
    return (mean_result, var_result)
    pass
q3()


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[15]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[18]:


stars.head(5)


# In[19]:


stars.isna().sum()


# In[20]:


stars.describe()


# In[27]:


df_filter = stars.query('target == False').mean_profile
false_pulsar_mean_profile_standardized = (df_filter - df_filter.mean())/df_filter.std()


# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[34]:


def q4():
    # Retorne aqui o resultado da questão 4.
    fn_ecdf= ECDF(false_pulsar_mean_profile_standardized)
    q1 = sct.norm.ppf(0.8, loc=0, scale=1)
    q2 = sct.norm.ppf(0.9, loc=0, scale=1)
    q3 = sct.norm.ppf(0.95, loc=0, scale=1)
    return (fn_ecdf(q1).round(3), fn_ecdf(q2).round(3), fn_ecdf(q3).round(3))
    pass
q4()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# * Sim, os valores fazem sentido.
# * A variável obedece a distribuição normal como é visto no gráfico de distribuição. 

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[29]:


def q5():
    # Retorne aqui o resultado da questão 5.
    q_theo = np.quantile(false_pulsar_mean_profile_standardized, [0.25, 0.50, 0.75])
    norm = sct.norm(false_pulsar_mean_profile_standardized)
    q_norm = [sct.norm.ppf(0.25, loc=0, scale=1), sct.norm.ppf(0.50, loc=0, scale=1), sct.norm.ppf(0.75, loc=0, scale=1)]
    q_result = (q_theo - q_norm).round(3)
    return tuple(q_result)
    pass
q5()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.

# * Sim, os valores fazem sentido.
# * Isso quer dizer que os valores da variável se aproximam muito bem à distribuição normal.
