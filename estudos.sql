


CREATE DATABASE BD_Predio;
GO

USE BD_Predio;
GO


CREATE TABLE Predios (
    ID_Predio INT PRIMARY KEY IDENTITY(1,1),
    Nome_Predio VARCHAR(100) NOT NULL,
    Endereco VARCHAR(200) NOT NULL,
    CEP VARCHAR(10),
    Quantidade_Andares INT,
    Quantidade_Apartamentos INT,
    Data_Construcao DATE
);


CREATE TABLE Apartamentos (
    ID_Apartamento INT PRIMARY KEY IDENTITY(1,1),
    ID_Predio INT NOT NULL,
    Numero_Apartamento VARCHAR(20) NOT NULL,
    Andar INT,
    Quantidade_Quartos INT,
    Area_Util DECIMAL(8,2),
    Valor_IPTU DECIMAL(10,2),
    FOREIGN KEY (ID_Predio) REFERENCES Predios(ID_Predio)
);


CREATE TABLE Moradores (
    ID_Morador INT PRIMARY KEY IDENTITY(1,1),
    ID_Apartamento INT NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    CPF VARCHAR(14) UNIQUE,
    Data_Nascimento DATE,
    Telefone VARCHAR(15),
    Email VARCHAR(100),
    Data_Mudanca DATE,
    Ativo BIT DEFAULT 1,
    FOREIGN KEY (ID_Apartamento) REFERENCES Apartamentos(ID_Apartamento)
);


CREATE TABLE Dependentes (
    ID_Dependente INT PRIMARY KEY IDENTITY(1,1),
    ID_Morador INT NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Relacao VARCHAR(50),
    Data_Nascimento DATE,
    FOREIGN KEY (ID_Morador) REFERENCES Moradores(ID_Morador)
);


INSERT INTO Predios (Nome_Predio, Endereco, CEP, Quantidade_Andares, Quantidade_Apartamentos, Data_Construcao)
VALUES ('Condomínio Residencial Alegria', 'Av. Principal, 500', '01234-567', 10, 40, '2015-06-15');

INSERT INTO Apartamentos (ID_Predio, Numero_Apartamento, Andar, Quantidade_Quartos, Area_Util, Valor_IPTU)
VALUES 
(1, '101', 1, 3, 85.50, 500.00),
(1, '102', 1, 2, 65.00, 400.00),
(1, '201', 2, 3, 85.50, 500.00),
(1, '202', 2, 2, 65.00, 400.00);

INSERT INTO Moradores (ID_Apartamento, Nome, CPF, Data_Nascimento, Telefone, Email, Data_Mudanca, Ativo)
VALUES 
(1, 'João Silva', '123.456.789-00', '1980-03-15', '11987654321', 'joao@email.com', '2023-01-10', 1),
(1, 'Maria Silva', '123.456.789-01', '1982-07-22', '11987654322', 'maria@email.com', '2023-01-10', 1),
(2, 'Pedro Santos', '111.222.333-44', '1975-11-30', '11988884444', 'pedro@email.com', '2022-05-20', 1),
(3, 'Ana Costa', '222.333.444-55', '1990-09-12', '11989995555', 'ana@email.com', '2024-02-15', 1);

INSERT INTO Dependentes (ID_Morador, Nome, Relacao, Data_Nascimento)
VALUES 
(1, 'Lucas Silva', 'Filho', '2010-06-20'),
(1, 'Sofia Silva', 'Filha', '2012-09-10'),
(3, 'Carlos Santos', 'Filho', '2015-01-05');
