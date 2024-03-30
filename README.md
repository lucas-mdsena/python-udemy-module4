# **Hands-on: respondendo perguntas de negócio**
Este repositório contém os materiais utilizados nas aulas do módulo 4, no curso da Udemy.
***

# **Apresentando o nosso problema**

A área de dados, principalmente as funções de analista e cientista de dados, é uma área híbrida entre negócios e TI. É correto dizer que não trabalhamos "com programação", mas a utlizamos em nosso trabalho.

Tão bem quanto as ferramentas, devemos conhecer o negócio onde estamos inseridos. Isso potencializa a nossa capacidade de entrega.

## **Nosso conjunto de dados**
Neste módulo utilizaremos o que aprendemos até para responder perguntas de negócio a partir de uma base de dados sobre a COVID-19, disponível no [Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset?rvi=1).

Este conjunto de dados, disponibilizado pelo governo do México, contém informações gerais sobre condições de saúde e desenvolvimento da doença de pacientes anônimos.

### **Dicionário de dados (traduzido)**

Nas features boleanas, 1 significa "sim" e 2 significa "não"; 97 e 99 representam missing values.
- sexo: 1 p/ mulher e 2 p/ homem.
- idade: idade do pacienteo.
- classificacao: resultado do teste de covid (valores 1-3 - paciente foi diagnosticado em diferentes graus; 4 ou superior - paciente não foi contaminado ou que o teste foi inconclusivo)
- tipo_paciente: tipo de atendimento que o paciente recebe na unidade (1 - retornou para casa; 2 - hospitalizado)
- pneumonia: se o paciente já apresenta, ou não, inflamação de vias aéreas.
- gravidez: se a paciente está grávida.
- diabetes: se o paciente tem diabetes.
- doenca_pulmonar_obstrutiva: se o paciente possui doença pulmonar obstrutiva crônica.
- asthma: se o paciente possui asma.
- imunossuprimido: se o paciente é imunossuprimido.
- hipertensao: se o paciente possui hipertensão.
- cardiovascular: se o paciente tem doenças relacionadas ao coração ou aos vasos sanguíneos.
- doenca_renal_cronica: se o paciente tem doença renal crônica ou não.
- outras_doencas: se o paciente possui outras doenças. 
- obesidade: se o paciente é obeso.
- fumante: se o paciente é fumante.
- usmr: se o paciente foi atendido em unidades de primeiro, segundo ou terceiro grau.
- unidade_medica: tipo de instituição do sistema nacional de saúde que proveu o tratamento
- intubado: se o paciente foi intubado.
- uti: se o paciente deu entrada à UTI.
- data_obito: se morto, indica a data da morte (9999-99-99 - paciente sobreviveu).

## **Perguntas a serem respondidas**

Com base em nosso conjunto de dados, vamos buscar responder às perguntas abaixo utilizando nossos conhecimentos:

**a. Como deu-se a evolução dos óbitos? Foi linear ou tivemos períodos de picos e controles?**

**b. Nos períodos com mais óbitos, podemos isolar os pacientes e ver qual predisposição de saúde  foi mais presente?**

**c. definir pergunta**

**d. definir pergunta**


<br>
<br>

tratamentos a fazer
- verificar se há homens na tabela com indicação de gravidez