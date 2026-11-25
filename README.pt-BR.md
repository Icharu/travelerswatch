<!-- lang-bar -->
[English](README.md) · **Português (Brasil)** · [Español](README.es.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [العربية](README.ar.md)

> Traduzido de `README.md` v1.0.0 (2026-11-25). Tradução assistida por máquina; revisões de falantes nativos são bem-vindas. A versão em inglês é a canônica.

# The Traveler's Watch (O Relógio do Viajante)

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending%20(Zenodo)-lightgrey)](CITATION.cff)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**Avaliação, análise de metodologia e vigilância contra desvio de contexto para projetos feitos com o Claude.**
Defina o rumo do seu projeto uma vez, receba um aviso de uma linha sempre que o trabalho se desviar
dele e mude de curso apenas de propósito, com cada mudança confirmada pelo gerente de projeto e
registrada.

> Um viajante atravessa uma neblina densa com um relógio quebrado. Toda vez que o consulta ao
> meio-dia, ele volta dez minutos, e o viajante segue percorrendo o mesmo trecho, certo de que está
> avançando.
> — [leia o conto completo](docs/tale.md)

Projetos longos feitos com modelos de linguagem falham do mesmo jeito: suposições iniciais se
cristalizam, o contexto se perde em resumos, e um modelo que pegou o caminho errado continua voltando
a ele ([por que isso acontece](docs/methods.md)). O Traveler's Watch dá ao seu projeto um relógio em que
você pode confiar.

## Como funciona

| Comando | O que faz |
|---|---|
| **`/checkwatch`** | **Sem diário de bordo:** define com você o *rumo* (Padrão, Contexto, Restrições, Problema, Ferramentas), move itens que estão na seção errada, aponta as tensões entre seções e grava `.watch/WATCH.md`. **Com diário de bordo:** faz um ponto de controle e informa **No caminho / Desviando / Fora do caminho**, com evidências. |
| **vigia** *(automático)* | A cada prompt, um hook do Claude Code lembra o Claude do rumo. Se o seu pedido se desvia, o Claude avisa em uma linha, sugere `/fixwatch` e segue com a tarefa. |
| **`/fixwatch`** | Propõe uma mudança de curso como um diff antes/depois, mostra o que mais ela afeta, espera a confirmação do gerente de projeto e só então atualiza o rumo e **acrescenta** uma entrada ao Registro de percurso (*Path log*). O Claude pode propor, inclusive quando interpretou mal o contexto; só o gerente de projeto confirma. |

### O rumo

| Seção | Responda a isto |
|---|---|
| **Padrão** (*Standard*) | Contra o que o trabalho será avaliado? Um **preset de lente**, uma **rubrica em texto livre** ou um **padrão externo nomeado**, sempre verificado quanto a adequação, avaliabilidade, consistência, escopo, direitos e ética. |
| **Contexto** (*Context*) | Onde esse trabalho se insere? Área, partes interessadas, situação atual, **obras de referência**. |
| **Restrições** (*Constraints*) | O que limita vocês? Prazo, orçamento, pessoas, tecnologia obrigatória, regulação. |
| **Problema** (*Problem*) | O que está errado hoje (**problema original**) e como é o "pronto" (**objetivo final**)? |
| **Ferramentas** (*Tools*) | O que vocês vão usar, e por que cada item se encaixa no contexto e nas restrições? |

### Lentes

As lentes adaptam as perguntas e os critérios padrão a uma área.
Incluídas: [Gestão de Projetos](skills/checkwatch/references/lenses/project-management.md) (padrão) ·
[Pesquisa](skills/checkwatch/references/lenses/research.md) ·
[Software](skills/checkwatch/references/lenses/software.md) ·
[Ciência de Dados](skills/checkwatch/references/lenses/data-science.md).
Para adicionar a sua, veja [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens).

## Instalação

**Como plugin do Claude Code** (skills + hook do vigia):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Os comandos ficam com namespace: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`.

**Somente as skills** (Claude Code ou qualquer agente que leia [Agent Skills](https://agentskills.io/); sem hook):

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch ~/.claude/skills/
```

Os comandos passam a ser `/checkwatch` e `/fixwatch`. Sem o hook, rode `/checkwatch` no início de
cada sessão de trabalho.

**Testar localmente sem instalar:** `claude --plugin-dir ./travelerswatch`

**Desligar o vigia temporariamente:** `export TRAVELERSWATCH_DISABLE=1`

## Exemplo rápido

```text
Você:   /checkwatch
Claude: Ainda não há diário de bordo. Primeiro, o Padrão: preset de lente, sua própria rubrica ou um padrão nomeado?
Você:   Lente de GP. Contexto: só temos duas pessoas em meio período. Problema: criar um app de coleta.
Claude: "Só duas pessoas em meio período" é uma limitação, então vai para Restrições.
        "Criar um app de coleta" é uma solução. Qual é o problema por trás dela, e como é o "pronto"?
…
Você:   Vamos adicionar um app gamificado para a cidade inteira.
Claude: ⚠️ Vigia: desvia do Problema (dois distritos-piloto) e das Restrições (orçamento de 20 mil).
        Continuar ou /fixwatch?
```

Sessão completa (em inglês): [examples/pm-walkthrough.md](examples/pm-walkthrough.md).

## Estrutura do repositório

```text
.claude-plugin/        manifests do plugin e do marketplace
skills/checkwatch/     SKILL.md · references/ (padrões, seções, relações, lentes) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, sem outras dependências)
tests/                 watchman.test.sh
docs/                  conto · conceitos · métodos (literatura) · adr/
examples/              sessão de GP comentada
```

Rodar os testes: `bash tests/watchman.test.sh`

## Documentação

- [Conceitos](docs/concepts.md): skills, o rumo, veredictos, quem decide
- [Métodos](docs/methods.md): a pesquisa por trás de cada decisão de design
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md)
- [Changelog](CHANGELOG.md)

*(A documentação detalhada está em inglês.)*

## Contribuindo

Contribuições são bem-vindas, especialmente **novas lentes** para outras áreas, traduções revisadas
por falantes nativos e novos casos de avaliação. Leia o [CONTRIBUTING.md](CONTRIBUTING.md) antes de
abrir um pull request.

## Segurança

**Não reporte vulnerabilidades em issues públicas.** Use o
[reporte privado de vulnerabilidades](https://github.com/Icharu/travelerswatch/security/advisories/new)
do GitHub (aba **Security**, depois **Report a vulnerability**). Os prazos de resposta são de melhor
esforço e dependem da severidade. Veja o [SECURITY.md](SECURITY.md) para o escopo, a tabela de
respostas e o que fazer enquanto aguarda.

## Citação

Se você usar o Traveler's Watch em pesquisa ou ensino, por favor cite-o. O botão
**"Cite this repository"** do GitHub lê o [CITATION.cff](CITATION.cff). Um DOI do Zenodo será
adicionado aqui assim que a v1.0.0 for lançada.

## Licença

[MIT](LICENSE) © 2026 Icaro de Jesus Silva. O conto em [docs/tale.md](docs/tale.md) é um reconto
original; a citação de Isaías 21:11 está em domínio público.

## Leituras recomendadas

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Lista comentada completa: [docs/methods.md](docs/methods.md)
