
def calc_bayes(prior_A,prob_B_dado_A,prob_B):
    return prior_A*prob_B_dado_A/prob_B


def run():
    probabilidad_cancer= 1/100000
    probabilidad_cancer_sintoma=1
    probabilidad_no_cancer=1-probabilidad_cancer
    probabilidad_no_cancer_simtoma=10/99999
    
    probabilidad_simtoma=(probabilidad_cancer*probabilidad_cancer_sintoma)+probabilidad_no_cancer*probabilidad_no_cancer_simtoma

    probabilidad_cancer_dado_sintoma=calc_bayes(probabilidad_cancer,probabilidad_cancer_sintoma,probabilidad_simtoma)

    print(f'La probabilidad de tener cancer dado que tienes un sintoma es de {probabilidad_cancer_dado_sintoma*100} %')


if __name__ == '__main__':
    run()