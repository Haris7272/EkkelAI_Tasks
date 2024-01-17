import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from rembg import remove


# Model 1

def opt_text_completion(input_text):
    # Load pre-trained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m")

    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate predictions using the model
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2)

    # Decode the generated output
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text


# Model 2

from io import BytesIO

def remove_background(uploaded_image):
    input_data = uploaded_image.read()

    output_data = remove(input_data)

    # Create BytesIO object to hold output data
    output_stream = BytesIO()
    output_stream.write(output_data)

    return output_stream



# import cv2
# from PIL import Image
# def main():
#     choose = int(input("Choose which Model to use\n 1. OPT Text Completion\n 2. Image Background Removal\n"))
    
#     if choose == 1:
#         input_text = input("Give me a sentence to complete: ")
#         generated_output = opt_text_completion(input_text)
#         print("Generated Output (OPT):", generated_output)

#     elif choose == 2:
#         input_image = cv2.imread('test1.png')

#         # Check if the image was successfully read
#         if input_image is not None:
#             # Perform Background Removal
#             output_stream = remove_background(input_image)

#             # Convert BytesIO to PIL Image and display
#             output_image = Image.open(output_stream)
#             output_image.show()

#             # Save the output image
#             output_path = 'output1.png'
#             output_image.save(output_path)
#             print(f"Background removed. Result saved to {output_path}")
#         else:
#             print("Error: Unable to read the input image.")


#     else:
#         print("Wrong input. Exiting...")

# if __name__ == "__main__":
#     main()

