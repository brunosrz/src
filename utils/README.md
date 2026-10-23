# Ferramentas compartilhadas

As ferramentas são módulos Python executados com o ambiente uv da raiz. Seus testes ficam em tests/.

## Comandos

| Comando                                                               | Finalidade                                  |
| --------------------------------------------------------------------- | ------------------------------------------- |
| `uv run python -m utils.check_commit --title "docs: explain cache"`   | Validar título de PR                        |
| `uv run python -m utils.check_commit .git/COMMIT_EDITMSG`             | Validar mensagem no hook                    |
| `uv run python -m utils.check_links README.md`                        | Verificar destinos locais de links Markdown |
| `uv run python -m utils.projects discover`                            | Gerar matriz JSON dos estudos               |
| `uv run python -m utils.projects check`                               | Executar checks de todos os estudos         |
| `uv run python -m utils.projects check --project python/tema/exemplo` | Verificar um projeto existente              |
| `uv run python -m utils.sync_labels`                                  | Sincronizar labels via gh                   |

O verificador de links cobre links inline relativos, ignora blocos de código, âncoras e URLs
externas; não valida IDs de títulos nem sintaxe de links por referência. Ele não realiza requisições
de rede.

O runner descobre manifestos somente nas pastas das linguagens e ignora diretórios gerados.
Workspaces aninhados são verificados pelo manifesto mais externo. Ferramentas ausentes e testes
vazios de Python/C++ geram falha. TypeScript deve configurar seu runner para falhar sem testes.

## Migração da base anterior

Foram preservados os propósitos dos templates, labeler, PR checks, Release Please e revisão Vectora,
com configurações ajustadas ao src. Os hooks de higiene, Ruff, Prettier e actionlint continuam na
base.

Foram removidos scripts de tradução, seleção/rotação de release, canais de atualização, milestones
de produto, deploys e testes da aplicação Vectora. Os validadores antigos de comentários e
referências específicas foram substituídos por validação de commits e links locais, sem proibir
vocabulário legítimo em material de estudo.

Uma cópia local dos arquivos originais foi preservada em .git/bootstrap-originals durante o
bootstrap; ela não é parte do repositório versionado.
