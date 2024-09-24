import json
from os import path






class Route:
    def __init__(self, rid):                    
        self.id = rid
        self.stops = []
        self.departure_time_utc = None
        self.zone_sequence = []                 # unico que nao está no json "route_data"

    def get_stop_with_id(self, stop_id):	    # Duvidas
        for stop in self.stops:
            if stop.id == stop_id:
                return stop
        

class Stop:
    def __init__(self, id, zone_id, route_id, stop_type):
        self.id = id
        self.zone_id = zone_id
        self.packages = []
        self.route_id = route_id
        self.stop_type = stop_type


class Package:
    def __init__(self, id, route_id, start_time_utc, end_time_utc, planned_service_time_seconds):        # Averiguar a falta ou não das "stops"
        self.id = id
        self.packages = []
        self.route_id = route_id
        self.start_time_utc = start_time_utc
        self.end_time_utc = end_time_utc
        self.planned_service_time_seconds = planned_service_time_seconds


'''
class Zone:
    def __init__(self):
        self.id


class ZoneSequence:
    def __init__(self, rid):
        self.zones_array = []
        self.route_id = rid
'''
#estas classes estao comentadas porque eram so arrays simples nao valia a pena



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        


def load_district_sequences():
    with open('C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/district_sequences.json') as json_file:
        #print(f'Loading district_sequences.json...')
        array_district_sequence = json.load(json_file)
        #print(f'Done.')

    for rtkey in array_district_sequence.keys():
        rid = rtkey
        rtObj = Route(rid)                                # 
        for zid in array_district_sequence[rtkey]["ZoneID_Sequence"]:	
            rtObj.zone_sequence.append(zid)               # 

        routes[rtkey] = rtObj
    



def load_route_data():
    with open("C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/route_data.json") as json_file:
        #print(f'Loading route_data.json...')
        array_route = json.load(json_file)
        #print(f'Done.')

    for rtkey in array_route.keys():
        rid = rtkey
        rtObj = routes[rid]
        rtObj.departure_time_utc = array_route[rid]["departure_time_utc"]
 
        for stop_name in array_route[rtkey]["stops"].keys():	
            stop_zone_id = array_route[rtkey]["stops"][stop_name]["zone_id"]
            stop_type = array_route[rtkey]["stops"][stop_name]["type"]
            stop = Stop(stop_name, stop_zone_id, rid, stop_type)
            rtObj.stops.append(stop)

    #print(array_route)
           


def load_package_data():
    with open("C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/package_data.json") as json_file:
        #print(f'Loading route_data.json...')
        array_package = json.load(json_file)
        #print(f'Done.')

    for rtkey in array_package.keys():
        rid = rtkey
        rtObj = routes[rid]                         # O que é o "rtObj"?
 
        for stop_name in array_package[rtkey].keys():	                                             # Para cada paragem em todas as paragens   (Corre todas as paragens uma a uma no array das paragens da rota "rtkey")
            for package_id in array_package[rtkey][stop_name]:                                       # Para cada package em cada paragem    (cada package em AD,  cada package em FE ...)
                package_data = array_package[rtkey][stop_name][package_id]
                start_time = package_data["time_window"]["start_time_utc"]
                end_time = package_data["time_window"]["end_time_utc"]
                planned_time = package_data["planned_service_time_seconds"]
                package = Package(package_id, rid, start_time, end_time, planned_time)               # Duvida. Está a interligar com a Class "Package"?
                stop = rtObj.get_stop_with_id(stop_name)
                stop.packages.append(package)

    #print(array_package["RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77"])
    




