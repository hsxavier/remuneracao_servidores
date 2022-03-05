#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Funções auxiliares para o exercício da República.org


import pandas as pd
import matplotlib.pyplot as pl


def parse_ptbr_series(string_series):
    """
    Converte uma série de strings que representam
    números em formato brasileiro para uma série
    de floats.

    Parâmetros
    ----------
    string_series : Pandas Series
        Série com os números em formato brasileiro
        (pontos separando os milhares e vírgula 
         separando os decimais).

    Retornos
    --------
    number_series : Pandas Series
        Série dos floats correspondentes.
    """

    # Remove espaços:
    no_spaces = string_series.str.split().str.join('')
    # Altera a pontuação:
    new_marks = no_spaces.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    # Converte para float:
    number_series = new_marks.astype(float)

    return number_series


def split_variables(series, data_separator=' ', name_separator='_'):
    """
    Separa variáveis guardadas em uma mesma série 
    (coluna de uma tabela).
    
    Parâmetros
    ----------
    series : Pandas Series
        Série de dados com variáveis misturadas.
    data_separator : str
        Caractere ou string que separa os 
        valores da série `series`.
    name_separator : str
        Caractere ou string que separa os 
        nomes das variáveis na série `series`.
        
    Retornos
    --------
    df : DataFrame
        Tabela com a série `series` dividida 
        em múltiplas colunas, uma para cada
        variável. O índice permanece o mesmo
        da `series`.
    """
    
    # Separa os nomes:
    col_names = series.name.split(name_separator)
    # Separa os valores:
    values = series.str.split(data_separator).tolist()
    # Cria a Tabela:
    df = pd.DataFrame(data=values, columns=col_names, index=series.index)
    
    return df


def extract_subset_series(remuneracao_df, sexo, raca, value_col='liquido', prefix='ref_'):
    """
    Dada uma tabela limpa de remuneração média anual
    de servidores por sexo e raça, retorna a série 
    temporal de um dos grupos de servidores.
    
    Parâmetros
    ----------
    remuneracao_df : DataFrame
        Tabela com os dados limpos, organizados 
        nas colunas 'ano', 'sexo', 'raça' e 'liquido'.
    sexo : str
        Sexo dos servidores a serem selecionados 
        ('Mulher' ou 'Homem').
    raca : str
        Raça dos servidores a serem selecionados 
        ('Negra' ou 'Branca').
    value_col : str
        Nome da coluna que contém os valores a serem
        retornados na série.
    prefix : str
        Prefixo a ser adicionado ao nome da série,
        que irá conter também o sexo e a raça.
    
    Retornos
    --------
    series : Pandas Series
        Série temporal, com índices dados pelos 
        anos e valores pela remuneração líquida.
    """
    # Seleciona apenas servidores de um certo grupo:
    subset_df = remuneracao_df.query('sexo == "{}" and raça == "{}"'.format(sexo, raca))
    
    # Prepara uma série temporal:
    series = subset_df.set_index('ano')[value_col]
    series.name = '{}{}_{}'.format(prefix, sexo, raca).lower()
    
    return series


def plot_timeseries(df, value_col):
    """
    Cria uma gráfico contendo uma série temporal
    para cada grupo de servidores.
    
    Parâmetros
    ----------
    df : DataFrame
        Tabela de dados limpos contendo as colunas
        'ano', 'raça', 'sexo' e `value_col`.
    value_col : str
        Nome da coluna de `df` que será apresentada 
        no gráfico (eixo vertical).
    """
    color_dict  = {'Negra': 'sienna', 'Branca': 'sandybrown'}
    format_dict = {'Mulher': '-', 'Homem': '--'}

    # Loop sobre grupos de servidores:
    for sexo in sorted(df['sexo'].unique()):
        for raca in sorted(df['raça'].unique()):

            # Seleciona um grupo:
            remun_grupo = extract_subset_series(df, sexo, raca, value_col=value_col)

            # Coloca a remuneração do grupo no gráfico:
            remun_grupo.plot(label='{}/{}'.format(sexo, raca), color=color_dict[raca], style=format_dict[sexo])

    # Formatação:
    pl.tick_params(labelsize=14)
    pl.xlabel('')
    ax = pl.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Marcas verticais e horizontais:
    pl.axvspan(2006, 2010, color='lightgray', alpha=0.4)
    pl.grid(axis='y', color='lightgray')
