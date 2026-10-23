# Estudos de Rust

Esta pasta está preparada para estudos independentes de Rust. Ainda não há exemplos executáveis.

## Estrutura

Crie cada estudo em `rust/<tema>/<nome>/` com README, manifesto, testes e dados sintéticos. Siga o
[modelo de estudo](../docs/example-template.md) e conecte o exemplo ao
[mapa de conceitos](../topics/README.md).

## Ferramentas

Cargo, rustfmt e Clippy. Use Cargo.toml e Cargo.lock; configure a edição no manifesto. Documente as
versões necessárias no README do estudo. Instale dependências dentro do projeto, sem compartilhar
uma instalação global entre os exemplos.

## Validação

Da raiz, execute `uv run python -m utils.projects check`. O CI descobre automaticamente projetos com
manifesto. Antes de adicionar um manifesto, prepare também seus testes e comandos de qualidade.
