---
project_name: Projeto de exemplo
date: 2025-12-25
---

# 1.Visão geral

O projeto reúne as reservas de salas e equipamentos de um centro comunitário numa agenda única. Hoje, os moradores pedem horários por mensagem, e a equipe confere cada solicitação à mão. A plataforma deve mostrar os períodos livres, registrar os pedidos e informar quando a reserva for confirmada.
- A agenda mostra os horários disponíveis e marca os períodos já reservados.
- *Cada morador escolhe* o espaço, a data e o horário antes de enviar o pedido.
- **A equipe acompanha as solicitações** e atualiza o calendário quando aprova ou cancela uma reserva.

# 2.Planejamento das sprints
O projeto será trabalhado em sprints de 15 dias cada uma, totalizando 2 sprints.
## Sprint 1: agenda e disponibilidade
Na primeira sprint, a equipe vai cadastrar os espaços e montar a agenda. O morador poderá escolher uma data, comparar os horários livres e enviar uma solicitação.
## Sprint 2: confirmação e cancelamento
Na segunda sprint, a equipe vai incluir a confirmação e o cancelamento de reservas. O sistema também vai avisar o morador quando a equipe aprovar ou recusar o pedido.

# 3.Usuários previstos:
**Administrador:** cadastra os espaços, define os horários de funcionamento e bloqueia datas de manutenção.
**Usuário:** consulta a agenda e solicita um horário livre. Se outra pessoa reservar o período antes da confirmação, o sistema avisa que ele já está ocupado.

# 4.User stories:

- **ADM01:** Como administrador, quero cadastrar os espaços disponíveis para que os moradores possam consultá-los ao fazer uma reserva.
- **ADM02:** Como administrador, quero definir o horário de funcionamento e bloquear datas de manutenção para que o sistema não ofereça períodos indisponíveis.
- **ADM03:** Como administrador, quero aprovar ou recusar solicitações de reserva para manter a agenda atualizada e informar o resultado ao morador.
- **ADM04:** Como administrador, quero cancelar uma reserva confirmada e liberar o horário na agenda quando necessário.
- **USR01:** Como usuário, quero consultar a disponibilidade dos espaços por data para escolher um horário livre.
- **USR02:** Como usuário, quero solicitar a reserva de um horário disponível e receber o resultado da solicitação.
