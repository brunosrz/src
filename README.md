# src — estudos de engenharia de software

Um laboratório para aprender desenvolvimento com profundidade: escrever código, entender sistemas,
testar hipóteses e explicar decisões. O objetivo é construir repertório para atuar com autonomia e
responsabilidade; senioridade também envolve comunicação, colaboração e experiência real.

A base de contribuição e automação está sendo estabelecida. As pastas de linguagens ainda não contêm
estudos executáveis; os temas abaixo são uma trilha planejada.

## Por onde começar

1. Leia o [roadmap](docs/roadmap.md) e escolha um problema pequeno.
2. Consulte o [mapa de conceitos](topics/README.md).
3. Escolha uma linguagem e siga o [modelo de estudo](docs/example-template.md).
4. Implemente, teste casos de erro e documente o que aprendeu.
5. Abra um PR conforme o [guia de contribuição](CONTRIBUTING.md).

## Organização

Cada estudo vive em `<linguagem>/<tema>/<nome>/`, com dependências e testes próprios. Um conceito
pode ter implementações em várias linguagens, conectadas por links.

| Pasta                          | Foco                                                |
| ------------------------------ | --------------------------------------------------- |
| [python/](python/README.md)    | Python, tipagem, automação, serviços e concorrência |
| [go/](go/README.md)            | Go, interfaces, goroutines, canais e serviços       |
| [cpp/](cpp/README.md)          | C++, memória, RAII, desempenho e sistemas           |
| [ts/](ts/README.md)            | TypeScript, tipos, runtime, APIs e aplicações       |
| [rust/](rust/README.md)        | Rust, ownership, traits, segurança e concorrência   |
| [topics/](topics/README.md)    | Conceitos independentes de linguagem                |
| [docs/](docs/roadmap.md)       | Roadmap, padrões e operação do repositório          |
| [utils/](utils/README.md)      | Validadores e execução dos checks                   |
| [tests/](tests/test_checks.py) | Testes das ferramentas compartilhadas               |

## Preparar o ambiente

Instale Git e uv. O uv gerencia o Python 3.14 da raiz. O pre-commit provisiona seus ambientes de
Node e Go para Prettier e actionlint; isso requer rede na primeira execução.

```sh
git clone https://github.com/brunosrz/src.git
cd src
uv sync --locked
uv run pre-commit install
uv run pre-commit run --all-files
uv run pytest
```

Para contribuir enquanto o repositório é privado, é necessário ter acesso no GitHub. Instale apenas
as toolchains dos estudos em que trabalhar; cada README deve informar versões e comandos. O comando
`uv run python -m utils.projects check` verifica todos os projetos existentes e falha se uma
ferramenta necessária estiver ausente.

## O que estudar

A trilha abrange algoritmos, estruturas de dados, Git, redes, sistemas operacionais, testes, design
de APIs, SQL, NoSQL, busca vetorial, cache, mensageria, eventos, pub/sub, sistemas distribuídos,
load balancing, segurança, observabilidade e entrega de software.

Os estudos devem mostrar quando usar uma técnica, quando evitá-la e como observar seus limites.
Benchmarks devem registrar ambiente e metodologia; números isolados não demonstram superioridade de
uma linguagem.

## Colaboração e automação

Issues descrevem problemas ou objetivos de aprendizagem. PRs usam Conventional Commits, testes e
explicações. O CI verifica ferramentas compartilhadas e descobre estudos com manifestos; pastas
vazias não contam como projetos testados.

O processo mantém o desenvolvedor no controle: cada tarefa começa com critérios observáveis, cada
mudança passa por diff e testes, e cada entrega declara evidências reais e limitações. A IA pode
acelerar exploração e implementação, mas decisões, revisão e aprovação continuam sendo
responsabilidades humanas.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md) e
[configuração do GitHub](docs/github-setup.md). CodeRabbit e Vectora Bot dependem de instalação
externa; seus arquivos de configuração não comprovam que estejam ativos.

## Uso do conteúdo

Ainda não foi escolhida uma licença pública. Antes de tornar o repositório público, o mantenedor
deve escolher uma licença e revisar a origem dos materiais. Exemplos copiados precisam preservar
atribuição e licença; exercícios devem usar dados sintéticos.
