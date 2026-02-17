import random
import time

def simulate_glitch(image_data):
    """Simulate a glitch effect on image data."""
    glitched_data = []
    for byte in image_data:
        # Randomly introduce glitches by altering bytes
        if random.random() < 0.05:  # 5% chance of glitching a byte
            glitched_data.append(random.randint(0, 255))
        else:
            glitched_data.append(byte)
    return bytearray(glitched_data)

def display_image(image_data):
    """Display an image in the console using ASCII characters."""
    chars = "@%#*+=-:. "
    width = 100
    height = int(len(image_data) / (3 * width))  # Assuming RGB data
    ascii_img = ""
    for i in range(height):
        row = image_data[i * width * 3:(i + 1) * width * 3]
        for j in range(0, len(row), 3):
            r, g, b = row[j], row[j+1], row[j+2]
            gray = int((r + g + b) / 3)
            ascii_img += chars[int(gray / (256 / len(chars)))]
        ascii_img += "\n"
    print(ascii_img)

def main():
    try:
        # Simulate capturing an image
        print("Simulating camera capture...")
        time.sleep(1)  # Simulate delay

        # Generate random image data (simulated capture)
        image_data = bytearray(random.randint(0, 255) for _ in range(3 * 100 * 40))  # 100x40 RGB image
        print("Captured image data.")

        # Apply glitch effect
        print("Applying glitch effect...")
        glitched_image_data = simulate_glitch(image_data)
        print("Glitch applied.")

        # Display the original and glitched images
        print("\nOriginal Image:")
        display_image(image_data)

        print("\nGlitched Image:")
        display_image(glitched_image_data)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()