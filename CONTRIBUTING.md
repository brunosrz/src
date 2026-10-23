# Como contribuir

Contribuições devem ajudar alguém a compreender e reproduzir um conceito, incluindo seus limites.
Documentação, correções e novos exercícios são bem-vindos.

## Fluxo de trabalho

1. Abra uma issue para uma proposta ampla; correções pequenas podem ir direto a um PR.
2. Sincronize `main` e crie uma branch curta: `feat/pub-sub`, `docs/cache` ou `fix/example-timeout`.
3. Faça um estudo por PR, seguindo o [modelo](docs/example-template.md).
4. Execute os checks e registre os comandos e resultados no PR.
5. Resolva a revisão; o mantenedor faz squash merge quando os checks passarem.

Títulos de PR e commits seguem `tipo(escopo): descrição`. Exemplos:
`feat(go): demonstrate bounded worker pool`, `docs(cache): explain invalidation trade-offs`. Tipos
aceitos: feat, fix, docs, refactor, test, chore, ci, perf, build e revert. O escopo é opcional;
títulos têm até 100 caracteres.

## Organização dos estudos

Use nomes em kebab-case: `python/messaging/in-memory-pub-sub/`. Não crie uma dependência global
entre todos os estudos. O índice temático deve apontar para cada implementação concluída.

Cada estudo precisa de README, manifesto de dependências, testes automatizados e dados sintéticos.
Serviços externos precisam de instruções de inicialização e limpeza; não exija credenciais reais nos
testes padrão.

Um manifesto marca um estudo como executável: `pyproject.toml`, `go.mod`, `Cargo.toml`,
`package.json` ou `CMakeLists.txt`. O CI descobre a raiz do projeto e ignora manifestos internos de
workspaces. Coloque a configuração de teste nesse projeto raiz.

## Qualidade por linguagem

- Python: uv.lock, Ruff, ty e pytest como dependências de desenvolvimento; tipos completos.
- Go: gofmt, go vet e go test; execute testes com race detector quando suportado.
- Rust: Cargo.lock, rustfmt, Clippy e cargo test; toolchain estável.
- TypeScript: package-lock.json; scripts `lint`, `typecheck` e `test` sem watch; strict no tsconfig.
- C++: CMake, compilação e CTest com testes registrados; clang-format para formatação. Configure
  C++20 ou superior no projeto.

Novas linguagens exigem atualização do detector, runner, CI e labels. Registre versões nos
manifestos e README. Para comparar implementações, use os mesmos dados e explicite diferenças de
semântica.

## Verificações locais

Instale as ferramentas com `uv sync --locked` e os hooks com `uv run pre-commit install`. Em
seguida:

```sh
uv run pre-commit run --all-files
uv run ruff check utils tests
uv run ty check utils tests
uv run pytest
uv run python -m utils.projects check
```

Os hooks podem corrigir formatação: revise e adicione os arquivos novamente. Não use `--no-verify`.
Pastas sem estudos são ignoradas, mas um projeto existente com ferramenta ausente falha
explicitamente.

## Revisão e comportamento

Explique o motivo de uma sugestão e trate dúvidas com respeito. Revisões automatizadas são apoio: o
autor continua responsável por entender o código. Não inclua segredos, dados pessoais ou material de
terceiros sem permissão.

Reporte problemas com reprodução mínima. Para vulnerabilidades que exponham credenciais ou dados,
use o canal privado disponível no GitHub; não publique o segredo na issue.
