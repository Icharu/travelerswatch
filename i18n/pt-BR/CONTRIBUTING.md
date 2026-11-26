<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · **Português (Brasil)** · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> Traduzido de `CONTRIBUTING.md` (v1.2.3, 2026-11-26). Tradução assistida por máquina; a versão em inglês é a canônica.

# Como contribuir com o The Traveler's Watch

Obrigado por ajudar a manter os viajantes no caminho. Contribuições de qualquer tamanho são bem-vindas.

## O que levou a este projeto

O TTW incentiva usuários e contribuidores a entender o que levou a ele antes de alterá-lo. O design
se baseia em literatura publicada entre 2020 e 2026: estudos sobre como modelos de linguagem se
desviam em trabalhos longos, revisões sobre como a IA está mudando a gestão de projetos e um estudo
sobre aumento descontrolado de escopo (*scope creep*).

Koshman e Zubkova (2026) descrevem a pesquisa sobre o funcionamento e o uso da IA no mundo moderno
como **interdisciplinar** por natureza; por isso, contribuições de qualquer área são bem-vindas. Duas
revisões situam o TTW nessa pesquisa:

- **O que a IA já faz bem na gestão de projetos.** Adamantiadou e Tsironis (2025) revisaram 97
  estudos revisados por pares (2011–2024). Segundo o resumo (*abstract*) deles, aprendizado de
  máquina, aprendizado profundo e modelos híbridos mostraram potencial para aprimorar a gestão de
  projetos, sobretudo na **estimativa de custos, na previsão de duração e na avaliação de riscos**. O
  TTW leva isso a sério: automatiza o trabalho repetitivo dentro do rumo.
- **O que ainda não está resolvido.** A mesma revisão, conforme resumida por Koshman e Zubkova
  (2026), relata que modelos de IA se adaptam de forma insuficiente a condições de projeto que mudam,
  têm validação limitada em relação aos dados iniciais e são pouco pesquisados em fases como a revisão
  pós-projeto. O TTW foi construído em torno dessas lacunas: o gerente de projeto mantém a direção, o
  rumo é conferido com as evidências e o diário de bordo sustenta uma revisão pós-projeto.

*Nota sobre as fontes (o que foi lido):* Koshman & Zubkova (2026): texto completo. Adamantiadou &
Tsironis (2025): lido por meio do resumo de Koshman & Zubkova e do resumo (*abstract*) e dos
metadados bibliográficos do seu registro DOI; o texto completo não foi lido. Versões anteriores deste
arquivo atribuíam a revisão de 97 publicações a Koshman & Zubkova; foi um erro de atribuição,
corrigido na v1.2.3.

| Ano | Referência | Por que importa aqui |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | Mudança não autorizada prejudica projetos → toda mudança de curso é confirmada e registrada |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | Modelos usam melhor as bordas de um contexto longo → um rumo curto junto a cada prompt |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | Juízes LLM precisam de critérios explícitos → o Padrão é definido antes de qualquer veredito |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | Modelos pegam caminhos errados e não se recuperam → o rumo é definido logo no início |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | Lembretes reduzem o desvio → o vigia a cada prompt |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | Revisão de 97 estudos: a IA mostra potencial em estimativas, previsões e riscos; adaptabilidade, validação e fases finais não resolvidas → automatizar o trabalho repetitivo, manter um humano no circuito |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | Revisão de 21 publicações (2021–2025) e de ferramentas de IA; resume a revisão de 97 estudos; enquadramento interdisciplinar → humano no circuito, contribuições de qualquer área |

A lista comentada completa, com a consequência de design de cada fonte, está em
[docs/methods.md](../../docs/methods.md) (em inglês). Como o projeto começou e quem decide está no
[GOVERNANCE.md](../../GOVERNANCE.md).

<details>
<summary><b>Referências completas</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- Outras fontes: [docs/methods.md](../../docs/methods.md).

</details>

## Formas de contribuir

