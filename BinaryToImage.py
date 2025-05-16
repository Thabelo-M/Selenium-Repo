# Reads binary content and saves as .jpg
with open("binary_image.bin", "rb") as input_file:
    binary_data = input_file.read()

with open("output_image.jpg", "wb") as image_file:
    image_file.write(binary_data)

print("Image converted and saved.")