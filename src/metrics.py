import numpy as np


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    

    bought_list = bought_list  # Тут нет [:k] !!
    
    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    # flags по спискам товаров
    bought_in_recommended = np.isin(bought_list, recommended_list)
    recommended_in_bought = np.isin(recommended_list, bought_list[bought_in_recommended])

    precision = np.sum(prices_recommended[recommended_in_bought])/np.sum(prices_recommended)

    return precision


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    # flags по спискам товаров
    bought_in_recommended = np.isin(bought_list, recommended_list)
    recommended_in_bought = np.isin(recommended_list, bought_list[bought_in_recommended])

    # меняем только знаменатель
    recall = np.sum(prices_recommended[recommended_in_bought])/np.sum(prices_bought)

    return recall