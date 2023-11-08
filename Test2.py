import streamlit as st 

#titulo da página que vai aparecer nos buscadores e no endereço do site.
st.set_page_config(page_title="Professor Téo")


# Criando uma siderbar para colocar os containers dentro
st.sidebar.selectbox("Disciplinas", ("Esportes Técnicos Combinatórios", "Didática e Formação" ))

# criando conteiner para a primeira disciplina que será apresentada no site

with st.container():

    # Titulo do primeiro tópico,container da página. 
    st.title(":red[DISCIPLINA DE ESPORTES TÉCNICO COMBINATÓRIO]")

    #titulo do primeiro assunto da página, conteúdo
    st.header("Conteúdos ")
   
    # inserindo os primeiros conteúdos,via link que estará no google drive, criando um link de acesso. 
    st.write("[- Introdução, Ginásticas, Saltos Ornamentais](https://docs.google.com/presentation/d/1L55dMwKyjFCIQ5WQwrA4jjIVN30YHrM7RXztzPfcUzY/edit?usp=sharing)")
    st.write("[- Nado sincronizado](https://docs.google.com/presentation/d/1cushzlLxXwlBVTq91Ck4jsimtohoa5S0c8uMAkaEqKk/edit?usp=sharing) ")
    st.write("[- Slackline](https://docs.google.com/presentation/d/1Iovhk7o42KUbVLEoLtWpMjM3Luw_T9P71Whczwp0a_I/edit?usp=sharing)")
    st.write("[- Skate](https://docs.google.com/document/d/1lP0iJU1jivs2rjSaUjcZqaSa8of2-S1iZkt-84d4NQs/edit?usp=sharing)")

    #titulo da imagem a seguir
    st.header("Prova e :green[Equipes]")

    #Colocar a imagem do resultado dos saltos ornamentais
    st.image("saltosOrnamentais.png", caption="Resultado da prova de Saltos Ornamentais")

    #Colocar imagem do resultado do nado sinronizado sem nado
    st.image("nadoSincronizado.png", width=400, caption = "Resultado da prova de Nado Sincronizado sem Nado")
    
   
# Criando uma siderbox de avisos 
# avisos sobre as datas de seminário e como acessar o conteúdo.
st.sidebar.text("""AVISOS!!! 

- Para acessar os conteúdos, é só
clicar no link desejado. 

- Seminário de Esportes Técnico 
Combinatório, será nos dias 22 
e 29 de outubro e 06 de Dezembro

- Prova Substituiva dia 06/12/2023, 
somente para os que ficaram de DP
e tiraram menos de 6,0 na prova 
P1. 

""")

 # criando conteiner para a segunda disciplina que será apresentada no site
with st.container():

    #separando os conteiners
    st.write("---")

    # Titulo do primeiro tópico,container da página. 
    st.title(":red[DISCIPLINA DE DIDÁTICA E FORMAÇÃO PROFISSIONAL]")

    #titulo do primeiro assunto da página, conteúdo
    st.header("Conteúdos ")

    #inserido links dos conteúdos da disciplina.
    st.write("[- Licenciatura e ou Bacharelado](https://docs.google.com/presentation/d/1ceQrs86LsMly_Rjq4tBK5ewHZzrTTvXZ8XpEpRe0MHM/edit?usp=sharing)" )
    st.write("[- História da Educação Física - Resumo](https://docs.google.com/presentation/d/1kIqjYfqujbxp8NylBRNiBCccRBqtR56l/edit?usp=sharing&ouid=106510003901617511102&rtpof=true&sd=true)")
    st.write("[- Abordagens da Educação Física](https://docs.google.com/presentation/d/1Oqm6h6QSrerxGPSepwyQHwUnRDUI85OBWFpmyiasVlc/edit?usp=sharing)")
    st.write("[- Disática, Educação Física e suas relações](https://docs.google.com/presentation/d/1ZW1-HESB9eF8HaZdVJousbi2-1N5ic7a/edit?usp=sharing&ouid=106510003901617511102&rtpof=true&sd=true)")
    st.write("[- Metodologia de Ensino - JEC's e TDfU](https://docs.google.com/presentation/d/1nF0M7ukChpTimq24Fb6F4Jh6OSx3cpcp_KJrQs-TIsY/edit?usp=sharing)")
    
    #informação sobre como acessar os conteúdos
    st.write("Click nos conteúdos para o acesso")
