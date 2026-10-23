# Estudos de Go

Esta pasta está preparada para estudos independentes de Go. Ainda não há exemplos executáveis.

## Estrutura

Crie cada estudo em `go/<tema>/<nome>/` com README, manifesto, testes e dados sintéticos. Siga o
[modelo de estudo](../docs/example-template.md) e conecte o exemplo ao
[mapa de conceitos](../topics/README.md).

## Ferramentas

gofmt, go vet e go test. Cada estudo usa go.mod; versione go.sum quando houver dependências.
Documente as versões necessárias no README do estudo. Instale dependências dentro do projeto, sem
compartilhar uma instalação global entre os exemplos.

## Validação

Da raiz, execute `uv run python -m utils.projects check`. O CI descobre automaticamente projetos com
manifesto. Antes de adicionar um manifesto, prepare também seus testes e comandos de qualidade.
