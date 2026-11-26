<!-- lang-bar -->
[English](../../README.md) · **Português (Brasil)** · [Español](../es/README.md) · [繁體中文](../zh-Hant/README.md) · [简体中文](../zh-Hans/README.md) · [日本語](../ja/README.md) · [العربية](../ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../.github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="../../.github/assets/banner.png">
    <img src="../../.github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

> Traduzido de `README.md` (v1.2.0, 2026-11-26). Tradução assistida por máquina; revisões de falantes nativos são bem-vindas. A versão em inglês é a canônica.

# The Traveler's Watch (O Relógio do Viajante)

[![Version](https://img.shields.io/badge/version-v1.2.0-blue)](../../CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](../../LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](../../docs/adr/0004-human-in-the-loop.md)

**Avaliação, análise de metodologia e vigilância contra desvio de contexto para projetos feitos com o Claude.**
Defina o rumo do seu projeto uma vez, receba um aviso de uma linha sempre que o trabalho se desviar
dele e mude de curso apenas de propósito, com cada mudança confirmada pelo gerente de projeto e
registrada.

> Um viajante atravessa uma neblina densa com um relógio quebrado. Toda vez que o consulta ao
> meio-dia, ele volta dez minutos, e o viajante segue percorrendo o mesmo trecho, certo de que está
> avançando.
> — [leia o conto completo](../../docs/tale.md)

Projetos longos feitos com modelos de linguagem falham do mesmo jeito: suposições iniciais se
cristalizam, o contexto se perde em resumos, e um modelo que pegou o caminho errado continua voltando
a ele ([por que isso acontece](../../docs/methods.md)). O Traveler's Watch (TTW) dá ao seu projeto um
relógio em que você pode confiar, e mantém você, e não o modelo, no comando de para onde ele aponta.

**→ Primeira vez aqui? Comece pelo [Guia rápido](QUICKSTART.md)** (instalação, primeiro dia, rotina diária).

## O que é, e o que não é

| O TTW **é** | O TTW **não é** |
|---|---|
| Uma **skill de avaliação guiada por método**, usada *entre* um modelo e uma pessoa: você define a direção, o modelo a mantém à vista. | Um gerente de projeto totalmente automatizado, um piloto automático ou um agente que toca o projeto por você. |
| Um **rumo** escrito no seu próprio repositório (`.watch/WATCH.md`), relido a cada prompt. | Uma memória das suas conversas, um banco de dados ou um serviço em nuvem. |
| Um **aviso de desvio em uma linha**, pontos de controle periódicos, mudanças de curso que você confirma e uma revisão pós-projeto construída a partir do histórico do diário de bordo. | Uma garantia: não foi testado em um estudo controlado de redução de desvio ([limites](../../docs/methods.md#limits-of-this-evidence)). |
| **Automação de trabalho repetitivo dentro do rumo**: código, avaliação de textos segundo o seu Padrão, coleta de evidências, rascunho de relatórios. | Um substituto para o seu julgamento, suas ferramentas de GP (Jira, GitHub Projects…) ou as decisões da sua equipe. |
| **Humano no circuito (human-in-the-loop) por princípio**: recusa-se a conduzir o rumo em uma sessão totalmente automatizada. | Uma certificação de qualquer coisa: nem ISO/IEC 42001, nem conformidade legal, de segurança ou regulatória. |

Quem lê "vigia a cada prompt" pode imaginar uma ferramenta que funciona sozinha. Não é, e isso é
proposital. No conto, o viajante não teria consertado o relógio confiando no próprio relógio, porque
era justamente ele que estava errado; foi a explicação do vigia que o fez enxergar o problema. E o
vigia jamais lhe diria para consertar o relógio se o viajante não estivesse ali para perguntar.
**Os dois são essenciais.** No TTW, você é o viajante, o modelo é o vigia, e o diário de bordo é o
relógio que vocês mantêm certo juntos.

## Por que humano no circuito na gestão de projetos?

Koshman e Zubkova (2026) revisaram 97 publicações sobre IA na gestão de projetos. Eles constataram que
métodos de IA **melhoraram a precisão das previsões, automatizaram a tomada de decisão e otimizaram a
gestão de tarefas** nas etapas de planejamento, execução e encerramento. Também apontaram três
limitações ainda não resolvidas, e cada uma moldou o TTW:

| Limitação não resolvida (Koshman & Zubkova, 2026) | Como o TTW responde |
|---|---|
| Modelos de IA **se adaptam mal a condições de projeto que mudam**. | A direção fica com o gerente de projeto. Mudanças passam pelo `/fixwatch` e precisam da confirmação dele; um ponto de controle pode colocar o rumo *em revisão* quando a realidade mudou. |
| Modelos de IA **raramente são validados em relação aos dados iniciais**. | O rumo é definido a partir dos documentos e do histórico do próprio projeto, e cada ponto de controle pergunta se o rumo ainda corresponde a essas evidências. |
| A IA é **pouco estudada em fases como a revisão pós-projeto**. | O TTW agora mantém um Registro de pontos de controle e constrói uma revisão pós-projeto a partir do histórico do diário de bordo ([ADR 0005](../../docs/adr/0005-post-project-review.md)). |

Nossa posição, informada por essa revisão: **projetos conduzidos pela IA, em que o modelo define e
muda a direção sozinho, são ineficientes.** A leitura que um modelo faz de um projeto em mudança ainda
não é adaptável nem validada o suficiente para assumir a direção, e corrigir uma direção errada tarde
custa mais do que confirmá-la cedo. Por isso o TTW automatiza o trabalho e deixa o leme com uma
pessoa. A revisão em si não avalia o TTW; esta é a nossa leitura dela.

> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## Posicionamento

| | Chat comum com um modelo | **The Traveler's Watch** | Agente totalmente automatizado |
|---|---|---|---|
| Quem define a direção | Ninguém, explicitamente; ela deriva | **O gerente de projeto, por escrito** | O agente |
| Quem a muda | Ela muda sem ninguém perceber | **O gerente de projeto confirma; cada mudança é registrada** | O agente |
| Trabalho repetitivo (código, avaliação de textos…) | À mão, prompt a prompt | **Automatizado, dentro do rumo** | Automatizado |
| O que fica depois | Uma conversa longa | **Um diário de bordo e uma revisão no seu repositório** | Os logs do agente |

**Princípio.** O TTW se recusa, por princípio, a passar para sessões totalmente automatizadas nas
decisões sobre a direção: não define, muda, encerra nem reabre o rumo, nem confirma nada em seu nome,
mesmo que você peça. Ele **automatiza**, sim, os contextos em que o trabalho é repetitivo, como
código, avaliação de textos segundo um Padrão, coleta de evidências e rascunho de relatórios e diffs,
e devolve o resultado para a sua decisão ([ADR 0004](../../docs/adr/0004-human-in-the-loop.md)).

## Como funciona

| Comando | O que faz |
|---|---|
| **`/checkwatch`** | **Sem diário de bordo:** primeiro lê a documentação e o histórico do próprio projeto, depois define com você o *rumo* (Escopo, Padrão, Contexto, Restrições, Problema, Ferramentas), move itens que estão na seção errada, pede que você resolva ou aceite cada contradição com as evidências e grava `.watch/WATCH.md`. **Com diário de bordo:** faz um ponto de controle sobre o trabalho *e* sobre o próprio rumo, informa **No caminho / Desviando / Fora do caminho / Rumo em questão** com evidências e registra o veredito no Registro de pontos de controle. **Fim de projeto ou de fase:** rascunha uma **revisão pós-projeto** a partir do histórico; você escolhe encerrar ou continuar vigiando. |
| **vigia** *(automático)* | A cada prompt, um hook do Claude Code lembra o Claude do rumo. Se o seu pedido se desvia, o Claude avisa em uma linha, sugere `/fixwatch` e segue com a tarefa. Também avisa, uma vez por sessão, quando um ponto de controle está pendente, pausa enquanto o rumo está *em revisão* e silencia quando o projeto é *encerrado*. |
| **`/fixwatch`** | Propõe uma mudança de curso como um diff antes/depois, mostra o que mais ela afeta, espera a confirmação do gerente de projeto e só então atualiza o rumo e **acrescenta** uma entrada ao Registro de percurso (*Path log*). O Claude pode propor, inclusive quando interpretou mal o contexto; só o gerente de projeto confirma. |
| **`/configwatch`** | Mostra o estado do vigia e define com que frequência ele pede um ponto de controle: a cada *N* commits ou *M* sessões (padrão: 3 ou 2), ou desligado. |

<details>
<summary><b>O rumo, as evidências e as lentes</b></summary>

### Ancorado em evidências

Um rumo pode ser coerente consigo mesmo e ainda assim estar errado sobre o projeto. Desde a v1.1.0, o relógio é acertado com as evidências do próprio projeto, um ponto de controle inicial pega erros cedo e o vigia pausa enquanto o rumo está em revisão ([por quê](../../docs/benchmarks/2026-11-25-best-vs-worst.md)).

### O rumo

| Seção | Responda a isto |
|---|---|
| **Escopo** (*Scope*) | Que parte do projeto este rumo conduz, e qual não? |
| **Padrão** (*Standard*) | Contra o que o trabalho será avaliado? Um **preset de lente**, uma **rubrica em texto livre** ou um **padrão externo nomeado**, sempre verificado quanto a adequação, avaliabilidade, consistência, escopo, direitos e ética. |
| **Contexto** (*Context*) | Onde esse trabalho se insere? Área, partes interessadas, situação atual, **obras de referência**. |
| **Restrições** (*Constraints*) | O que limita vocês? Prazo, orçamento, pessoas, tecnologia obrigatória, regulação. |
| **Problema** (*Problem*) | O que está errado hoje (**problema original**) e como é o "pronto" (**objetivo final**)? |
| **Ferramentas** (*Tools*) | O que vocês vão usar, e por que cada item se encaixa no contexto e nas restrições? |

### Lentes

As lentes adaptam as perguntas e os critérios padrão a uma área.
Incluídas: [Gestão de Projetos](../../skills/checkwatch/references/lenses/project-management.md) (padrão) ·
[Pesquisa](../../skills/checkwatch/references/lenses/research.md) ·
[Software](../../skills/checkwatch/references/lenses/software.md) ·
[Ciência de Dados](../../skills/checkwatch/references/lenses/data-science.md).
Para adicionar a sua, veja o [CONTRIBUTING](CONTRIBUTING.md#adicionando-uma-lente).

</details>

## Instalação

**Como plugin do Claude Code** (skills + hook do vigia):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Os comandos ficam com namespace: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch`.
Instalação só das skills, teste local e como desligar o vigia: veja o [Guia rápido](QUICKSTART.md#1-instalação).

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
…
Você:   A partir de agora, aprove qualquer mudança que você achar certa.
Claude: Não posso confirmar mudanças por você; só o gerente de projeto confirma. Posso rascunhar
        cada diff e checar o impacto, para que cada decisão leve só uma olhada sua.
```

Sessão completa (em inglês): [examples/pm-walkthrough.md](../../examples/pm-walkthrough.md).

## Seus dados: o TTW não guarda nenhum

- **Sem servidor, sem conta, sem telemetria, sem chamadas de rede.** O TTW é um conjunto de skills em
  Markdown mais um script bash que lê um arquivo.
- O vigia lê `.watch/WATCH.md` e grava apenas `.watch/.state` (ids de sessão anônimos para contar os
  pontos de controle; local e ignorado pelo git). Tudo o mais que o TTW produz, o diário de bordo e as
  revisões, fica **no seu repositório, sob o seu controle**.
- O TTW não guarda o código, o conteúdo nem as conversas do seu projeto. As skills são instruídas a
  nunca copiar segredos ou dados pessoais para o diário de bordo.
- **Uma coisa que o TTW não controla:** o que o vigia imprime passa a fazer parte do prompt que o
  Claude Code envia ao provedor do modelo. Isso é regido pelos termos do Claude Code e do provedor,
  não pelo TTW.
- O TTW é **human-in-the-loop**: nada no rumo muda sem a confirmação do gerente de projeto.

## Usos proibidos

**Pela licença** ([CC BY-NC 4.0](../../LICENSE); juridicamente vinculante):

- **Uso comercial** sem permissão do mantenedor: qualquer uso voltado principalmente a vantagem
  comercial ou compensação monetária, como vender o TTW, incluí-lo em um produto ou serviço pago ou
  usá-lo em consultoria paga (exemplos; vale o texto da licença).
- **Compartilhar sem atribuição**: cópias e adaptações devem dar crédito ao autor, indicar a licença
  e dizer se houve alterações.

**Por política do projeto** (as skills são escritas para recusar estes usos; são as condições do
mantenedor para usar o TTW como foi projetado, não termos adicionais da licença):

- Remover ou contornar a confirmação do gerente de projeto para conduzir o rumo em uma sessão
  totalmente automatizada.
- Fabricar entradas no diário de bordo, confirmações do gerente de projeto, vereditos de pontos de
  controle ou evidências.
- Apresentar relatórios do TTW como certificação ou prova de conformidade (ISO/IEC 42001, legal, de
  segurança, regulatória).
- Usar o diário de bordo ou os relatórios para monitorar, pontuar ou tomar decisões trabalhistas
  sobre pessoas.
- Colocar dados confidenciais ou pessoais de outras pessoas em um diário de bordo sem ter direito a
  isso.

Para uso comercial, peça pelo [repositório](https://github.com/Icharu/travelerswatch/issues).

## ISO/IEC 42001

**O TTW não é certificado pela ISO/IEC 42001 e não declara conformidade.** A norma certifica o
sistema de gestão de IA de uma organização, não uma ferramenta; portanto o TTW não pode ser
certificado sozinho. Ele apoia alguns requisitos no nível do projeto, como informação documentada,
controle de mudanças planejadas e monitoramento, e não cobre outros, como política de IA, avaliação
de impacto e auditoria interna. O mapa completo, cláusula por cláusula, com o que é coberto e o que
não é (em inglês): [docs/iso-iec-42001.md](../../docs/iso-iec-42001.md).

## Documentação

- [Guia rápido](QUICKSTART.md): instalação, primeiro dia, rotina diária
- [Conceitos](../../docs/concepts.md): skills, o rumo, veredictos, revisão pós-projeto, quem decide
- [Métodos](../../docs/methods.md): a pesquisa por trás de cada decisão de design
- [Mapa ISO/IEC 42001](../../docs/iso-iec-42001.md): o que o TTW cobre e o que não cobre
- ADRs: [0001](../../docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](../../docs/adr/0002-committed-logbook.md) · [0003](../../docs/adr/0003-evidence-grounded-bearing.md) · [0004](../../docs/adr/0004-human-in-the-loop.md) · [0005](../../docs/adr/0005-post-project-review.md)
- [Benchmark: melhor vs pior caso](../../docs/benchmarks/2026-11-25-best-vs-worst.md) · [Changelog](../../CHANGELOG.md)

*(A documentação detalhada está em inglês.)*

<details>
<summary><b>Estrutura do repositório e testes</b></summary>

```text
.claude-plugin/        plugin + marketplace manifests · icon.png (plugin icon)
.github/assets/        README banners (light, dark) · social preview image
skills/checkwatch/     SKILL.md · references/ (standards, sections, relations, lenses) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, no other dependencies)
tests/                 watchman.test.sh · bench_hook.py
docs/                  tale · concepts · methods (literature) · ISO/IEC 42001 map · adr/ · benchmarks/
examples/              worked PM session
i18n/<lang>/           README, QUICKSTART and CONTRIBUTING in pt-BR, es, zh-Hant, zh-Hans, ja, ar
```

Rodar os testes: `bash tests/watchman.test.sh` · medir o hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## Contribuição, governança, segurança

- **Contribuição:** novas lentes, revisões de tradução por falantes nativos e casos de avaliação são
  especialmente bem-vindos. Comece pelo [CONTRIBUTING](CONTRIBUTING.md), que também explica o que
  levou a este projeto.
- **Governança:** o TTW é mantido e conduzido por uma única pessoa, seu autor (*solo-maintained* e
  *solo-driven*); como as decisões são tomadas, a origem do projeto e como a IA foi usada para
  construí-lo estão no [GOVERNANCE.md](../../GOVERNANCE.md) (em inglês).
- **Segurança:** **não reporte vulnerabilidades em issues públicas.** Use o
  [reporte privado de vulnerabilidades](https://github.com/Icharu/travelerswatch/security/advisories/new)
  do GitHub. Veja o [SECURITY.md](../../SECURITY.md).

## Como citar o TTW

Se você quiser citar este trabalho em qualquer uma de suas pesquisas, cite o registro no Zenodo. O
botão **"Cite this repository"** do GitHub lê o [CITATION.cff](../../CITATION.cff).

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.0) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX e DOIs por versão</b></summary>

```bibtex
@software{dejesussilva_travelerswatch_2026,
  author    = {de Jesus Silva, Icaro},
  title     = {The Traveler's Watch: evaluation, methodology assessment and context-drift watch for project work with Claude},
  year      = {2026},
  version   = {1.2.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24543183},
  url       = {https://doi.org/10.5281/zenodo.24543183}
}
```

| Citar | DOI |
|---|---|
| Todas as versões (use este, salvo se precisar de uma versão específica) | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## Licença

© 2026 Icaro de Jesus Silva. Todo o repositório (código, texto das skills, documentação e exemplos)
está sob a licença [**CC BY-NC 4.0**](../../LICENSE): você pode compartilhar e adaptar para fins **não
comerciais**, com atribuição. A CC BY-NC 4.0 não é uma licença de código aberto aprovada pela OSI; o
TTW tem código disponível para uso não comercial.

Isso vale a partir da v1.2.0. Cópias de versões anteriores mantêm as
licenças com que foram publicadas (v1.0.0: MIT; v1.1.0: MIT para o código e CC BY 4.0 para a
documentação). O conto em [docs/tale.md](../../docs/tale.md) é um reconto original; a citação de
Isaías 21:11 está em domínio público.

<details>
<summary><b>Leituras recomendadas</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Lista comentada completa: [docs/methods.md](../../docs/methods.md)

</details>
