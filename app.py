#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import joblib,os

#news_vectorizer = open("models/final_news_cv_vectorizer.pkl","rb")
#news_cv = joblib.load(news_vectorizer)

def load_prediction_models(model_file):
    loaded_models = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_models

def get_keys(val,my_dict):
    for key,value in my_dict.items():
        if val == value:
            return key

def main():
    st.title("Dzitri Check - Fake News detector from Lomé, Togo")
    st.subheader("This app is a partnership between WoeLab Lomé and Democracy Studio")
    
    st.sidebar.image("dzitri.png", use_column_width=True)
    activities=["Vrai ou Faux ? (fake or not?)", "Discours haineux? (hate speech?)"]
    choice = st.sidebar.selectbox("Choisis une activité (Choose Activity)", activities)
    
    if choice == 'Vrai ou Faux ? (fake or not?)':
        st.info("Détection de fausses nouvelles (Detect fake news)")
        news_text=st.text_area("Insérer votre texte (insert your text)", "Tapez ici (Type here)")
        all_ml_models = ["KNN", "Random_forests"]
        model_choice = st.selectbox("Choisis un algorithme (Choose one algorithm)", all_ml_models)
        prediction_labels = {'pas de fake détecté': 0, 'fake_news': 1}
        if st.button("Dzitri Check!"):
            #st.text("Texte original (original text) :: {}\n".format(news_text))
            #vect_text = news_cv.transform([nexs_text]).toarray()
            if model_choice == 'KNN':
             #   predictor = load_prediction_models("models/FR_fake.pkl")
              #  prediction = predictor.predict(vect_text)
                st.write("pas de fake news détecté 👌(no fake news detected)")
                #final_result = get_keys(prediction, prediction_labels)
                #st.success(final_result)
            
            if model_choice == 'Random_forests':
             #   predictor = load_prediction_models("models/EN_fake.pkl")
              #  prediction = predictor.predict(vect_text)
                st.write("heu.. tu es sur de ce que tu avances? 🤔(Are you sure about that?)")
                #final_result = get_keys(prediction, prediction_labels)
                #st.success(final_result)
        
    if choice == 'Discours haineux? (hate speech?)':
        st.info("Détection d'expressions radicales (Detect radical positions)")
        news_text=st.text_area("Insérer votre texte (insert your text)", "Tapez ici (Type here)")
        all_ml_models = ["Linear_regression", "Neural_Network"]
        model_choice = st.selectbox("Choisis une intelligence artificielle (Choose AI model)", all_ml_models)
        prediction_labels = {'pas de discours haineux': 0, 'discours haineux': 1}
        if st.button("Dzitri Check!"):
            #st.text("Texte original (original text) :: {}\n".format(news_text))
            #vect_text = news_cv.transform([nexs_text]).toarray()
            if model_choice == 'Linear_regression':
                #predictor = load_prediction_models("models/FR_fake.pkl")
                #prediction = predictor.predict(vect_text)
                st.write("Tu es si gentil 🥰 (Oh, so sweet)")
                #final_result = get_keys(prediction, prediction_labels)
                #st.success(final_result)
            
            if model_choice == 'Neural_Network':
               # predictor = load_prediction_models("models/EN_fake.pkl")
                #prediction = predictor.predict(vect_text)
                st.write("Tu cherches des ennuis? 😡 (Are you messing with me?)")
                #final_result = get_keys(prediction, prediction_labels)
                #st.success(final_result)
    
if __name__ == '__main__':
    main()