if __name__ == '__main__':

    #lista_x={} 
    todas_as_sequencias=dict()
    routes = {}

    """
    time_info = TravelTimesData()	# Instancia e Inicializa classe TravelTimesData
    filename = 'data/travel_times.json'
    filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), filename)
    time_info.load_json(filepath)	# Carrega .json
    time_info.parse_and_insert_raw_data()	# Faz parsing dos dados carregados do json para as estruturas das classes
    p1 = 'VE'
    p2 = 'AD'
    route_idx = 0
    print(f"time r[{route_idx}] - [{p1}][{p2}]: {time_info.get_time_from(route_idx, p1, p2)}")	# Procura directamente o tempo de viagem entre p1 e p2
    """



    load_district_sequences() #fills the routes with the zone sequence
    load_route_data() #fills the routes with the stops
    load_package_data() #fills the stops with the package data

    
    lol = []
    stops_zones=[]

    for key in routes.keys(): #percorre as rotas
        #print("Route ID:")
        #print(key) 
        #print("Route departure_time_utc")
        #print(routes[key].departure_time_utc)
        #print("Zone sequence:")
        #print(routes[key].zone_sequence)
        #print("Stops")
        #print(routes[key].stops[0].id) 
        #routes[key].stops[0].zone_id -> para ir buscar a zona da stop, deve dar-te jeito
        #print("First package of the first stop")
        #print(routes[key].stops[0].packages[0].planned_service_time_seconds)
        #print("First package of the first stop end time")
        #print(routes[key].stops[0].packages[0].end_time_utc)

        #print("---------------------------------------")


        for zone_id in routes[key].zone_sequence:                       # Como tem o break, o ciclo corre todas as "zones" (distritos) da rota 1
            for stop in routes[key].stops:                              # Para cada stop em todas as stops da rota 1
                if stop.zone_id == zone_id:                             # 
                        #print(zone_id)
                        #print(stop.id)
                    
                    lol.append(stop.id)
                #print(f"distito: {zone_id}   stops: {stop.id}")

        lol.clear()
        break


                  

    with open('C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/travel_times.json') as json_file:    # Importar o json "travel_times" para pyhton
            #print(f'Loading Json...')
            array_travel_times = json.load(json_file)  
            #print(f'Done.')

  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                        # CÁLCULOS E FERRAMENTAS AUXILIARES



                                                              #  CRIAÇÃO DE DUAS LISTAS: UMA COM O ID DE CADA ROUTE E OUTRA COM LISTAS DAS STOPS DE CADA ROTA (LISTAS DENTRO DE LISTAS)


    with open('C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/package_data.json') as json_file:    # Importar o json "package_data" para pyhton
         array_package = json.load(json_file)  


    all_routes=[]

    for rota in routes.keys():
        all_routes.append(rota)
    #print(all_routes)                                      # Lista com as rotas todas ['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77', ... , 'RouteID_00747543-3f2f-47ae-a2f2-91b30ce207ab']
  
    
    stops_routes=[]
    temporaria=[]

    for rota in all_routes:                                                                 # Ciclo útil para depois percorrer todas as rotas
        for paragem in routes[rota].stops:
            temporaria.append(paragem.id)
        stops_routes.append(temporaria[:])
        temporaria.clear()
                

    #print(stops_routes)                                                           
        




 # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
                                                        #  CRIAÇÃO DE DUAS LISTAS: ID DOS PONTOS INICIAS DE CADA ROTA E POSIÇÕES DOS PONTOS INICIAIS DE CADA ROTA

       
    
    pos_pontos_ini=[]

    pontos_iniciais = []            

    for p in range(0, len(all_routes)):
        for stop in routes[all_routes[p]].stops:
            if stop.stop_type == "Station":
                pontos_iniciais.append(stop.id)                                  
    
    #print(pontos_iniciais)                                                  # pontos_iniciais = [VE, UX, RD, LR, SE, WR, TP, EX, ZP, SP, QO, BD, RT]

    for pos_rotas in range(0, len(stops_routes)):                                                   # 0 a 12 (rotas)
        for pos_rota_x in range(0, len(stops_routes[pos_rotas])):                                   # 0 a len de cada rota individual (ciclo)
            if pontos_iniciais[pos_rotas] == stops_routes[pos_rotas][pos_rota_x]:
                pos_pontos_ini.append(pos_rota_x)
    #print(pos_pontos_ini)
            

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    # CRIAÇÃO DE UMA LISTA DAS AS ROTAS COM STOPS SEM DISTRITO (NaN)
    
    with open('C:/Users/nunog/Desktop/School/ISEP/1º ano/1º semestre/Projeto 1/Instances/route_data.json') as json_file:    # Importar o json "travel_times" para pyhton
            #print(f'Loading Json...')
            array_route_data = json.load(json_file)  
            #print(f'Done.')


    lista_rotas_com_stops_nan=[]

    for pos_rota_x in range(0, len(all_routes)):
        for paragem in range(0, len(stops_routes[pos_rota_x])):
            if array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][paragem]]["zone_id"] == "NaN" and array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][paragem]]["type"] == "Dropoff":
                if pos_rota_x not in lista_rotas_com_stops_nan:
                    lista_rotas_com_stops_nan.append(pos_rota_x)                                # [5,6,7,12]
    #print(lista_rotas_com_stops_nan)                                                   

           


  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            # MODELO


    sequencia_final_rota = []                           # Sequencia final das stops da rota 
    Districts_route=[]                            # Lista da sequencia dos distritos da rota 
    stops_por_cada_distrito = []                   # Lista temporária que mostra as stops de cada distrito individualmente, um por um (por causa do clear)

    tempos_temporarios=[]                  # Lista temporária dos tempos entre o ponto de partida ou stop atual e as restantes stops do distrito. Útil para seleção dos postos de entrega e dos tempos entre postos com menor tempo (utilizado para a seleção do menor_posto e menor_distancia)
    tempos_totais_entre_stops_e_ponto_de_partida=[]                       # Lista de todos os tempos entre stops  

    menor_posto=""                        
    menor_distancia=0

    lista_distritos_atribuidos=[]
    nan_distritos=[]

                                                        # CRIAÇÃO DE UMA LISTA COM TODAS AS STOPS COM "NaN" (SEM DISTRITO) DA ROTA

    lista_stops_nan=[]                                      # Lista com todas as stops com "NaN" (Sem distrito) da rota
    tempos_entre_nan=[]                            


    for pos_rota_x in range(0, len(all_routes)):

        p1=pontos_iniciais[pos_rota_x]

        sequencia_final_rota.append(p1)            # Adicionar á sequência o posto/posição de partida         NOTA:  CRIAR LISTA COM TODOS OS PONTOS DE PARTIDA
        stops_por_cada_distrito.append(p1)





        if pos_rota_x in lista_rotas_com_stops_nan:
            for paragem in range(0, len(stops_routes[pos_rota_x])):
                #print(paragem.id)
                if array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][paragem]]["zone_id"] == "NaN" and array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][paragem]]["type"] == "Dropoff":
                    lista_stops_nan.append(stops_routes[pos_rota_x][paragem])

            
                                                                    #  LISTA TEMPORARIA COM TODOS OS TEMPOS ENTRE A PARAGEM NAN (SEM DISTRITO) E AS RESTANTES EXCLUINDO A PARAGEM NAN 
  

                                                                    #  E LISTA COM O DITRITO ATRIBUIDO A CADA PARAGEM NAN 
            menor_distancia_nan=0
            distrito_paragem_nan=""
            


            for pos_nan in range(0, len(lista_stops_nan)):
                for paragem in range(0, len(stops_routes[pos_rota_x])):
                        #print(paragem)
                        if stops_routes[pos_rota_x][paragem] != lista_stops_nan[pos_nan]:
                            tempos_entre_nan.append(array_travel_times[all_routes[pos_rota_x]][lista_stops_nan[pos_nan]][stops_routes[pos_rota_x][paragem]])
                            #print(tempos_temporarios)
                        #for tempo in 
                #print(tempos_entre_nan)
                        menor_distancia_nan=tempos_entre_nan[0]                 # Condição inicial da variável "menor_distancia_nan"
                        for j in range(0,len(tempos_entre_nan)):            # Ciclo para seleção da menor distância entre o primeiro posto e os restantes
                            if tempos_entre_nan[j]<=menor_distancia_nan:
                                menor_distancia_nan=tempos_entre_nan[j]
                                if array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][j]]["zone_id"] != "NaN":
                                    distrito_paragem_nan=array_route_data[all_routes[pos_rota_x]]["stops"][stops_routes[pos_rota_x][j]]["zone_id"]
                                    nan_distritos.append(distrito_paragem_nan)    
                #print(distrito_paragem_nan)
                lista_distritos_atribuidos.append(distrito_paragem_nan)
                tempos_entre_nan.clear()
            #print(distrito_paragem_nan)
                
            #print(distrito_paragem_nan)
            #print(lista_distritos_atribuidos)



        for zona in routes[all_routes[pos_rota_x]].zone_sequence:
            if zona not in "nan" and zona not in Districts_route:                 # Existem zones repetidas (desconsiderou-se as repetidas e as que não tinham zone.id)
                Districts_route.append(zona)                                     # Lista com apenas a sequencia dos distritos da rota 1
        #print(f"Lista da sequencia dos distritos da rota 1: {Districts_route}")

        for zone_id in Districts_route:
            if pos_rota_x in lista_rotas_com_stops_nan:
                for pos_distrito in range(0,len(lista_distritos_atribuidos)):
                    if lista_distritos_atribuidos[pos_distrito] == zone_id:
                        stops_por_cada_distrito.append(lista_stops_nan[pos_distrito])



        for zone_id in Districts_route:                  # Corre cada distrito da sequencia de distritos da rota 1 (por causa do break)
            for stop in routes[all_routes[pos_rota_x]].stops:                                     # Para cada stop do conjunto de stops da rota 1
                if stop.zone_id == zone_id:
                    #print(stop.id)                              # Se o distrito dessa stop for igual ao distrito a observar na linha 274
                    stops_por_cada_distrito.append(stop.id)
            #print(zone_id)
                

                
            while len(stops_por_cada_distrito)>1:                 # Como irão ser removidos postos da lista "zone_stops", o ciclo irá correr enquanto houver mais que um posto
                for c in range(1,len(stops_por_cada_distrito)):            # Ciclo que irá proporcionar o "append" dos tempos entre o posto inicial e os restantes
                    tempos_temporarios.append(array_travel_times[all_routes[pos_rota_x]][stops_por_cada_distrito[0]][stops_por_cada_distrito[c]])                 # "Append" de cada tempo para a lista "tempos_temporários"
                    menor_distancia=tempos_temporarios[0]                 # Condição inicial da variável "menor_distancia"
                    for i in range(0,len(tempos_temporarios)):            # Ciclo para seleção da menor distância entre o primeiro posto e os restantes
                        if tempos_temporarios[i]<=menor_distancia:
                            menor_distancia=tempos_temporarios[i]
                            menor_posto=stops_por_cada_distrito[i+1]
                sequencia_final_rota.append(menor_posto)
                tempos_totais_entre_stops_e_ponto_de_partida.append(menor_distancia)
                #print(menor_distancia)
                #print(menor_posto)


                stops_por_cada_distrito.remove(menor_posto)                            # A lógica presente centra-se em, no fim de selecionar a menor distância e respetivo posto, remover o posto inicial, pois já não é mais o ponto de partida,
                stops_por_cada_distrito.remove(stops_por_cada_distrito[0])                      # e mover o posto com menor distância para a primeira posição.
                stops_por_cada_distrito.insert(0,menor_posto)                          # Como as listas são imutáveis, o processo é remover o "menor_posto" e inseri-lo no inicio para poder-se novamente selecionar a próxima distância mínima

                tempos_temporarios.clear()                                    # Tornar a lista vazia de forma a poder-se inserir novamente novas distâncias a avaliar para progredir com a sequência
        

            #print(f"Distrito {zone_id}: {stops_por_cada_distrito}")            
            stops_por_cada_distrito.clear()
            stops_por_cada_distrito.append(menor_posto)                             # Este "append" serve para, no distrito seguinte, as distâncias serem procuradas a partir da última stop do distrito anterior

        tempos_totais_entre_stops_e_ponto_de_partida.append(array_travel_times[all_routes[pos_rota_x]][sequencia_final_rota[len(sequencia_final_rota)-1]][sequencia_final_rota[0]]) 
        sequencia_final_rota.append(p1)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                              
                                                                        # OBTENÇÃO DA LISTA COM TODOS OS TEMPOS PARA O KPI - TOTAL TRAVEL TIME

            # Lógica: Criar lista apenas com o tempo entre stops (remover tempo do ponto de partida até à 1º stop, e remover tempo da última stop ao ponto de partida). Criar nova lista com as somas: dos tempos entre stops (lista anterior) e com a lista dos tempos em cada stop (sum_planned_times_per_stop). Por fim adicionar a esta última lista o tempo do ponto de partida até à 1º stop, e adicionar tempo da última stop ao ponto de partida 
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            
                                                        #  CRIAÇÃO DE UMA LISTA DOS TEMPOS DE ENTRE STOP (APENAS) 


                   # Tempos totais por stop, tempo do ponto de partida até à 1ª stop e tempo da última stop ao ponto de partida

        tempo_total_entre_stops=[]

        tempo_total_entre_stops=tempos_totais_entre_stops_e_ponto_de_partida[:]
        tempo_total_entre_stops.pop(0)
        tempo_total_entre_stops.pop(len(tempo_total_entre_stops)-1)
        
        #print(tempo_total_entre_stops)               # Como seria de esperar, existe menos um tempo entre stops (117 na rota 1) em comparação com o tempo em cada stop (118 na rota 1). Somaram-se os tempos entre cada lista e adicionou-se o tempo na última stop
        #print(len(tempo_total_entre_stops))

        
   
            
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
                                                                            #  CRIAÇÃO DE UMA LISTA COM LISTAS DE TODOS OS PACKAGES ID DE CADA ROTA
        encomendas=[]
        all_packages=[]

    
        
        for c in range(0,len(routes[all_routes[pos_rota_x]].stops)):
                for pack in routes[all_routes[pos_rota_x]].stops[c].packages:
                    encomendas.append(pack.id)
                    #print(f"Stop: {paragem.id}  Packages: {pack.id}")
                #print(f"Stop: {routes[all_routes[pos_rota_x]].stops[c].id} Packs: {encomendas}")

                all_packages.append(encomendas[:])
                encomendas.clear()

        #print(all_packages)                                    # [['PackageID_9d7fdd03-f2cf-4c6f-9128-028258fc09ea', 'PackageID_5541e679-b7bd-4992-b288-e862f6c84ae7', 'PackageID_84d0295b-1adb-4a33-a65e-f7d6247c7a07'], ['PackageID_15c6a204-ec5f-4ced-9c3d-472316cc7759']   

        #print(len(all_packages))                               # Verificacão do número de stops 

        
       

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
                                                                            #  CRIAÇÃO DE UMA LISTA COM O NÚMERO DE PACKAGES P0R STOP  
        number_packages_per_stop=[]

        for i in range(0,len(all_packages)):
            number_packages_per_stop.append(len(all_packages[i]))

        number_packages_per_stop.pop(pos_pontos_ini[pos_rota_x])                   # Elimina o valor do ponto de partida               

        #print(number_packages_per_stop)                                          # [3, 1, 2, 1, 4, 3, 2, 3, 2, 1, 2, 2, ... ]

        #print(len(number_packages_per_stop))                                     # Verificação do número de stops         276

        

        #time_per_package=[]

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
                                                                            #  CRIAÇÃO DE UMA LISTA COM OS TEMPOS DO 1º PACKAGE DE CADA STOP (SEM REPETIÇÃO DE TEMPOS)
    
        lista_sem_repeticoes=[]


        for c in range(0,len(routes[all_routes[pos_rota_x]].stops)):
            if c != pos_pontos_ini[pos_rota_x]:
                lista_sem_repeticoes.append(routes[all_routes[pos_rota_x]].stops[c].packages[0].planned_service_time_seconds)

        #print(lista_sem_repeticoes)

        #print(len(lista_sem_repeticoes))
                
        #print(routes[all_routes[pos_rota_x]].stops[103].packages[0].planned_service_time_seconds)                 # A posição 103 dá erro oor causa do VE (ponto inicial) - não tem planned time

    
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
                                                                            #  CRIAÇÃO DE UMA LISTA COM OS TEMPOS DE SERVIÇO DE CADA ROTA
        multi_planned_times_per_stop=[]

        for c in range(0, len(number_packages_per_stop)):
            multi_planned_times_per_stop.append(number_packages_per_stop[c]*lista_sem_repeticoes[c])
        
        #print(multi_planned_times_per_stop)
        #print(len(multi_planned_times_per_stop))


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
                                                                            #  CRIAÇÃO DE UMA LISTA COM OS TEMPOS TOTAIS DE E PARA CADA STOP POR POSIÇÃO DE CADA ROTA
    
        kpi_ttt=[] 


        kpi_ttt.append(tempos_totais_entre_stops_e_ponto_de_partida[0])

        for c in range (0,len(tempo_total_entre_stops)):
            kpi_ttt.append(tempo_total_entre_stops[c]+multi_planned_times_per_stop[c+1])                             # c+1 funciona para a lista "multi_planned ..." porque tem mais uma posição que a lista "tempo_total_entre_stops"
                                                                                                                  # Isto acontece pq o tempo entre paragens é sempre 1 unidade inferior ao número de paragens (exemplo: 3 paragens têm e tempos de viagem entre elas)
        kpi_ttt.insert(1,multi_planned_times_per_stop[0])                                                                 # Tempo de serviço da primeira stop (o tempo se viagem já foi contabilizado na partida)
        kpi_ttt.append(tempos_totais_entre_stops_e_ponto_de_partida[len(tempos_totais_entre_stops_e_ponto_de_partida)-1])        # Acrescentar o tempo da última stop ao ponto de partida

        #print(kpi_ttt)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                            #  CRIAÇÃO DE UMA LISTA COM O TEMPO TOTAL DE CADA ROTA (TOTAL TRAVEL TIME)

        soma_tempos_stops=0
        for tempo in kpi_ttt:                                                               # OBTENÇÃO DA SOMA DOS TEMPOS TOTAIS (KPI - TOTAL TRAVEL TIME)
            soma_tempos_stops=soma_tempos_stops+tempo
        #print(f"Tempos entre stops (segundos): {soma_tempos_stops}")
        #print(f"Tempos entre stops (horas): {soma_tempos_stops/60/60}")



    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #print("-=-"*85)
        print("-=-"*85)

        print(f"Sequencia rota {[pos_rota_x]}: {sequencia_final_rota}")
        #print("---"*85)
        print(f"Total Travel Time (segundos): {soma_tempos_stops:.2f}")
        print(f"Total Travel Time (horas): {soma_tempos_stops/60/60:.2f}")

        
        
        
        #lista_x[pos_rota_x]=sequencia_final_rota

        todas_as_sequencias[f"Rota {pos_rota_x}"] = sequencia_final_rota.copy()






        def save_output_json( node_seq, ttt_s, ttt_h):	# Função que permite escrever um ficheiro JSON na directoria onde está a correr o código com os resultados.
		# Data to be written
            sequence_json = {
#            "total travel time (seconds)": ttt_s,	
#            "total travel time (hours)": ttt_h,		
			"Sequências": node_seq

		}
 
            with open(f"result_.json", "w") as outfile:
                json.dump(sequence_json, outfile)

        
       
    
        
        
        
        
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        sequencia_final_rota.clear()
        Districts_route.clear()
        stops_por_cada_distrito.clear()
        tempos_temporarios.clear()
        tempos_totais_entre_stops_e_ponto_de_partida.clear()
        menor_posto=""
        menor_distancia=0
        kpi_ttt.clear()
        tempo_total_entre_stops.clear()
        multi_planned_times_per_stop.clear()
        soma_tempos_stops=0
        encomendas.clear()
        all_packages.clear()
        number_packages_per_stop.clear()


        lista_stops_nan.clear()
        tempos_entre_nan.clear()
        menor_distancia_nan=0
        distrito_paragem_nan=""
        lista_distritos_atribuidos.clear()
        nan_distritos.clear()

#print(todas_as_sequencias)

save_output_json(todas_as_sequencias, soma_tempos_stops, (soma_tempos_stops/60/60))