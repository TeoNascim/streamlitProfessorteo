import streamlit as st 

#titulo da página que vai aparecer nos buscadores e no endereço do site.
st.set_page_config(page_title="Professor Téo")


# Criando uma siderbar para colocar os containers dentro
st.sidebar.selectbox("Disciplinas", ("Esportes Técnicos Combinatórios", "Didática e Formação" ))

# criando conteiner para a primeira disciplina que será apresentada no site

with st.container():

    # Titulo do primeiro tópico,container da página. 
    st.title("DISCIPLINA DE 'ESPORTES TÉCNICO COMBINATÓRIO'")

    #titulo do primeiro assunto da página, conteúdo
    st.header("Conteúdos ")

    #informação sobre como acessar os conteúdos
    st.subheader("Click nos conteúdos para o acessar os slides")

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
    st.image("nadoSincronizado.png", caption = "Resultado da prova de Nado Sincronizado sem Nado")
   
# Criando uma siderbox de avisos 
#st.sidebar.selectbox("Avisos", ("Seminário", "Prova Substitutiva"))
st.sidebar.text("Avisos!!! Seminário de Esportes Técnico Combinatório, será nos dias 22 e 29 de outubro e 06 de Dezembro")



  



 # criando conteiner para a segunda disciplina que será apresentada no site
with st.container():

    #separando os conteiners
    st.write("---")

    # Titulo do primeiro tópico,container da página. 
    st.subheader("DISCIPLINA DE DIDÁTICA E FORMAÇÃO PROFISSIONAL")

    #titulo do primeiro assunto da página, conteúdo
    st.title("Conteúdos ")

    #informação sobre como acessar os conteúdos
    st.write("Click nos conteúdos paro o acesso")
