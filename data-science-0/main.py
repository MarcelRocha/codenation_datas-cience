#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head(10)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[5]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass
q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[6]:


def q2():
    # Retorne aqui o resultado da questão 2.
    bf_gender_age =black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] =='26-35')]
    return bf_gender_age.User_ID.nunique()
    pass
q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[12]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()
    pass
q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[13]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()
    pass
q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[16]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return (black_friday.shape[0] - black_friday.dropna().shape[0])/black_friday.shape[0]
    pass
q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[15]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday.isnull().sum().max()
    pass
q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[19]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].value_counts().idxmax()
    pass
q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[20]:


def q8():
    # Retorne aqui o resultado da questão 8.
    purchase_min = black_friday['Purchase'].min()
    purchase_max = black_friday['Purchase'].max()
    purchase_nmz = (black_friday['Purchase'] - purchase_min)/(purchase_max - purchase_min)
    return purchase_nmz.mean()
    pass
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[8]:


def q9():
    # Retorne aqui o resultado da questão 9.
    black_friday['Purchase_pdz']= (black_friday['Purchase'] - black_friday['Purchase'].mean())/black_friday['Purchase'].std()
    return  len([i for i in black_friday['Purchase_pdz'] if i > -1 and i <1] )
    pass
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[7]:


def q10():
    # Retorne aqui o resultado da questão 10.
    pc_2 = black_friday[black_friday['Product_Category_2'].isna()]
    pc_3 = category_2[category_2['Product_Category_3'].isna()]
    return pc_2.shape == categ_3.shape
    pass
q10()

