-- 1. Criando do banco de dados
CREATE DATABASE projeto_senac_bigdata;
USE projeto_senac_bigdata;

-- 2. Tabela 1 poços exploratórios até jan/26 (arquivo df_pocos_copy)
CREATE TABLE tabela_pocos (
    id_poco VARCHAR(100) PRIMARY KEY,
    estado VARCHAR(50),
    bacia VARCHAR(100),
    profundidade_m DECIMAL(10,2),
    pre_sal VARCHAR(10),
    fluido_notificacao_descoberta VARCHAR(100)
);

-- 3. Tabela 2 histórico de intervencao nos poços exploratórios (arquivo df_intervencao_pocos_copy)
CREATE TABLE tabela_intervencoes (
    id_intervencao INT AUTO_INCREMENT PRIMARY KEY,
    Nome_poco_anp VARCHAR(100),
    Operador_atual VARCHAR(100),
    Sonda VARCHAR(100),
    Objetivo VARCHAR(150),
    Ambiente VARCHAR(50),
    Data_inicio DATE,
    Data_termino DATE,
    -- Chave Estrangeira para fazer o relacionamento entre as tabelas
    FOREIGN KEY (Nome_poco_anp) REFERENCES tabela_pocos(id_poco)
);