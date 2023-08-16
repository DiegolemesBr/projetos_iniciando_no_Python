class programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self._like = 0
        self.ano = ano
    @property 
    def like(self):
        return self._like
   
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,Nome_novo):
        self._nome = Nome_novo
        
    def dar_like(self):
        self._like += 1 
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._like} Likes' 
    
class filme(programa):
    def __init__(self,nome,ano,duração):
        super().__init__(nome,ano)
        self.duração = duração
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duração} min - {self._like} Likes'    
   

class serie(programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._like} Likes'
class Playlist:
    def __init__(self,nome,conteudo):
        self.nome = nome
        self._conteudo = conteudo
    def __getitem__(self,item):
        return self._conteudo[item]
    def __len__(self):
        return len(self._conteudo)
    @property
    def listagem(self):
        return self._conteudo
    @property 
    def tamanho(self):
        return len(self._conteudo)    
    

vingadores = filme("vingadores guerra infinita",2018,"179")
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
#print(f'nome:{vingadores.nome} - ano: {vingadores.ano} - duração {vingadores.duração}-likes {vingadores.like}')
lucifer = serie("lucifer",2016,6)
lucifer.dar_like()
lucifer.dar_like()
lucifer.dar_like()
lucifer.dar_like()
lucifer.nome = 'lucife'
#print(f'nome:{lucifer.nome} - ano: {lucifer.ano} - temporadas {lucifer.temporadas}-likes {lucifer.like}')
vingadores2 = filme("vingadores ultimato",2019,"182")
vingadores2.dar_like()
vingadores2.dar_like()
vingadores2.dar_like()
BBT = serie("big bang: ateoria ",2007,12)
BBT.dar_like()
BBT.dar_like()
BBT.dar_like()
BBT.dar_like()
ADF = filme("O aprendiz de feiticeiro",2010,"109")
ADF.dar_like()
ADF.dar_like()
ADF.dar_like()
Filmes_e_series = [vingadores,vingadores2 ,lucifer, BBT, ADF ]
Pra_ver_no_final_de_semana = Playlist("O que você deve ver no seu fim de semana",Filmes_e_series)
print(f"Numero de produções dentro da playlist: {len(Pra_ver_no_final_de_semana)}")
print(f' O filme O aprendiz de feiticeiro esta presente na playlist? {ADF in Pra_ver_no_final_de_semana}')
for programa in Pra_ver_no_final_de_semana:
    print(programa)
    