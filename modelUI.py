import streamlit as st
from models import opt_text_completion, remove_background
from PIL import Image

def main():
    st.title("Streamlit OPT Text Completion and Background Removal")

    # Model 1: Text completion
    st.header("MODEL 1: \nOPT Text Completion")

    # Form to take input text
    with st.form("opt_form"):
        input_text_opt = st.text_area("Enter Text for OPT")
        st.markdown(
            """<style>
                div[data-testid="stFormSubmitButton"] button {
                    background-color: red;
                    color: white;
                }
            </style>""",
            unsafe_allow_html=True
        )

        submit_button = st.form_submit_button("Generate completed Text")

    if submit_button:
        # give input to the OPT model and obtain result
        text_result = opt_text_completion(input_text_opt)


        st.subheader("Input Text:")
        st.text(input_text_opt)

        st.subheader("Output Text (OPT):")
        st.text(text_result)


    # Model 2: background remover
    st.header("MODEL 2: \nImage Background Removal")

    # Upload Image
    uploaded_image_bg_removal = st.file_uploader("Upload Image for Background Removal", type=["jpg", "jpeg", "png"])

    if uploaded_image_bg_removal is not None:
        # Display uploaded image
        st.image(uploaded_image_bg_removal, caption="Uploaded Image", use_column_width=True)

        if st.button("Remove Background"):
            # call the funciton to use the model for background removal
            output_stream = remove_background(uploaded_image_bg_removal)

            # Display Image without Background
            st.subheader("Image without Background:")
            # BytesIO to PIL conversion to display
            output_image = Image.open(output_stream)
            st.image(output_image, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
