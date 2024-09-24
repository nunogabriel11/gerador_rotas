# Problema de roteamento
O âmbito deste projeto focou-se na obtenção de 13 rotas diárias distintas de uma empresa e otimização do tempo demorado, com recurso a programação em python.
A organização forneceu 4 extensos ficheiros “Json” compostos pela sequência de distritos a respeitar, informação de cada mercadoria a ser entregue, a informação de cada rota (zonas e localizações geográficas) e os tempos decorridos entre duas entregas.
TALVEZ ANEXAS JSONS
O pensamento lógico para resolução deste projeto centrou-se em aplicar o modelo TSP (Traveling Salesman Problem), por outras palavras, modelo do caminho mais próximo, respeitando a sequência de distritos mencionada.
Como referido anteriormente, os resultados pretendidos centram-se na obtenção de cada uma das 13 rotas e tempo total de viagem, nunca excedendo as 24 horas diárias, como se pode ver pelo seguinte exemplo:<br /><br />


<p align="center">
  <img src="https://github.com/nunogabriel11/gerador_rotas/blob/main/imgs/route6.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 1: Figura ilustrativa do resultado obtido para a rota 6, proveniente do código pyhton desenvolvido</i>
</p><br />



A partir da informação geográfica de entrega de cada mercadoria (Json “route_data), foi possível obter uma perceção visual de cada uma das 13 rotas com a criação de um mapa de cada uma das localizações de cada rota, com auxílio da funcionalidade “3D Maps” do Excel.<br /><br />

<p align="center">
  <img src="https://github.com/nunogabriel11/gerador_rotas/blob/main/imgs/map.png?raw=true" width="400" />
</p>


<p align="center">
<i>Figura 2: Figura ilustrativa do trajeto a realizar para a rota 9</i>
</p><br />

