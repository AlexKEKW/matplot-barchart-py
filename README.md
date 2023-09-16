# matplot-barchart-py

# Análise dos Clubes Mais Valiosos da Premier League

Este projeto envolve uma análise dos clubes mais valiosos da Premier League, uma das ligas de futebol mais prestigiadas do mundo. Utilizamos Python, Pandas e Matplotlib para realizar essa análise.

## Dados

Os dados utilizados neste projeto são armazenados em um dicionário Python chamado "dictClubes". Ele contém as informações dos 10 clubes mais valiosos da Premier League, com os nomes dos clubes como chaves e os valores de mercado como valores associados a essas chaves.

## Análise de Dados

Usamos a biblioteca Pandas para converter o dicionário em uma série de dados. Em seguida, usamos a biblioteca Matplotlib para criar um gráfico de barras na vertical que exibe as informações dos clubes mais valiosos.

## Resultados

O gráfico de barras na vertical apresenta visualmente a diferença nos valores de mercado dos clubes da Premier League. Através da análise do gráfico, podemos tirar as seguintes conclusões:

- O clube mais valioso da Premier League é o "Manchester City" com um valor de mercado de aproximadamente 999.999 milhões.
- O "Liverpool" e o "Chelsea" são os clubes que se aproximam do valor de mercado do "Manchester City", com valores de 870.000 milhões e 866.700 milhões, respectivamente.
- O "Everton" é o clube menos valioso entre os 10 analisados, com um valor de mercado de cerca de 380.700 milhões.

## Próximos Passos

Este projeto de análise pode ser expandido para incluir mais clubes ou para analisar outras métricas, como o desempenho em campo em relação ao valor de mercado. Também é possível automatizar a atualização dos dados para manter a análise sempre atualizada.

## Como Executar

Para executar a análise, você pode seguir os seguintes passos:

1. Clone este repositório para a sua máquina local.
2. Certifique-se de que você possui Python, Pandas e Matplotlib instalados.
3. Execute o script Python para gerar o gráfico de barras.

```bash
python analise.py