| Contribuição | Onde |
|---|---|
| Uma **lente** para uma nova área (ex.: eventos, construção, programas sem fins lucrativos, design de produto) | `skills/checkwatch/references/lenses/` |
| Uma **revisão de tradução** por falante nativo | `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING, tale) |
| Um novo **caso de avaliação** (um prompt e o comportamento esperado) | `skills/<skill>/evals/evals.json` |
| Um **relato de bug** ou ideia | [Issues](https://github.com/Icharu/travelerswatch/issues). Use os modelos. |
| Um **problema de segurança** | **Não** em issues. Veja o [SECURITY.md](../../SECURITY.md). |

## Adicionando uma lente

1. Copie uma lente existente (ex.: `project-management.md`) para `lenses/<area>.md`.
2. Mantenha os mesmos quatro títulos para que a skill use qualquer lente da mesma forma:
   - **How the sections read in this field**: uma tabela que reformula Contexto, Restrições, Problema, Ferramentas
   - **Default criteria**: 4 a 8 critérios *observáveis* (veja `references/standards.md`)
   - **Drift signals**: como é sair do caminho nessa área
   - **Typical tools**
3. Escreva os critérios **com suas próprias palavras**. Não cole texto de normas pagas ou protegidas
   por direitos autorais; cite-as pelo nome e referencie apenas seções.
4. Adicione a lente à lista em `skills/checkwatch/SKILL.md` (passo A1) e à seção *Lenses* do README.
5. Adicione ao menos um caso de avaliação em `skills/checkwatch/evals/evals.json` que use a lente.

## Alterando as skills

- Mantenha cada `SKILL.md` curto e orientado a decisões; coloque detalhes em `references/`.
- Não enfraqueça as regras centrais ([GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)):
  **só o gerente de projeto confirma** uma mudança de curso, um encerramento ou uma contradição
  aceita; **o Path log e o Registro de pontos de controle só aceitam acréscimos**; **nada de sessões
  totalmente automatizadas** para o rumo ([ADR 0004](../../docs/adr/0004-human-in-the-loop.md));
  **nenhum dado guardado** fora do repositório do usuário.
- Use apenas o frontmatter padrão de Agent Skills (`name`, `description`, `license`, `metadata`) para
  que as skills continuem portáveis.
- Explique mudanças de comportamento em um ADR em `docs/adr/` quando elas mudarem uma decisão de design.

## Alterando o hook

- Apenas bash (≥ 3.2, por causa do macOS) e awk; git é opcional. Prefira built-ins do bash a
  processos extras; o diário de bordo é lido em uma única passada de `awk`.
- Ele deve sempre sair com 0, ficar em silêncio sem diário de bordo ou com o rumo `closed`, limitar a
  saída, não fazer chamadas de rede e não gravar nada além de `.watch/.state`.
- **Escreva primeiro o teste que falha** em `tests/watchman.test.sh`, depois faça-o passar, e meça o
  tempo por prompt antes e depois:

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## Alterando o formato do diário de bordo

O hook lê rótulos exatos: `## Status`, `- **Bearing:**` (`confirmed` / `under review …` /
`closed …`), `- **Checkpoint cadence:**` (`every N commits or M sessions` / `off`),
`- **Last checkpoint:** <date> @ <sha>`, `**Boundary notes:**`, linhas de Relations que contêm
"accepted" e o título `## Path log`. `## Checkpoint log` é lido só pelas skills. Altere-os apenas em
conjunto com o hook, o modelo (`skills/checkwatch/assets/WATCH.md`), as skills e os testes.

## Traduções

Os arquivos em inglês na raiz (`README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`) são os canônicos. As
traduções ficam agrupadas por idioma em `i18n/<lang>/`, para que a raiz não fique poluída. Ao mudar
um arquivo em inglês, indique no pull request quais traduções ficaram desatualizadas. Tradutores:
mantenham idênticos a barra de idiomas, os links (relativos a `i18n/<lang>/`, ex.:
`../../docs/methods.md`), os badges, os comandos e os blocos de código de shell (o diálogo do *Exemplo
rápido* pode ser traduzido). Atualizem a nota `Traduzido de` no topo do arquivo. Árabe: mantenham o
texto dentro de `<div dir="rtl">` e os blocos de código fora dele.

