from dotenv import load_dotenv
load_dotenv()

from google import genai
from PIL import Image
from io import BytesIO
import os

# Configure the client with your API key
client = genai.Client()

def get_available_bags():
    """Get list of available bag files"""
    bag_files = []
    for file in os.listdir('.'):
        if file.endswith('Bag.png'):
            bag_files.append(file)
    return sorted(bag_files)

def select_bag():
    """Interactive bag selection"""
    bags = get_available_bags()
    
    if not bags:
        print("No bag files found!")
        return None
    
    print("\nAvailable bags:")
    for i, bag in enumerate(bags, 1):
        print(f"{i}. {bag}")
    
    while True:
        try:
            choice = int(input(f"\nSelect a bag (1-{len(bags)}): "))
            if 1 <= choice <= len(bags):
                selected_bag = bags[choice - 1]
                print(f"You selected: {selected_bag}")
                return selected_bag
            else:
                print(f"Please enter a number between 1 and {len(bags)}")
        except ValueError:
            print("Please enter a valid number")

prompt = """Create a new image by combining the elements from the provided images. Take the person from image 1 and place them with the handbag from image 2. The final image should be a natural scene of the person holding the handbag in a pickleball court setting."""

image1 = Image.open("viman.jpg")
selected_bag = select_bag()

if selected_bag is None:
    print("No bag selected. Exiting...")
    exit()

image2 = Image.open(selected_bag)

# Call the API to generate content
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt,image1,image2]
)

# The response can contain both text and image data.
# Iterate through the parts to find and save the image.
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("boy-with-bag.png")

        