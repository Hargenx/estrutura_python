## Projeto de Soma de Códigos ASCII

Este é um pequeno projeto em Python que inclui funções para calcular a soma dos códigos ASCII de uma string, com diferentes complexidades de tempo. O projeto consiste em três funções principais:

### 1. `soma_char_codigos_1: O(N)`

- Esta função tem uma complexidade de tempo linear (O(N)), onde N é o comprimento da string. Ela percorre cada caractere da string uma vez e soma o código ASCII de cada caractere.

### 2. `soma_char_codigos_2: O(N^2)`

- Esta função tem uma complexidade de tempo quadrática (O(N^2)). Utiliza dois loops aninhados para percorrer a string e soma o código ASCII de cada caractere em cada iteração.

### 3. `soma_char_codigos_3: O(N^3)`

- Esta função tem uma complexidade de tempo cúbica (O(N^3)). Utiliza três loops aninhados para percorrer a string e soma o código ASCII de cada caractere em cada iteração.

### Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Hargenx/estrutura_python.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd estrutura_python
    ```

3. **Execute o script principal:**

    ```bash
    python main.py
    ```

- Isso imprimirá os resultados das três funções com a string '123456789'.

### Big O Notation (Notação Big O)

A notação Big O (O) é usada para descrever a eficiência de um algoritmo em termos de tempo de execução ou espaço de memória em relação ao tamanho dos dados de entrada. As funções neste projeto são classificadas de acordo com suas complexidades de tempo:

- *O(N)*: Linear. A eficiência do algoritmo aumenta linearmente com o tamanho dos dados.
- *O(N^2)*: Quadrática. A eficiência do algoritmo aumenta quadraticamente com o tamanho dos dados.
- *O(N^3)*: Cúbica. A eficiência do algoritmo aumenta cúbicamente com o tamanho dos dados.

Escolher a complexidade certa para um determinado problema é crucial para garantir a eficiência do código, especialmente ao lidar com grandes conjuntos de dados.

### Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.


**Autor**: Raphael M. S. de Jesus

**Data**: 06/02/2024