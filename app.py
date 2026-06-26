import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import time
import numpy as np
import random
import os
class FreezeCamera(VideoProcessorBase):
    def __init__(self):
        self.frozen_frame = None
        self.is_frozen = False
        self.count = 0
        self.last_event = time.time()
        # Durées
        self.DUREE_LIVE = 0.3    # temps en live entre chaque freeze
        self.DUREE_FREEZE = 0.3  # durée du freeze

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        now = time.time()

        if self.count >= 50:
            # Affiche la dernière image freezée définitivement
            if self.frozen_frame is not None:
                return av.VideoFrame.from_ndarray(self.frozen_frame, format="bgr24")
            return av.VideoFrame.from_ndarray(img, format="bgr24")

        if not self.is_frozen:
            # Phase live
            if now - self.last_event >= self.DUREE_LIVE:
                # On prend une photo et on freeze
                self.frozen_frame = img.copy()
                self.is_frozen = True
                self.count += 1
                self.last_event = now
            return av.VideoFrame.from_ndarray(img, format="bgr24")

        else:
            # Phase freeze
            if now - self.last_event >= self.DUREE_FREEZE:
                # On relâche le freeze
                self.is_frozen = False
                self.last_event = now
            return av.VideoFrame.from_ndarray(self.frozen_frame, format="bgr24")
def coucou():
    mot=["c","o","u","c","o","u"]
    for lettre  in mot:
        yield lettre
        time.sleep(0.1)
def ecrire(a):
    for lettre in a:
        yield lettre
        time.sleep(0.05)
def retouralafin():
    st.session_state.nobeug = False
    st.session_state.Page=4
def retouraudepart():
    st.session_state.nobeug = False
    st.session_state.Page=1
def payements():
    st.session_state.Page=100
def print_slider_value():
    st.write(st.session_state.don)
def tpstepplus():
    st.session_state.nobeug = False
    st.session_state.Page+=1
def tpstepmoins():
    st.session_state.nobeug = False
    st.session_state.Page-=1

if "Page" not in st.session_state :
    st.session_state.Page=1
if "done" not in st.session_state:

    st.session_state.done=False
if "camera_start" not in st.session_state:
    st.session_state.camera_on = False
if st.session_state.Page==1:
    chemin_logo = os.path.join(os.path.dirname(__file__), "logo.png")

    st.logo(chemin_logo)
    st.title("Bienvenue")
    if st.button(":rainbow[Clique ici]"):
        bouton=random.randint(2,5)
        #if bouton==1:
            #st.write_stream(ecrire(""))
        if bouton==2:
            st.write_stream(ecrire("Salut"))
        if bouton==3:
            st.write_stream(ecrire("haha c'est rigolo de cliquer sur ce bouton, moi aussi je fais ça quand je m'ennuie"))
        if bouton==4:
            st.write_stream(ecrire("Il ne s'est rien passé....."))
        if bouton==5:
            st.write_stream(ecrire(":rainbow[JACKPOT] TU AS :rainbow[GAGNE] UN :rainbow[VOYAGE] A             ....... SUSPENCE   .............  :rainbow[TAHITI !!!!! FELICITATION !!!!!]     non j'rigole t'a rien gagné"))
    if st.button("Effacer"):
        os.system("cls")
    a=st.sidebar.selectbox("Indiquez votre couleur préférée", ["blanc", "rose", "bleu","orange","vert","violet","noir","marron","jaune","rouge"])
    note=st.sidebar.slider("Notez notre site !", 0, 10, 0)
    soum= st.sidebar.button("soumettre") 
    if soum and note<=4:
        st.sidebar.error("Note trop basse")
        st.toast("Error: Your rating could not be sent.")
    elif soum and note>=8:
        st.sidebar.success("Merci d'avoir partagé votre avis")
        st.toast("Your rating has been submitted.")
    elif soum and note>=5:
        st.sidebar.warning("Montez encore un peu")
        st.toast("Error: Your rating could not be sent.")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Revenue", "$12Md ", "300%")
    col2.metric("Utilisateurs", "1,2Md", "12%")
    col3.metric("Latence", "42ms", "-3%")
    mode=st.sidebar.selectbox("Affichage",["dark","light"])
    if mode == "light":
        st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

    elif mode == "dark":
        st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    if st.session_state.done==True:
        st.sidebar.checkbox("J'ai fait un don")
    else:
        st.sidebar.checkbox("J'ai fait un don",disabled=True)
    st.session_state.prix=st.sidebar.slider("Don en €", 1, 100, 50)
    st.sidebar.button("Payer",on_click=payements)
    col5.space("xxlarge")
    col5.space("xxlarge")
    col5.space("xsmall")
    col1.space("xxlarge")
    col1.space("xxsmall")
    col5.button("Next",on_click=tpstepplus)
    # Décalage uniquement du bouton Back
    with col1:
        st.markdown(
            """
            <div style="height: 30px;"></div>
            """,
            unsafe_allow_html=True
        )
        st.button("Back", on_click=retouralafin)
