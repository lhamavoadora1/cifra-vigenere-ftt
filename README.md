O programa foi feito em python e seu controle é por teminal.

Foi criado uma lista de caracteres que contém todas as letras do alfabeto (algumas com os acentos mais comuns), espaço em branco, ponto, vírgula, etc, e à partir daí que será criado a tabula recta (ou grade) de Vigenère.

Para cada linha da tabela, o alfabeto é inserido com o segundo caractere sendo o primeiro da linha e por assim em diante.

Existem 3 opções no início do programa: Criptografar, Descriptografar e Sair.
Ao escolher Criptografar ou Descriptografar, será necessário escrever uma frase simples e uma chave
O programa devolverá a frase criptografada entre aspas com a chave oferecida (lembrando que os caracteres da frase e chave serão transformados em letras maiúsculas)

Para encontrar o caractere criptografado foi feito uma simples localização na matriz dos índices x e y do alfabeto.
O processo de descriptografia é o mesmo conceito só que o índice a ser descoberto é o x.
