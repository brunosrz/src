# Mapa de conceitos

Este índice organiza conceitos que atravessam linguagens. Os temas estão planejados; adicione links
para implementações somente quando existirem e estiverem verificadas.

## Trilhas

| Área                  | Assuntos                                               | Experimento sugerido                       |
| --------------------- | ------------------------------------------------------ | ------------------------------------------ |
| Fundamentos           | Algoritmos, estruturas de dados, complexidade, memória | Comparar busca linear e índice             |
| Redes e APIs          | DNS, TCP, HTTP, TLS, REST, RPC, contratos              | Medir timeout e cancelamento               |
| SQL                   | Modelagem, índices, transações, isolamento             | Reproduzir uma anomalia de concorrência    |
| NoSQL                 | Documentos, chave-valor, colunas, grafos               | Modelar por padrão de acesso               |
| Busca vetorial        | Embeddings, métricas, ANN, filtros, recall             | Comparar busca exata e aproximada          |
| Cache                 | TTL, invalidação, cache-aside, stampede                | Evitar recomputação concorrente            |
| Eventos e pub/sub     | Filas, fan-out, ordering, idempotência, outbox         | Reprocessar mensagens duplicadas           |
| Concorrência          | Threads, async, locks, canais, backpressure            | Construir um worker pool limitado          |
| Sistemas distribuídos | Replicação, partições, consistência, consenso          | Simular queda de um nó                     |
| Load balancing        | L4/L7, round-robin, least-connections, health checks   | Retirar um backend indisponível            |
| Design                | Interfaces, composição, padrões, DDD, refatoração      | Separar regra de negócio de I/O            |
| Qualidade             | Testes, contratos, fuzzing, testes de propriedades     | Encontrar um caso limite automaticamente   |
| Operação              | Containers, CI/CD, métricas, traces, SLOs              | Diagnosticar uma regressão                 |
| Segurança             | Autorização, injeção, segredos, supply chain           | Testar limites de acesso                   |
| Engenharia            | RFCs, ADRs, revisão, incidentes, mentoria              | Documentar uma decisão e suas alternativas |

## Como conectar exemplos

Ao concluir um estudo, crie uma página temática com links relativos para as implementações,
pré-requisitos e perguntas de comparação. Use o [modelo de estudo](../docs/example-template.md) e
mantenha dados e dependências dentro de cada projeto.
