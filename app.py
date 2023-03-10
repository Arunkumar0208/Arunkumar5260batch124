import pickle
import streamlit as st 


pickle_in = open("BankNote.pickel","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(varaince,skewness,curtosis,entropy):
    prediction=classifier.predict([[varaince,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("bank_note Prediction")
    variance = st.text_input("variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(varaince,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
