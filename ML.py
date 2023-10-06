import cv2
from PIL import Image
import pytesseract

# Path to the Tesseract executable (update this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def handwriting_to_text_from_frame(frame):
    # Convert the OpenCV BGR image to RGB (PIL format)
    img_rgb = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img_rgb)

    return text

# Read the image from file
image_path = r'C:\Users\pc cam\Desktop\Ai_junctionX\uploads/officiel_1.jpg'
frame = cv2.imread(image_path)

# Perform OCR on the frame
result_text = handwriting_to_text_from_frame(frame)

# Display the result on the frame
cv2.putText(frame, result_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the frame
cv2.imshow('Handwriting Recognition', frame)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()
