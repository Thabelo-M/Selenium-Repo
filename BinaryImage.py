#Converting the buggy.jpg image to binary string
def image_bin(image_path):
    with open("bug.jpg", "rb") as image:
        binary_string = image.read()
    return binary_string

image_path = "bug.jpg"
binary_string = image_bin("bug.jpg")
print(binary_string)
with open("image_binary.bin", "wb") as binary_file:
    binary_file.write(binary_string)
print(f"Binary image saved to: {image_path}")