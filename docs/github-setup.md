# Configuração do GitHub

Este guia descreve a automação de brunosrz/src e como reaplicá-la com GitHub CLI. A configuração de
um app no repositório não substitui sua instalação na conta.

## Configuração aplicada

O repositório usa main, issues habilitadas, squash merge, título e corpo do PR no commit, exclusão
de branches após merge e labels versionadas em [.github/labels.json](../.github/labels.json). A
visibilidade permanece privada.

```sh
gh auth status
uv run python -m utils.sync_labels
gh repo edit brunosrz/src --enable-squash-merge --enable-merge-commit=false --enable-rebase-merge=false --delete-branch-on-merge
```

O script de labels cria ou atualiza as entradas do catálogo; não remove labels que alguém tenha
criado manualmente. Novas linguagens e temas precisam também de regras no labeler.

## Checks e permissões

O workflow PR Checks roda em push para main, PR e disparo manual. Ele verifica título, hooks, tipos
e testes das ferramentas em Linux e Windows. Estudos são descobertos por manifesto e executados em
Linux, com a toolchain correspondente.

O job consolidado chama-se `PR checks`. Quando não há manifestos de estudos, registra isso
explicitamente; os checks compartilhados continuam obrigatórios. O hook de estudos é omitido no job
de ferramentas porque os projetos são verificados nos jobs próprios.

O labeler usa pull_request_target apenas para metadados. Não faz checkout nem executa código do PR.
As Actions estão fixadas por SHA; Dependabot propõe atualizações semanais. O token padrão tem
leitura; cada workflow declara permissões adicionais estritamente necessárias.

## Proteção de main

A política desejada exige PR, check `PR checks` atualizado, conversas resolvidas e histórico linear,
sem force push ou exclusão. Aprovação humana mínima é zero porque o mantenedor trabalha sozinho;
colaboradores futuros podem elevar esse número.

No bootstrap, a consulta de rulesets retornou HTTP 403: o plano atual exige GitHub Pro ou
repositório público para esse recurso. A política está versionada em
[.github/branch-protection.json](../.github/branch-protection.json) para aplicação quando
disponível:

```sh
gh api --method PUT repos/brunosrz/src/branches/main/protection --input .github/branch-protection.json
gh api repos/brunosrz/src/branches/main/protection
```

Um check verde não significa que a proteção está ativa. Confirme o resultado da API ou as
configurações da branch depois de mudar o plano ou tornar o repositório público.

## Releases

Release Please usa uma versão única do conjunto de estudos, manifesto, version.txt e CHANGELOG.md. O
merge de um PR de release cria tag e release; não publica pacotes em registries. A primeira
referência local é 0.1.0, ainda sem tag publicada.

O workflow usa GITHUB_TOKEN. Como PRs criados por esse token não disparam outros workflows
automaticamente, o passo seguinte solicita workflow_dispatch do PR Checks na branch de release do
próprio github-actions[bot]. Esse workflow tem apenas leitura. Não é necessário copiar um PAT
pessoal para secrets.

A permissão de Actions para criar PRs foi habilitada. O workflow não aprova nem faz merge de PRs
automaticamente. Consulte a
[documentação do Release Please](https://github.com/googleapis/release-please-action) para a
limitação de eventos do token.

## Bots de revisão

O CodeRabbit está configurado em [.coderabbit.yaml](../.coderabbit.yaml), em português, com foco
didático. Para ativá-lo, instale o [GitHub App CodeRabbit](https://github.com/apps/coderabbitai) com
acesso ao repositório; confira plano e permissões na instalação. A
[referência de configuração](https://docs.coderabbit.ai/reference/configuration) explica os campos.

O Vectora Bot mantém o contrato recebido no arquivo
[.github/vectora-review.yml](../.github/vectora-review.yml): revisão sob demanda pela label vectora
ou comando do bot; correção automática de CI desabilitada. A instalação e o acesso precisam ser
conferidos no painel do mantenedor do Vectora Bot. Nenhum endpoint, credencial ou schema novo foi
presumido.

A autenticação atual do gh não permite enumerar instalações de GitHub Apps. Portanto, a ativação
desses dois apps não foi comprovada por essa API. Os checks de CI não dependem de seus pareceres.

GitHub Actions e Dependabot cobrem a automação nativa. O arquivo de instruções do Copilot pode
orientar revisões quando esse recurso estiver disponível na conta; ele não instala nem habilita uma
assinatura.

## Antes de tornar público

Escolha uma licença, confira atribuições e revise conteúdo e histórico por segredos. Depois de mudar
a visibilidade, aplique a proteção de main e confira as permissões de execução de workflows para
forks. Não exponha credenciais em exemplos ou logs.

Para atualizar ferramentas Python, altere pyproject.toml e uv.lock juntos. Atualizações do
pre-commit usam `uv run pre-commit autoupdate`; valide o diff e os hooks antes de commitar.