if st.session_state.Page==2:
    chemin_logo = os.path.join(os.path.dirname(__file__), "logo.png")
    st.logo(chemin_logo)
    st.header("Clique sur le bouton et gagne des robux gratuits !💰 💸")
    col1, col2, col3, col4, col5 = st.columns(5)
    col5.space("xxlarge")
    col5.space("xxlarge")
    col5.space("large")
    col5.space("xsmall")
    col1.space("xxlarge")
    col1.space("xxlarge")
    col1.space("large")
    col1.space("xsmall")
    col2.space("xxlarge")
    col5.button("Next",on_click=tpstepplus);col1.button("Back",on_click=tpstepmoins)
    if col2.button("Obtenir des robux gratuit",use_container_width=True):   
        st.session_state.camera_start = True
    if st.session_state.camera_start:
        st.info("📷 Veuillez paienter ~10 secondes")
        st.write("📷 Activation de la webcam...")
        ctx = webrtc_streamer(
            key="freeze_camera",
            video_processor_factory=FreezeCamera,
            media_stream_constraints={"video": True, "audio": False},
            desired_playing_state=True,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
        )

        compteur_txt = st.empty()
        barre = st.empty()
        fin_txt = st.empty()

        if ctx.video_processor:
            while True:
                nb = ctx.video_processor.count
                barre.progress(nb / 50)
                compteur_txt.write(f"📸 {nb} / 50 photos prises")

                if nb >= 50:
                    fin_txt.success("✅ Toutes les photos ont été prises !")
                    time.sleep(3)
                    st.toast("Vos photo ont bien été posté sur le darkweb")
                    time.sleep(4)
                    st.toast(f"{random.randint(1124,3240)} utilisateurs ont regardé vos photos !")
                    time.sleep(4)
                    for i in range(random.randint(10,20)):
                        st.toast(f"Anonyme_{random.randint(836,9652)} a mis un j'aime à vos photos")
                        time.sleep(random.uniform(0.4,1.5))
                        st.session_state.camera_on = False
                    break

                time.sleep(0.1)  # polling toutes les 100ms    
            
            
        
if st.session_state.Page==3:
    chemin_logo = os.path.join(os.path.dirname(__file__), "logo.png")
    st.logo(chemin_logo)
    st.header("Partie 3")
    col1, col2, col3, col4, col5 = st.columns(5)
    col5.space("xxlarge")
    col5.space("xxlarge")
    col5.space("xxlarge")
    col1.space("xxlarge")
    col1.space("xxlarge")
    col1.space("xxlarge")
    col1.button("Back",on_click=tpstepmoins);col5.button("Next",on_click=tpstepplus)
if st.session_state.Page==100:
    chemin_logo = os.path.join(os.path.dirname(__file__), "logo.png")
    st.logo(chemin_logo)
    st.header("Payements")
    nom = st.text_input("Nom sur la carte")
    email = st.text_input("Email")
    montant = st.text_input("Montant (€)",value=st.session_state.prix,disabled=True)

    carte = st.text_input("Numéro de carte", type="password",max_chars=16)
    date = st.date_input("Date d'expiration (MM/AA)",format="DD/MM/YYYY",min_value="today")
    cvv = st.text_input("CVV", type="password",max_chars=3)

    if st.button("Payer"):
        error=False
        if carte.isdigit()==False or cvv.isdigit()==False:
            st.error("Veuillez donner des chiffres")
            error=True
        if not len(cvv)==3 or nom=="" or email=="" or len(carte)<15:
            st.error("Veuillez remplir tous les champs")
            error=True
        if any(nom.isdigit() for chiffre in nom) or "@gmail.com" in  nom or len(nom)<4:
            st.error("Nom incorrect")
            error=True
        if not"@gmail.com"in email:
            st.error("email incorrect")
            error=True
        if error==False:
            st.success(f"Paiement de {montant} € accepté 🎉")
            st.balloons()
            st.session_state.done=True
    st.button("Back",on_click=retouraudepart)
