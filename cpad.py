
#Esse app foi desenvoldo com o objetivo de facilitar as operações financeiras da Plumeria Arte e Design

#IMPORTÇÕES

import PySimpleGUI as sg




#TELA CONVITES

sg.theme('LightBrown9')   # Tema de Cores

img = [      [sg.Image(r'C:\Users\ULTRABOOK\Desktop\projetos\programacao\Cpad\data\logo250x250.png',size=(250,250))]
       ]#Fim da img
calculadora=[[sg.Text('Calculadora Plumeria Arte e Design',font=50,text_color='Black' )],
             [sg.Text('Número de Convites:',size=(19,0)),sg.Input(size=(15,0),key='conv',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Valor da Impressão:',size=(19,0)),sg.Input(size=(15,0),key='imp',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Valor do Envelope:',size=(19,0)),sg.Input(size=(15,0),key='env',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Metros/Pacote:',size=(19,0)),sg.Input(size=(15,0),key='tip',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Valor de Cada Pacote(laço/enfeite):',size=(19,0)),sg.Input(size=(15,0),key='enf',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Valor da caixa de envio:',size=(19,0)),sg.Input(size=(15,0),key='box',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Button('Calcular')]
             ]#Fim da Calculadora

layout1 = [  [sg.Column(calculadora,size=(280,280)),sg.Column(img,size=(250,250))],
             [sg.Text('',font=30,size=(60,10),text_color='Black',background_color='White',key='Resposta' )]
                                   ] #Fim do layout1

img2 = [      [sg.Image(r'C:\Users\ULTRABOOK\Desktop\projetos\programacao\Cpad\data\logo250x250.png',size=(250,250))]
       ]#Fim da img


r_keys = ['1', '2', '3','4','5','6','7'] #Essa lista serve para identificar o Radio selecionado

telataxas= [[sg.Text('Calculadora Plumeria Arte e Design',font=50,text_color='Black' )],
            [sg.Text('Entre com o valor total do serviço',size=(19,0)),sg.Input(size=(15,0),key='totalservico',background_color='White',text_color='Black',do_not_clear= False)],
            [sg.Text('Entre com o valor total de gastos',size=(19,0)),sg.Input(size=(15,0),key='totalgasto',background_color='White',text_color='Black',do_not_clear= False)],
            [sg.Text('Como o cliente pagou?',size=(19,0))],
            [sg.Radio('Dinheiro', "metodo", default=True,key=r_keys[0]),sg.Radio('Boleto', "metodo",key=r_keys[1]),sg.Radio('Débito', "metodo",key=r_keys[2]),sg.Radio('Elo7', "metodo",key=r_keys[3])],
            [sg.Radio('Cartão à vista', "metodo",key=r_keys[4]),sg.Radio('Cartão Parcelado', "metodo",key=r_keys[5])],
            [sg.Radio('MercadoPago(parcelado)', "metodo",key=r_keys[6])],
            [sg.Text('Entre com o valor do Envio',size=(19,0)),sg.Input(size=(15,0),key='totalenvio',background_color='White',text_color='Black',do_not_clear= False)],
            [sg.Button('OK')]
            
           ]#Fim da telataxas

layout2 = [ [sg.Column(telataxas,size=(280,280)),sg.Column(img2,size=(250,250))],
            [sg.Text('',font=30,size=(60,10),text_color='Black',background_color='White',key='Resposta2' )]
            
                                  ] #Fim do layout2

layout = [  [sg.TabGroup([[sg.Tab('Convites',layout1), sg.Tab('Taxas',layout2,)]])],
            [sg.Button('Cancelar')]
            
            
                                   ] #Fim do layout


#JANELA
window = sg.Window('Cpad', layout, icon=(r'C:\Users\ULTRABOOK\Desktop\projetos\programacao\Cpad\data\Grey Circle Leaves Floral Logo (26) (1).ico'))

#Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event in (None,'Cancelar'):   
        break
      
    
    
    
    
    
    
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
            if (Tamanho_total%(tipo*100))== 0:
                QuantidadeDePacotes= Tamanho_total/(tipo*100)
            else:
                QuantidadeDePacotes= (Tamanho_total//(tipo*100))+1
           
            ValorTotalEnfeite= QuantidadeDePacotes*vpenf

            custototal= impressao+envelope+vcaixa+ValorTotalEnfeite
            lucro= custototal*1.2
            valorvenda= custototal+lucro
            valorunid= valorvenda/Qconvites

            
            window['Resposta']('Você deverá cobrar: R$'+str(round(valorunid,2))+ ' por unidade.\n\nCompre '+ str(int(QuantidadeDePacotes))+ ' pacotes de '+ str(tipo)+ ' metros.\n\nVocê gastará um total de: R$'+str(round(custototal,2))+' para confeccionar '+str(Qconvites)+ ' convites.\n\nO cliente pagará um total de: R$'+str(round(valorvenda,2))+ ' pela encomenda.')
            
            window.refresh()

        except:
            sg.popup('Preencha todos os campos com numeros')
            
#Operações tela Taxas
    if event in ('OK'):
        try:
            ValorPago=float(values['totalservico'].replace(",","."))
            Taxa_Dinheiro=0
            Taxa_MPago= ValorPago*0.0499
            Taxa_Boleto= ValorPago*0.0349
            Taxa_PointAV= ValorPago*0.0379
            Taxa_PointPc= ValorPago*0.0436
            Taxa_Debito= ValorPago*0.0199
            Taxa_Elo7= ValorPago*0.12
            Gasto= float(values['totalgasto'].replace(",","."))
            TaxaEnvio= float(values['totalenvio'].replace(",","."))
            TaxaCorreta= int([ key for key in r_keys if values[key]][0]) #Essa variavel recebe o valor da key do Radio

            if TaxaCorreta==1:
                Valor_Recebe= ValorPago-Taxa_Dinheiro
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==2:
                Valor_Recebe= ValorPago-Taxa_Boleto
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==3:
                Valor_Recebe= ValorPago-Taxa_Debito
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==4:
                Valor_Recebe= ValorPago-Taxa_Elo7
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==5:
                Valor_Recebe= ValorPago-Taxa_PointAV
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==6:
                Valor_Recebe= ValorPago-Taxa_PointPc
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            elif TaxaCorreta==7:
                Valor_Recebe= ValorPago-Taxa_MPago
                LucroReal= Valor_Recebe-Gasto-TaxaEnvio

            else:
                print('erro')
            window['Resposta2']('Você Receberá R$:'+str(round(Valor_Recebe,2))+' na sua conta.\n\nSeu lucro será de R$:'+str(round(LucroReal,2))+' já com taxas descontadas.')
        except:
            sg.popup('Preencha todos os campos com numeros')



window.close()
        