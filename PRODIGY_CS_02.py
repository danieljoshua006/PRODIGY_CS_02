from PIL import Image
import os

def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                # Basic pixel manipulation (modulo 256 to keep in range)
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[i, j] = (r, g, b)

        img.save(output_path)
        print(f"✅ Encrypted image saved as: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                # Reverse pixel manipulation
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b)

        img.save(output_path)
        print(f"✅ Decrypted image saved as: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🔏 Image Encryption Tool - ProDigy Infotech")

    action = ''
    while action not in ['encrypt', 'decrypt']:
        action = input("Do you want to 'encrypt' or 'decrypt' an image? ").strip().lower()

    image_path = input("Enter the path of the image file: ")
    key = int(input("Enter encryption/decryption key (number): "))

    if not os.path.exists(image_path):
        print("❌ File not found.")
        return

    output_path = input("Enter output file name (with .png or .jpg): ")

    if action == 'encrypt':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
