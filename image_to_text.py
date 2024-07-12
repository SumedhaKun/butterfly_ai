import os
from dotenv import load_dotenv

load_dotenv()

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

def image_to_text(img):
    subscription_key = os.getenv('SUB_KEY')
    endpoint = "https://visioninstanceazure.cognitiveservices.azure.com/"

    credentials = CognitiveServicesCredentials(subscription_key)
    client = ComputerVisionClient(endpoint, credentials)

    # Open the image file
    description_results = client.describe_image(img)

    if description_results.captions:
        print('Description:')
        captions=[]
        for caption in description_results.captions:
            print(f'{caption.text} (confidence: {caption.confidence:.2f})')
            captions.append(caption.text)
        return ''.join(captions)
    else:
        print('No description detected.')
        return None