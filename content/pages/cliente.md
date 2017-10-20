Title: Cliente




##*Visão do projeto*

Ser diabético de tipo 1 significa ter que medir várias vezes por dia os seus niveis de glicose e injetar uma quantidade de insulina adequada no seu corpo. Mas qualquer um se pode esquecer de medir os seus níveis uma vez por outra, ou ter dificuldade em perceber a quantidade de insulina que deve dar para comer certos alimentos. Além disso familiares, amigos e médicos têm necessidade em saber o estado atual dessa pessoa.

Assim, face às dificuldades existentes no controlo de doentes diabéticos, o nosso grupo pretende desenvolver uma plataforma que acompanhe o doente através de medições de glicose, da atividade física, e da quantidade de hidratos de carbono ingeridos por forma a aconselhar o doente a adoptar o melhor estilo de vida saudável possível, fornecendo uma plataforma acessível e intuitiva de usar quer pelo paciente quer por aqueles que se preocupam com o paciente (médico, familiares, e amigos).

##*Funcionalidades do sistema*
* Histórico de medições dos niveis de glicose e da atividade física que podem ser consultados não só pelo paciente, mas também por amigos, familia e médicos que o acompanhem.

* Ferramenta de calculo de quantidade de glicose a injetar com base na quantidade de hidratos de carbono dos alimentos que o paciente ingerir.

* Calcular as médias de glicemia dos últimos 7,14,30 ou 90 dias ou ainda quantidades médias de hidratos de carbono consumidos e de insulina administrada por dia/refeição/hora.

* Notificações para a realização medições de glicemia a determinadas horas ou ocasiões particulares (por exemplo: 15 minutos após uma hipoglicemia para a verificação de que os valores glicêmicos voltaram a normalidade)

* Aconselhar o utilizador para uma possível mudança de atividade física de forma a acomodar um estilo de vida mais saudável.

* Notificações de consultas, exames ou outros eventos médicos.

##*Prioridades/ Objetivos do projeto*

Este projeto pretende auxiliar todos aqueles que têm diabetes tipo 1 a manter um controlo dos seus níveis de glicose no dia-a-dia mantendo-o a par das medições que deve fazer ao longo do dia através de notificações, ajudando assim o paciente a cumprir as suas responsabilidades médicas.
Um outro ponto fulcral que o projeto deverá atingir será a praticalidade do sistema, uma vez que um doente diabético tem de estar frequentemente a par do seu estado glicêmico é importante que o sistema seja prático o suficiente para que se adapte às diferentes situações do dia a dia do paciente. Por essa mesma razão o foco do lado do cliente da plataforma será um website e uma aplicação móvel disponível para smartphones.

*Produtos semelhantes*

A aplicação móvel Diabetes:m providencia um conjunto de funcionalidades semelhantes àquela que se pretende implementar, no entanto os dados não estão disponíveis através dum serviço RESTFull ao contrario do projeto que pretendemos desenvolver. Por outro lado, dados da atividade física não são medidos nesta app nem existe partilha destes dados com outras entidades de forma conveniente e rápida. 
De qualquer modo, é um bom exemplo do tipo de processamento de dados que se poderá realizar no nosso projeto.

##*Para quem se destina esta aplicação*
A plataforma está destinada a doentes diabéticos tipo 1 de qualquer idade e também para familiares, amigos e médicos interessados em acompanhar o estado do doente. A plataforma irá disponibilizar informações como os níveis de glicose destes, valores tais que irão ser consumidos por clientes interessados no doente em causa. 

Processos
De um modo geral podemos incluir 3 atores no sistema com diferentes papéis, Os pacientes, o sistema em si e os consumidores de informação processada pelo sistema:

| *Ator*  | *Papel no sistema*   |
|---|---|
| Doente Diabético  |  Fornecer informação acerca dos seus níveis de glicose (através do medidor de glicose conectado a um rpi), da sua atividade física, da quantidade de hidratos de carbono consumidos e da quantidade de insulina injetada (através da app móvel). |
| Sistema  |  Processar e fornecer dados aos vários clientes da plataforma. Esses dados sofrer atualizações sempre que nova informação é recebida dos sensores.Devem também, estar disponíveis a partir de um serviço rest para a aplicação móvel e para o website, onde os clientes interessados no doente possam ter acesso a estes dados. |
| Cliente (exemplos: doutor, pai, amigo, doente ..)  | Aceder aos dados fornecidos pelo sistema acerca do estado do doente diabético.  |

