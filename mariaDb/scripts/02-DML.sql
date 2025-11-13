-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`especialidade`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`especialidade` (`id_especialidade`, `nome`) VALUES (1, 'Otorrinolaringologia');
INSERT INTO `vida_mais_facil`.`especialidade` (`id_especialidade`, `nome`) VALUES (2, 'Endocrinologia');
INSERT INTO `vida_mais_facil`.`especialidade` (`id_especialidade`, `nome`) VALUES (3, 'Ortopedia');
INSERT INTO `vida_mais_facil`.`especialidade` (`id_especialidade`, `nome`) VALUES (4, 'Cuidador');
INSERT INTO `vida_mais_facil`.`especialidade` (`id_especialidade`, `nome`) VALUES (5, 'Cardiologia');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`profissional`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `descricao`, `registro_profissional`) VALUES (1, 'Cristina da Silva Almeida', '85992993270', 1, 'Formada pela Universidade Federal do Ceará em 2010. Tenho 40 anos e atuo com o público idoso há mais de 10 anos', '134256CRM/CE');
INSERT INTO `vida_mais_facil`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `descricao`, `registro_profissional`) VALUES (2, 'Malu Milena Nogueira', '85993362036', 3, 'Especialista em Ortopedia pela Universidade Federal do Ceará em 2011. Desde o início da minha carreira me dedico ao público idoso', '152455CRM/CE');
INSERT INTO `vida_mais_facil`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `descricao`, `registro_profissional`) VALUES (3, 'Luana Rebeca Aline Corte Real', '85987195214', 4, 'Sou cuidadora há mais de 10 anos. Sou muito atenciosa e regrada quanto a rotina dos meus clientes', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`cliente`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`cliente` (`id_cliente`, `nome`, `telefone`, `cpf`, `rua`, `numero`, `email`, `hash_senha`) VALUES (1, 'Eduardo Ribeiro', '85984399162', '52336530368', 'Rua Dois de Setembro', 238, 'eduardo.r@gmail.com', '$2b$12$1Vu7H.AUZzpckBITwK8mguWky/fUJEZ8QwP2l8vQkQoExzWGOJ0ke');
INSERT INTO `vida_mais_facil`.`cliente` (`id_cliente`, `nome`, `telefone`, `cpf`, `rua`, `numero`, `email`, `hash_senha`) VALUES (2, 'Ana Fernanda Yasmin Barbosa', '85981589062', '58950204533', 'Rua Humberto Levita', 370, 'ana_barbosa@saa.com.br', '$2b$12$hHOm9bdVRXSekxC3WxxSGO6g8Kc9I.vUU2p.g23sNE0iaM3WG9ZjS');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`hora`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (1, '07:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (2, '08:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (3, '09:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (4, '10:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (5, '11:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (6, '12:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (7, '13:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (8, '14:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (9, '15:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (10, '16:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (11, '17:00');
INSERT INTO `vida_mais_facil`.`hora` (`id_hora`, `valor`) VALUES (12, '18:00');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`dia`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (1, 'Segunda');
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (2, 'Terça');
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (3, 'Quarta');
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (4, 'Quinta');
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (5, 'Sexta');
INSERT INTO `vida_mais_facil`.`dia` (`id_dia`, `nome`) VALUES (6, 'Sábado');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`agendamento`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`agendamento` (`id_agendamento`, `id_profissional`, `id_cliente`, `id_hora`, `id_dia`, `data`) VALUES (1, 1, 1, 4, 3, '2025-08-20');
INSERT INTO `vida_mais_facil`.`agendamento` (`id_agendamento`, `id_profissional`, `id_cliente`, `id_hora`, `id_dia`, `data`) VALUES (2, 2, 2, 8, 4, '2025-08-21');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`indicador`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`indicador` (`id_indicador`, `tipo`, `valor`, `id_cliente`, `data_registro`, `observacoes`) VALUES (1, 'Pressão', '13/9', 1, DEFAULT, 'Senti um pouco de dor de cabeça antes de medir a pressão');
INSERT INTO `vida_mais_facil`.`indicador` (`id_indicador`, `tipo`, `valor`, `id_cliente`, `data_registro`, `observacoes`) VALUES (2, 'Oxigenação', '96', 1, DEFAULT, NULL);
INSERT INTO `vida_mais_facil`.`indicador` (`id_indicador`, `tipo`, `valor`, `id_cliente`, `data_registro`, `observacoes`) VALUES (3, 'Pressão', '120/80', 2, DEFAULT, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`horario_disponivel`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (1, 1);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (4, 1);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (11, 1);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (2, 2);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (6, 2);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (8, 2);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (1, 3);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (3, 3);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (8, 3);
INSERT INTO `vida_mais_facil`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (9, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_facil`.`dia_disponivel`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_facil`;
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 1);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (3, 1);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (5, 1);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 2);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (2, 2);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (4, 2);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 3);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (2, 3);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (4, 3);
INSERT INTO `vida_mais_facil`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (5, 3);

COMMIT;
