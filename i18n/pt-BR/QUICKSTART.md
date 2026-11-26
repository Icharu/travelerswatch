<!-- lang-bar -->
[English](../../QUICKSTART.md) · **Português (Brasil)** · [Español](../es/QUICKSTART.md) · [繁體中文](../zh-Hant/QUICKSTART.md) · [简体中文](../zh-Hans/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [العربية](../ar/QUICKSTART.md)

> Traduzido de `QUICKSTART.md` (Unreleased, 2026-11-25). Tradução assistida por máquina; a versão em inglês é a canônica.

# Guia rápido

Instale o The Traveler's Watch (TTW), defina o rumo do seu projeto no primeiro dia e use-o todos os
dias depois disso. Voltar ao [README](README.md).

**O TTW é conduzido no dia a dia (daily-led).** Você conduz o trabalho de cada dia. O vigia mantém o
rumo à vista a cada prompt, e o diário de bordo guarda o histórico; assim, cada dia começa de onde o
projeto realmente está, e não do que o modelo lembra.

## 1. Instalação

Escolha uma opção.

| Opção | Comandos | O que você recebe |
|---|---|---|
| **Plugin do Claude Code** (recomendado) | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | Skills + o vigia automático. Comandos: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch` |
| **Só as skills** (Claude Code ou qualquer agente de [Agent Skills](https://agentskills.io/)) | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | Skills, sem vigia. Comandos: `/checkwatch`, `/fixwatch`, `/configwatch`. Rode `/checkwatch` à mão no início de cada sessão. |
| **Testar sem instalar** | `claude --plugin-dir ./travelerswatch` | Tudo, só nesta sessão |

Requisitos: Claude Code para o vigia; `bash` e `awk` (macOS e Linux já têm); `git` é opcional, mas
habilita a contagem de commits e a revisão pós-projeto completa.

## 2. Primeiro dia: defina o rumo

1. Abra o Claude Code na pasta raiz do projeto.
2. Rode **`/checkwatch`**. Responda em uma linha: o que é o projeto e que parte dele este rumo conduz.
3. O Claude lê o seu README, `docs/` e o histórico recente do git, e mostra um **cartão de
   evidências** e **rascunhos** de cada seção. Você os corrige; ele pergunta sobre lacunas, itens na
   seção errada e qualquer ponto em que suas respostas contradizem as evidências. Conte com cerca de
   cinco rodadas.
4. Confirme o rumo. O Claude grava `.watch/WATCH.md` e adiciona `.watch/.state` ao `.gitignore`.
5. **Faça commit do diário de bordo**: `git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`.

A partir daqui, nada no rumo muda sem a sua confirmação.

## 3. Todos os dias

| Quando | O que você faz | O que o TTW faz |
|---|---|---|
| **Início do dia** | Abra o Claude Code e trabalhe normalmente. | O vigia relê `.watch/WATCH.md` no seu primeiro prompt; as mudanças confirmadas ontem já valem. |
| **Durante o trabalho** | Peça o que precisar: código, revisões, rascunhos. | O trabalho repetitivo é feito dentro do rumo. Se um pedido se desvia, o Claude avisa em **uma linha** e segue. |
| **Aparece um aviso de desvio** | Decida: foi um desvio de percurso, ou o caminho está mudando de fato? | Desvio: só continue. Mudança real: rode **`/fixwatch`**, revise o diff e o impacto, e confirme ou cancele. |
| **"Um ponto de controle está pendente"** | Rode **`/checkwatch`** quando tiver um minuto. | Informa *No caminho / Desviando / Fora do caminho / Rumo em questão* com evidências e acrescenta uma linha ao Registro de pontos de controle. |
| **Fim do dia** | Faça commit de `.watch/WATCH.md` junto com o seu trabalho, se ele mudou. | Nada mais. O TTW não guarda dados fora do seu repositório. |
| **Fim de uma fase ou do projeto** | Diga ao Claude: "a fase está terminando, vamos fazer a revisão pós-projeto." | Rascunha uma revisão a partir do Registro de pontos de controle, do Path log e do histórico do git. Você escolhe **revisar e encerrar** ou **só revisar**. |

### O que o TTW sabe, e quando

O TTW acompanha as mudanças diárias do projeto pelo diário de bordo e pelo git, não observando seus
arquivos. Para ser preciso:

| Momento | O que é lido | O que **não** é lido |
|---|---|---|
| **A cada prompt** (vigia) | O rumo e o Status em `.watch/WATCH.md`; o número de commits e sessões desde o último ponto de controle. | Seu código, diffs ou outros arquivos. |
| **Ponto de controle** (`/checkwatch`) | A conversa, o `git log` desde o último ponto de controle, os arquivos alterados, os documentos listados em *Evidence scanned*. | Nada fora da pasta do projeto. |
| **Revisão pós-projeto** | O diário de bordo inteiro (Registro de pontos de controle + Path log) e o histórico git de `.watch/WATCH.md`. | Nada fora da pasta do projeto. |

## 4. Comandos em resumo

| Comando | Use para |
|---|---|
| `/checkwatch` | Definir o rumo (primeira vez) · fazer um ponto de controle · fazer uma revisão pós-projeto |
| `/fixwatch` | Mudar de curso de propósito · encerrar uma revisão · reabrir um projeto encerrado |
| `/configwatch` | Ver o estado · definir a frequência dos pontos de controle: inicial `every 3 commits or 2 sessions` (padrão), estável `every 10 commits or 5 sessions`, personalizada ou `off` |

## 5. O que o TTW não fará por você

O TTW não confirma uma mudança, não aceita uma contradição nem encerra o projeto em seu nome, mesmo
que você peça. Ele rascunha o diff, verifica o impacto e reúne as evidências para que cada decisão
leve só uma olhada sua. Isso é proposital: veja
[O que é, e o que não é](README.md#o-que-é-e-o-que-não-é).

## 6. Desligar ou pausar

- Neste terminal: `export TRAVELERSWATCH_DISABLE=1`
- De vez: `/plugin` → travelerswatch → disable (as skills continuam funcionando à mão).
- Menos lembretes de ponto de controle: `/configwatch` → estável ou `off`.

## Próximos passos

[Conceitos](../../docs/concepts.md) · [Exemplo completo](../../examples/pm-walkthrough.md) ·
[Métodos](../../docs/methods.md) · [Como contribuir](CONTRIBUTING.md)
