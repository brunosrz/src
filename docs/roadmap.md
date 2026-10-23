# Roadmap de aprendizado

Esta trilha é planejada, não uma lista de funcionalidades prontas. Avance por evidências de
compreensão, sem tratar quantidade de linguagens como medida de senioridade.

## Fundamentos

Estude Git, terminal, debugging, tipos, memória, complexidade, estruturas de dados, algoritmos,
processos, threads, arquivos, TCP, DNS, HTTP e TLS.

Entregável sugerido: uma API pequena com validação, testes, documentação e histórico de commits
compreensível. Explique onde o tempo e a memória são gastos.

## Modelagem, testes e persistência

Explore design modular, composição, interfaces, orientação a objetos e programação funcional.
Compare testes unitários, integração, contratos e ponta a ponta; pratique refatoração guiada por
testes.

Em SQL, estude modelagem, constraints, transações, isolamento, índices, planos de execução e
migrações. Em NoSQL, compare documentos, chave-valor, colunas e grafos a partir de padrões de
acesso. Em busca vetorial, explore embeddings, distâncias, ANN, recall e filtros.

Entregável sugerido: o mesmo caso de uso com duas estratégias de persistência e uma comparação
justificada.

## Concorrência, eventos e distribuição

Compare sincronismo e assincronismo, locks, canais, cancelamento e backpressure. Estude filas e
pub/sub, entrega pelo menos uma vez, idempotência, ordenação, retries, dead-letter queues, outbox e
consistência eventual.

Explore cache-aside, TTL, invalidação, stampede, rate limiting, balanceamento L4/L7, health checks,
sticky sessions, replicação, particionamento e tolerância a falhas.

Entregável sugerido: um fluxo de processamento que suporte mensagens duplicadas, queda de consumidor
e indisponibilidade temporária.

## Operação e decisões de engenharia

Estude logs estruturados, métricas, traces, SLIs/SLOs, profiling, carga, capacidade, CI/CD,
containers, rollbacks e gestão de segredos. Relacione segurança a autenticação, autorização,
injeção, dependências e limites de confiança.

Entregável sugerido: serviço com dashboard, teste de carga reproduzível, simulação de falha e relato
do diagnóstico.

## Prática de senioridade

Escreva propostas curtas com alternativas, restrições, custo e plano de migração. Pratique revisão,
comunicação de incidentes, mentoria e divisão de problemas. Discuta decisões em função do contexto,
em vez de transformar padrões em regras universais.

Um estudo está concluído quando outra pessoa consegue executá-lo, entender suas escolhas e modificar
um requisito com confiança.
