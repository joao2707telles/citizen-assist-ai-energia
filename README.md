# Citizen Assist AI - Energia e Sustentabilidade

## Integrantes
- João Augusto Poloniato Telles - RM 571443
- Lais da Silva Dias - RM 569943

## Disciplina
Soluções em Energias Renováveis e Sustentáveis

## Público e problema
O público escolhido são **jovens entrando no mercado de trabalho**.

Nesta parte do Citizen Assist AI, analisamos o consumo de um espaço simples de estudo ou trabalho em casa. A ideia é ajudar o usuário a entender o consumo de energia e comparar uma alternativa de eficiência energética com uma fonte renovável.

## Cenário analisado
Foi considerado o uso durante **5 horas por dia, por 30 dias**, de:

| Equipamento | Potência usada |
|---|---:|
| Notebook | 65 W |
| Lâmpada comum | 60 W |
| Ventilador | 60 W |

As potências são **estimativas didáticas**, usadas para permitir os cálculos e a comparação.

Também foi adotada uma tarifa simplificada de **R$ 1,00 por kWh**. Esse valor é uma premissa do estudo e não representa uma tarifa garantida de concessionária.

O cálculo usado foi:

`Consumo (kWh) = Potência (W) x horas de uso x dias / 1000`

## Consumo atual
- Notebook: **9,75 kWh/mês**
- Lâmpada comum: **9,00 kWh/mês**
- Ventilador: **9,00 kWh/mês**
- **Total: 27,75 kWh/mês**
- **Custo estimado: R$ 27,75/mês**

## Alternativa 1 - Troca por LED
Foi comparada a lâmpada de 60 W com uma lâmpada LED de 9 W.

Resultados:
- novo consumo total: **20,10 kWh/mês**
- economia: **7,65 kWh/mês**
- economia estimada: **R$ 7,65/mês**

### Vantagens
- baixo investimento;
- redução imediata do consumo;
- maior eficiência energética.

### Limitações
A economia depende do tempo real de uso e da potência da lâmpada escolhida.

## Alternativa 2 - Energia solar
Foi usado como exemplo um pequeno painel fotovoltaico de **100 W**.

Premissas:
- 4,5 horas de sol pico por dia;
- rendimento global estimado de 80%;
- 30 dias no mês.

Cálculo:

`100 W x 4,5 h x 0,80 x 30 / 1000 = 10,80 kWh/mês`

Resultados:
- geração estimada: **10,80 kWh/mês**
- cobertura do consumo estudado: **38,9%**
- consumo restante da rede: **16,95 kWh/mês**
- economia teórica na tarifa adotada: **R$ 10,80/mês**

### Vantagens
- utiliza uma fonte renovável;
- reduz o consumo da rede;
- a geração fotovoltaica não emite poluentes diretamente durante a conversão da luz em eletricidade.

### Limitações
A geração varia com localização, clima, sombreamento, orientação e perdas do sistema. A instalação também exige investimento inicial maior.

## Comparação

| Item | Cenário atual | LED | Solar 100 W |
|---|---:|---:|---:|
| Consumo da rede (kWh/mês) | 27,75 | 20,10 | 16,95 |
| Redução (kWh/mês) | - | 7,65 | 10,80 |
| Economia estimada (R$/mês) | - | 7,65 | 10,80 |
| Investimento inicial | - | Baixo | Maior |
| Fonte renovável | Não | Não | Sim |

## Recomendação
Para quem quer começar com pouco investimento, a troca por LED é a opção mais simples.

No cenário analisado, a energia solar reduz mais o uso da rede e utiliza uma fonte renovável, mas exige investimento inicial maior e depende das condições do local.

As duas soluções também podem ser usadas juntas.

## Integração com o Citizen Assist AI
O programa permite:
- ver a análise completa;
- perguntar sobre consumo;
- perguntar sobre lâmpada LED;
- perguntar sobre energia solar;
- visualizar avisos sobre as limitações das estimativas.

## Como executar
Com Python instalado, execute:

```bash
python main.py
```

Não foram utilizadas bibliotecas externas.

## Estrutura
```text
citizen-assist-ai-energia/
├── README.md
├── main.py
├── analise_energia.py
├── TESTES.md
└── data/
    └── dados_consumo.csv
```

## Dados e premissas
Os dados usados no estudo estão em `data/dados_consumo.csv`.

Os valores de potência, tarifa, horas de uso, horas de sol pico e rendimento são premissas estimadas e estão claramente identificados. Eles servem para demonstrar o método de cálculo e não devem ser tratados como resultados garantidos.

## Fontes consultadas
- Ministério de Minas e Energia - Potência e consumo de energia:
  https://www.gov.br/mme/pt-br/assuntos/noticias/potencia-e-consumo-de-energia-o-que-sao-e-como-impactam-na-conta-de-luz

- Ministério de Minas e Energia - Eficiência energética em LED:
  https://www.gov.br/mme/pt-br/assuntos/noticias/indices-minimos-de-eficiencia-energetica-para-fontes-de-luz-com-tecnologia-led-podem-proporcionar-menos-gastos-de-energia-eletrica

- ANEEL - Micro e Minigeração Distribuída:
  https://www.gov.br/aneel/pt-br/assuntos/geracao/geracao-distribuida

- Empresa de Pesquisa Energética - Energia solar fotovoltaica:
  https://www.epe.gov.br/pt/areas-de-atuacao/energia-eletrica/expansao-da-geracao/fontes

## Limitações
Este projeto apresenta uma análise simplificada. Para uma aplicação real, seria necessário utilizar a potência real dos equipamentos, a tarifa específica da unidade consumidora e dados solares específicos da localização.