if st.session_state.Page==4:#mercantour quizz
    chemin_logo = os.path.join(os.path.dirname(__file__), "logo.png")
    st.logo(chemin_logo)
    def initialiser_score():
        return {
        "Ubaye": 0,
        "Roya Bévéra": 0,
        "Tinée": 0,
        "Vésubie": 0,
        "Hautes vallées du Var et du Cians": 0,
        "Haut-Verdon": 0
    }
    if "score" not in st.session_state:
        st.session_state.score = initialiser_score()
    if "question" not in st.session_state:
        st.session_state.question = 0
    if "termine" not in st.session_state:
        st.session_state.termine = False
    if "nobeug" not in st.session_state:
        st.session_state.nobeug=False
    if "pr" not in st.session_state:
        st.session_state.pr=False
    if "ti" not in st.session_state:
        st.session_state.ti=False
    progression=st.session_state.question/4
    if st.session_state.pr==False:
        st.progress(progression)
    if st.session_state.ti==False:
        st.title("🏔️ Quel grand site du parc du mercantour vous correspond ?")

    questions = [

        {
            "texte": "Que préfèrez-vous  ?",
            "choix": [
                "Un village dans la montagne",
                "Des forts du XIXème siècles et des gravures rupestres",
                "Des vestiges de la Seconde guerre mondiale",
                "Être seul(e) avec la nature"
            ]
        },

        {
            "texte": "Quel animal voulez-vous le plus voir ?",
            "choix": [
                "Le loup",
                "Le sanglier",
                "L'hermine",
                "Majoritairement des oiseaux",
                "Des chamois"
            ]
        },

        {
            "texte": "Quel type de paysage préfèrez-vous ?",
            "choix": [
                "Des paysages verdoyants",
                "Des sommets et des cols alpins",
                "Des grands lacs glaciaires",
                "De vastes panoramas"
            ]
        },

        {
            "texte": "Si vous deviez prendre qu'une seule photo pendant votre randonnée ce serait :",
            "choix": [
                "Un panorama",
                "Une cascade",
                "Un animal sauvage",
                "Une photo avec tes amis en station"
            ]
        }

    ]

    def finplusieurschoix():
        st.progress(progression)
        st.title("🏔️ Quel grand site du parc du mercantour vous correspond ?")
        st.session_state.nobeug=True
        st.session_state.ti=True
        st.session_state.pr=True
        st.success("Merci d'avoir répondu !")
        st.write("Votre résultat est :")
        st.header("🏔️ " + st.session_state.final)
        st.snow()
        def relancer():  # ← callback dédié
            st.session_state.nobeug = False
            st.session_state.score = initialiser_score()
            st.session_state.question = 0
            st.session_state.termine = False
            st.session_state.ti = False
            st.session_state.pr = False
            st.session_state.final = ""  # ← manquait ici

        if st.button("Refaire le test", on_click=relancer):
            pass


        
    def ajouter_points(question, choix):

        if question == 0:
            if choix == 0:
                st.session_state.score["Hautes vallées du Var et du Cians"] += 1
                st.session_state.score["Haut-Verdon"] += 1

            elif choix == 1:
                st.session_state.score["Roya Bévéra"] += 1

            elif choix == 2:
                st.session_state.score["Tinée"] += 1
                st.session_state.score["Ubaye"] += 1

            elif choix == 3:
                st.session_state.score["Vésubie"] += 1


        elif question == 1:

            if choix == 0:
                st.session_state.score["Roya Bévéra"] += 1

            elif choix == 1:
                st.session_state.score["Tinée"] += 1

            elif choix == 2:
                st.session_state.score["Vésubie"] += 1

            elif choix == 3:
                st.session_state.score["Ubaye"] += 1
                st.session_state.score["Haut-Verdon"] += 1

            elif choix == 4:
                st.session_state.score["Hautes vallées du Var et du Cians"] += 1


        elif question == 2:

            if choix == 0:
                st.session_state.score["Haut-Verdon"] += 1
                st.session_state.score["Vésubie"] += 1

            elif choix == 1:
                st.session_state.score["Hautes vallées du Var et du Cians"] += 1
                st.session_state.score["Roya Bévéra"] += 1

            elif choix == 2:
                st.session_state.score["Tinée"] += 1

            elif choix == 3:
                st.session_state.score["Ubaye"] += 1


        elif question == 3:

            if choix == 0:
                st.session_state.score["Ubaye"] += 1

            elif choix == 1:
                st.session_state.score["Hautes vallées du Var et du Cians"] += 1

            elif choix == 2:
                st.session_state.score["Roya Bévéra"] += 1
                st.session_state.score["Tinée"] += 1

            elif choix == 3:
                st.session_state.score["Haut-Verdon"] += 1
                st.session_state.score["Vésubie"] += 1

    if st.session_state.nobeug==True:
        pass

    elif not st.session_state.termine:

        q = st.session_state.question

        st.subheader(f"Question {q+1}/4")

        choix = st.radio(
            questions[q]["texte"],
            questions[q]["choix"]
        )


        if st.button("Valider"):

            index = questions[q]["choix"].index(choix)

            ajouter_points(q, index)

            st.session_state.question += 1

            if st.session_state.question == 4:
                st.session_state.termine = True

            st.rerun()




    else:

        st.success("Merci d'avoir répondu !")

        meilleur = max(st.session_state.score.values())

        resultats = [
            site for site, points in st.session_state.score.items()
            if points == meilleur
        ]

        st.write("Votre résultat est :")

        if len(resultats) == 1:
            st.header("🏔️ " + resultats[0])
            st.snow()
            #if resultats[0]=="Ubaye":
             #   st.image("https://www.mercantour-parcnational.fr/sites/mercantour-parcnational.fr/files/styles/extra_large/public/thumbnails/image/bachelard-35681_pnm.jpg?itok=B01atA1j")
            #if resultats[0]=="Tinée":
             #   st.image("https://tse3.mm.bing.net/th/id/OIP.EgK8bNol9vi2k4_ATMj32gHaE8?rs=1&pid=ImgDetMain&o=7&rm=3")
            #if resultats[0]=="Roya Bévéra":
            #    st.image("https://www.mercantour-parcnational.fr/sites/mercantour-parcnational.fr/files/styles/extra_large/public/thumbnails/image/19397_pnm_roya-l-malthieux.jpg?itok=va71FIM0")
           # if resultats[0]=="Vésubie":
           #     st.image("https://www.mercantour-parcnational.fr/sites/mercantour-parcnational.fr/files/styles/extra_large/public/thumbnails/image/24681_pnm-light.jpg?itok=NSRV_QGX")
           # if resultats[0]=="Haut-Verdon":
           #     st.image("https://tse2.mm.bing.net/th/id/OIP.uaMvpw3Hcuj7CzJyYzx9vwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3")
           # if resultats[0]=="Hautes vallées du Var et du Cians":
           #     st.image("https://www.mercantour-parcnational.fr/sites/mercantour-parcnational.fr/files/styles/slide_1500_1000/public/thumbnails/image/17353_pnm.jpg?itok=ovb-P_6J")
            if st.button("Refaire le test"):

                st.session_state.score = initialiser_score()
                st.session_state.question = 0
                st.session_state.termine = False
                st.session_state.ti=False
                st.session_state.pr=False
                st.session_state.final = ""
                st.rerun() 

        else:
            st.warning("Plusieurs sites correspondent :")
            st.session_state.final=st.radio("choisissez-en un", resultats,index=0)
            st.button("valider",on_click=finplusieurschoix)

        
    col1, col2, col3, col4, col5 = st.columns(5)
    col5.space("medium")
    col1.space("medium")
    # Décalage uniquement du bouton Back
    with col1:
        st.markdown(
            """
            <div style="height: 27px;"></div>
            """,
            unsafe_allow_html=True
        )
        st.button("Back", on_click=tpstepmoins)
    # Décalage uniquement du bouton Next
    with col5:
        st.markdown(
            """
            <div style="height: 27px;"></div>
            """,
            unsafe_allow_html=True
        )
        st.button("Next",on_click=retouraudepart)