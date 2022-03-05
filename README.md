# A evolução da remuneração de servidores por sexo e raça

Neste repositório, fazemos uma análise breve da evolução temporal das remunerações médias reais
(i.e. corrigidas pela inflação) dos servidores públicos civis federais em atividade, agrupados por
raça e sexo, utilizando os seguintes [dados do IPEA](https://www.ipea.gov.br/atlasestado/filtros-series/28/vinculos-e-remuneracoes-por-sexo):
_Remuneração líquida média mensal no Executivo civil federal ativo, por sexo e raça (1999-2020)_.

## Estrutura do projeto:

    .
    ├── README.md                                     <- Este documento
    ├── requirements.txt                              <- Principais pacotes de python necessários
    ├── dados                                         <- Diretório onde salvar os dados
    |   ├── brutos                                    <- Dados tais quais obtidos do IPEA
    |   └── limpos                                    <- Dados limpos
    ├── analises                                      <- Análises feitas e códigos utilizados
    |   ├── my_functions.py                           <- Funções preparadas para a análise
    |   └── resolucao_exercicio_remunerac....ipynb    <- Notebook com a análise realizada
    └── relatorio.pdf                                 <- Texto comentando as tendências observadas

## Preparação

Este projeto utiliza Python 3.4+ e os pacotes `pandas`, `matplotlib`, `urllib` e `pathlib`
(biblioteca padrão para Python 3.4+).
É preciso instalar o Python 3 e esses pacotes caso eles já não estejam instalados. O projeto também utiliza
um leitor de notebooks (jupyter notebook ou jupyter lab).

Para uma reprodução mais garantida:

1. Certificar-se de que possui Python 3.4 ou mais recente instalado com os comandos: `python --version` ou `python3 --version`.
2. Rodar os seguintes comandos:

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt 

## Sobre o projeto

Todo o processo de análise, incluindo o _download_ dos dados e sua limpeza, estão no notebook
[resolucao_exercicio_remuneracao_vs_sexo_raca.ipynb](analises/resolucao_exercicio_remuneracao_vs_sexo_raca.ipynb).

Por conveniência, os dados baixados encontram-se na pasta [dados/brutos](dados/brutos) e os dados
já limpos encontram-se em [dados/limpos](dados/limpos).

O arquivo [analises/my_functions.py](analises/my_functions.py)
é importado pelo notebook e contém funções criadas para esta análise.

O documento [relatorio.pdf](relatorio.pdf) contém a discussão sobre a análise feita.

## Contato

Quaisquer dúvidas a respeito deste trabalho podem ser encaminhadas a [Henrique Xavier](http://henriquexavier.net) (<https://github.com/hsxavier>). 