##*Riscos e Problemas*
Um compromisso do nosso sistema é que o utilizador apenas receberá informação atualizada na app móvel ou no website apenas se estiver conectado á internet o que poderá ser de algum modo inconveniente para alguns utilizadores (nomeadamente de faixas etárias mais avançadas), limitando um pouco o público alvo do produto. 
Por outro lado, nem todos os utilizadores têm o smartphone ideal para o uso do sistema (um smartphone ideal neste contexto seria um com o gps constantemente ligado e com heart rate sensor embutido). Deste modo, nem todos os utilizadores irão usufruir do track de atividade física que a plataforma providenciará apenas disponível através da informação fornecida por estes sensores.

##*Business processes*
De modo a atingirmos os objetivos estabelecidos anteriormente neste documento, e com base no tempo que nos é disponibilizado para este projeto, as etapas atualmente planeadas de desenvolvimento do projeto sao as seguintes:
1. Definir o que o sistema deverá ser capaz de fazer, em como poderá ser útil para os utilizadores, de modo a que o uso deste sistema acrescente valor no seu dia a dia (fancy stuff) e pensar na organização do sistema e o que será conveniente implementar.

2. Implementar uma api RESTful no raspberry pi capaz de fornecer dados glicêmicos e outro tipo de dados correlacionados com estes valores (atividade física, hidratos de carbono ingeridos etc) a clientes da plataforma.

3. Através da organização do sistema pensado anteriormente implementar com todos os sensores/dispositivos e criar um “esqueleto” que prove que o sistema pensado funciona e que a implementação da plataforma possa avançar, fazendo alterações no esquema da organização do sistema, testando o medidor de glicose com o sensor de raspberry e estabelecer comunicação com o servidor.

4. Implementação inicial do website, e da aplicação móvel, interligando estas componentes com os sensores e o servidor, de modo a que seja possível fazer a leitura dos níveis de glicose do utilizador, e enviar esses dados para os clientes através do servidor(rpi).

5. Implementar notificações e estimativas de injeções de glicose com base em valores de hidratos de carbono ingerido pelo utilizador no sistema.

À medida que o projeto vai avançando, estes planos poderão mudar consoante aquilo que pode ou não ser possível implementar.

##*System wide Requirements - non functional*
A projeto a desenvolver deverá providenciar características como: 
* Confiança e segurança da plataforma ao cliente.
* Escalabilidade do serviço.
* Robustez da aplicação com recuperação de erros (ajudando o utilizador a ultrapassá-los sempre que possível).
* Tempos de resposta de pedidos ao servidor baixos. 
* Portabilidade alta(fornecida pela aplicação móvel). 
* Documentação clara e acessível aos utilizadores da plataforma.
* Alta acessibilidade á plataforma (também fornecida pelo facto de esta estar disponível em formato web e app móvel).
* A UI da plataforma deverá ser intuitiva o suficiente de forma a que qualquer pessoa com ou sem experiência tenha facilidade a usá-la.

##*System wide architecture - deployment*

A plataforma a desenvolver será composto por uma aplicação móvel para android e um web site.
A aplicação móvel beneficiará dos sensores de movimento (giroscópio, gps, etc.) para ler a informação dos níveis de glicose do utilizador e enviar esses dados para o servidor. A versão web servirá apenas para consulta dos dados do utilizador. 
O servidor ficará alojado num Raspberry Pi, que fornecerá informações enviadas pela mobile app ao web site, para futura consulta. Também estará responsável por responder a possíveis pedidos de apis, pelo que este tem que ser sincronizado (no caso de houver vários pedidos ao mesmo tempo ou de a informação ser mudada aquando de um pedido). O servidor será feito usando wildfly, a app será desenvolvida em android e o web site será desenvolvido usando java server faces.

