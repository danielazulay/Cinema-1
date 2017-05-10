import filme
import sala

sessoes = []
ingressosMeia = 0
ingressoInteira = 0

def criar_sessao(cod_sessao, cod_filme, cod_sala, horario):
    sessao = [cod_sessao, cod_fime, cod_sala, horario]
    sessoes.append(sessao)

def recuperar_sessao(cod_sessao):
    for se in sessoes:
        if se[0] == cod_sessao:
            return se
        return False

def verificar_lotacao(cod_sessao):
    for se in sessoes:
        if se[0] == cod_sessao:
            for sa in sala.salas:
                if sa[0] == se[2]:
                    return sa[1]
                else:
                    return None
        else:
            return None
                    
def listar_sessoes():
    return sessoes

def remover_sessao(cod_sessao):
    for se in sessoes:
        if se[0] == cod_sessao:
            sessoes.remove(se)
        else None

def remover_todos_ingressos():
    ingressosMeia = 0
    ingressosInteira = 0
    return ingressosMeia
    return ingressosInteira
    
def iniciar_sessao():
    


        
    
            
    
