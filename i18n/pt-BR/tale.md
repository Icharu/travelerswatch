<!-- lang-bar -->
[English](../../docs/tale.md) · **Português (Brasil)** · [Español](../es/tale.md) · [繁體中文](../zh-Hant/tale.md) · [简体中文](../zh-Hans/tale.md) · [日本語](../ja/tale.md) · [العربية](../ar/tale.md)

> Traduzido de `docs/tale.md` (v1.2.0, 2026-11-26). Tradução assistida por máquina; a versão em inglês é a canônica.

# O Relógio do Viajante

*Um reconto original, escrito para este projeto.*

Um viajante partiu através de um vale que a neblina havia engolido por inteiro. Não conseguia ver a
estrada, então confiou na única coisa que levava consigo e que não dependia da visão: seu relógio de
bolso. Tinha calculado a jornada em horas: caminhar até o meio-dia, virar para o leste na ponte de
pedra, chegar à cidade ao anoitecer.

No que o relógio chamava de meio-dia, ele parou, apertou a coroa com o indicador direito e leu os
ponteiros. Doze. Virou para o leste. Caminhou. Algum tempo depois, conferiu de novo, e o relógio
marcava dez para o meio-dia. Franziu a testa, achou que tinha lido errado e seguiu andando até o
relógio marcar doze outra vez. Virou para o leste mais uma vez.

Ele não sabia que o relógio estava quebrado. Toda vez que o apertava ao meio-dia, ele voltava dez
minutos. Assim, toda vez que conferia, ele refazia um trecho que já tinha percorrido, certo de que
estava avançando. A neblina escondia a ponte de pedra pela qual ele passava de novo e de novo. Ao
anoitecer estava cansado e nem um pouco mais perto da cidade, e não sabia dizer onde tinha perdido
o dia.

Na muralha da cidade, um vigia guardava seu posto a noite inteira. Os viajantes lá embaixo lhe
gritavam a velha pergunta (*"Guarda, que houve de noite?"*) e ele respondia com o que de fato
conseguia ver: por onde a estrada seguia, quanto faltava para o amanhecer. Ele não adivinhava e não
bajulava. Quando a estrada mudava, ele dizia, e dizia por quê.

O problema do viajante não era a neblina. Neblina é normal; toda estrada longa tem um pouco. O
problema dele era uma referência em que não podia confiar, consultada exatamente no momento em que
mais precisava dela, voltando atrás sem aviso, e ninguém de vigia para lhe dizer que já tinha visto
aquela ponte antes.

Se ele tivesse chegado à muralha naquela noite e gritado a velha pergunta, o vigia teria lhe dito o
que de fato conseguia ver: que a ponte pela qual ele passava era uma só, e que o relógio estava
atrasando. O viajante teria aberto a caixa e consertado o relógio. Não o teria consertado confiando
na palavra do relógio, porque era justamente o relógio que estava errado. E o vigia jamais lhe diria
para consertá-lo se o viajante não estivesse ali para perguntar. Nenhum dos dois teria consertado o
relógio sozinho.

---

## Por que isto é uma skill

Projetos longos feitos com modelos de linguagem se desviam de um jeito muito parecido. Suposições
iniciais se cristalizam, parte da conversa se perde em resumos, e um modelo que pegou o caminho
errado continua voltando a ele, enquanto cada passo isolado parece progresso. O Traveler's Watch dá
ao projeto duas coisas que faltaram ao viajante:

| No conto | Na skill |
|---|---|
| O viajante que pergunta, decide e conserta o relógio | **Você, o gerente de projeto**: você define o rumo e confirma cada mudança |
| Um relógio em que se pode confiar | O **rumo** em `.watch/WATCH.md`: escrito, versionado, sem voltar atrás quando o contexto se perde |
| O relato honesto do vigia | O **hook do vigia**: a cada prompt, uma linha se o trabalho se desviou |
| Virar para o leste de propósito | **`/fixwatch`**: uma mudança de curso escolhida, confirmada pelo gerente de projeto e registrada |
| Conhecer a estrada antes de partir | **`/checkwatch`**: Padrão, Contexto, Restrições, Problema e Ferramentas acordados antes de caminhar |
| Olhar para trás, do portão da cidade | **Revisão pós-projeto**: o que o diário de bordo mostra sobre a jornada inteira |

Nenhum dos lados funciona sozinho. O vigia só pode responder a um viajante que esteja ali para
perguntar, e o viajante não pode confiar em um relógio que ninguém confere. É por isso que o TTW é um
método usado *entre* um modelo e uma pessoa, nunca uma ferramenta que percorre a estrada por você.

A frase *"Guarda, que houve de noite?"* é de Isaías 21:11 (domínio público).
