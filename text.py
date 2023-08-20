
import keras_ocr
import matplotlib.pyplot as plt
import streamlit as st






st.title('TextSearch')

tab0,tab1, tab2 = st.tabs(["Home ","Get all text from the given picture", "Search for specific tex in a given picture"])

with tab0:
   st.header("TextSearch")
   st.text("Discover the power of seamless text extraction from images with TextSearch Vision, a cutting-edge application that revolutionizes the way you interact with visual content. Gone are the days of manual transcription and time-consuming data entry – TextSearch Vision empowers you to effortlessly uncover and utilize text within images.\n"

"🔍 Effortless Image Text Search:\n With TextSearch Vision, the hassle of poring over images for specific text is a thing of the past. Our advanced image recognition technology quickly and accurately scans images to locate and extract embedded text.\n"

"📸 Versatile Image Input:\n Whether it's photographs, scanned documents, screenshots, or graphics, TextSearch Vision easily handles a wide range of image formats. Simply upload your images, and the application takes care of the rest.\n"

"💬 Instant Text Extraction:\n Extracted text is immediately presented to you in an easily readable format. Whether it's paragraphs, lists, or snippets, you'll have the text at your fingertips within seconds.\n"

"⚙️ Advanced OCR Technology:\n TextSearch Vision leverages state-of-the-art Optical Character Recognition (OCR) algorithms to ensure exceptional accuracy in text extraction, even from complex images and diverse fonts.\n")
   st.image("ocr.jpeg")
with tab1:
   st.text("upload your image by selecting it and you will get all the existing text within it in the text area bellow")
   st.header("Select your image")
   uploaded_file_1 = st.file_uploader("Choose a file",accept_multiple_files=False)
   
   
   txt=" "
   if uploaded_file_1 is not None:
    
    with open(uploaded_file_1.name,"wb") as f:
     f.write(uploaded_file_1.getbuffer())
    st.image(uploaded_file_1.name,width=300)
    pipeline = keras_ocr.pipeline.Pipeline()
    images = [
    keras_ocr.tools.read(uploaded_file_1.name) ]
    prediction_groups = pipeline.recognize(images)
    counter=0
    for text, box in prediction_groups[0]:
      txt += text+" "
      counter +=1
      if (counter==5):
        txt+="\n"
        counter=0
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("text detection")
    for image, predictions in zip(images, prediction_groups):
        plt.figure(figsize=(10, 20))
        keras_ocr.tools.drawAnnotations(image=image, predictions=predictions)
        st.pyplot()
    st.header("Extracted text ")
    st.text_area('Text', txt)
with tab2:
   st.text("upload your image by selecting it and enter the word you want to search within it.")
   st.header("Select your image")
   uploaded_file_2 = st.file_uploader("Choose your file",accept_multiple_files=False)

   if uploaded_file_2 is not None:
     
     with open(uploaded_file_2.name,"wb") as f:
      f.write(uploaded_file_2.getbuffer())
     st.image(uploaded_file_2.name,width=300)
   st.header("Enter the searched word")
   given_text = st.text_input('tap your word here')
   
   if st.button('Start searching') :

    pipeline = keras_ocr.pipeline.Pipeline()
    images = [
    keras_ocr.tools.read(uploaded_file_2.name) ]
    prediction_groups = pipeline.recognize(images)
    
    extracted_text=[]
    for text, box in prediction_groups[0]:
      if given_text == text:
        new_tuple = (text,box)
        extracted_text.append(new_tuple)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("text detection")
    
    plt.figure(figsize=(10, 20))
    keras_ocr.tools.drawAnnotations(image=images[0], predictions=extracted_text)
    st.pyplot()
   