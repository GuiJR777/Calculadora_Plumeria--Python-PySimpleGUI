## # CALCULADORA DE TAXAS PLUMERIA ARTE DESIGN

Projeto Criado com o objetivo de auxiliar nas atividades financeiras da web empresa de design gráfico Plumeria Arte e Design.

Bibliotecas e Tecnologias utilizadas:
- Python 3.81;
- PySimpleGUI;

A ferramenta conta com input de dados em uma interface gráfica para realização de calculos para atividades rotineiras para a empresa (taxas de cartão, valor a ser cobrado por determinado serviço...).

        
    #operações tela Convites
        
        if event in ('Calcular'):
            try:
                Qconvites= int(values['conv'])
                vimp=float(values['imp'].replace(",","."))
                venv=float(values['env'].replace(",","."))
                vpenf=float(values['enf'].replace(",","."))
                vcaixa=float(values['box'].replace(",","."))
                tipo= int(values['tip'])
                
          
                impressao= Qconvites*vimp
                envelope= Qconvites*venv
                Qunid= 70
                Tamanho_total= Qconvites*Qunid

![Layout Cpad](https://i.imgur.com/aop9T1T.png "Layout Cpad")