**Mantenham o tipo de afirmação.** Toda frase sobre o TTW é uma *intenção de projeto* ("foi projetado
para", "a skill instrui o Claude a"), um *mecanismo* ("o hook faz X", verificável em um arquivo) ou
um *resultado* ("no teste <X>, <número>"). A tradução deve manter o mesmo tipo: confiram o verbo, não
só o substantivo. Mantenham as mesmas fontes e os mesmos números do inglês, deixem citações
autor–ano e títulos originais sem tradução e não acrescentem afirmações nem fontes locais. O espanhol
usa espanhol internacional neutro (*se* impessoal ou *usted*). zh-Hans e zh-Hant são localizados
separadamente, nunca convertidos caractere a caractere.

| English | pt-BR | es | zh-Hans | zh-Hant | ja | ar |
|---|---|---|---|---|---|---|
| is designed to | foi projetado para | está diseñado para | 旨在 | 旨在 | 〜を目的として設計されている | صُمّم لـ |
| the skill instructs Claude to | a skill instrui o Claude a | la skill indica a Claude que | 技能指示 Claude | 技能指示 Claude | スキルは Claude に〜するよう指示する | توجّه المهارةُ Claude إلى |
| tested by evals, not enforced by code | testado por evals, não imposto por código | probado con evals, no impuesto por código | 由评测检验，而非由代码强制 | 由評測檢驗，而非由程式碼強制 | eval で検証されており、コードで強制されてはいない | تُختبَر بالتقييمات ولا تفرضها الشيفرة |
| may / can | pode | puede | 可能 | 可能 | 〜可能性がある | قد |
| according to | segundo | según | 据 | 據 | 〜によれば | وفقًا لـ |
| as summarized by | conforme resumido por | según el resumen de | 据…的综述 | 據…的回顧 | 〜の要約による | كما لخّصه |
| design premise | premissa de projeto | premisa de diseño | 设计前提 | 設計前提 | 設計上の前提 | فرضية التصميم |
| guarantees | *avoid*: foi projetado para | *avoid*: está diseñado para | *avoid*: 旨在 | *avoid*: 旨在 | *avoid*: 〜設計されている | *avoid*: صُمّم لـ |
| always (rules only) | sempre | siempre | 始终 | 始終 | 必ず | دائمًا |
| significant (statistical only) | significativo | significativo | 显著 | 顯著 | 有意 | دالّ إحصائيًا |
| substantial (non-statistical) | substancial | sustancial | 较大 | 較大 | 大きな | كبير |
| evidence | evidência | evidencia | 证据 | 證據 | 根拠 | الأدلة |
| indicates (not "proves") | indica | indica | 表明 | 顯示 | 示唆する | تشير إلى |
| efficient | eficiente | eficiente | 高效 | 高效 | 効率的 | ذو كفاءة |
| effective | eficaz | eficaz | 有效 | 有效 | 効果的 | فعّال |
| drift | desvio | desvío | 漂移 | 偏移 | ずれ | الانحراف |
| bearing | rumo | rumbo | 航向 | 航向 | 針路 | المسار |
| human in the loop | humano no circuito | humano en el circuito | 人在回路中 | 人在迴路中 | ヒューマン・イン・ザ・ループ | الإنسان ضمن الحلقة |

O glossário é assistido por máquina; correções de falantes nativos são bem-vindas.

## Pull requests

1. Faça um fork e crie um branch: `feat/<coisa>`, `fix/<coisa>`, `docs/<coisa>` ou `lens/<area>`.
2. Mantenha cada pull request focado em uma única mudança.
3. Rode `bash tests/watchman.test.sh` e `claude plugin validate .` se tiver o Claude Code.
4. Adicione uma entrada em **Unreleased** no [CHANGELOG.md](../../CHANGELOG.md).
5. Use mensagens no padrão [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`).

Ao contribuir, você concorda que suas contribuições são licenciadas nos mesmos termos do restante do
repositório: [CC BY-NC 4.0](../../LICENSE).
