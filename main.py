from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor

from fastapi import FastAPI, File, UploadFile


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get")
async def get():
    try:
        

        image = Image.open("current_file.jpg")

        langs = ["en"]  # Replace with your languages
        det_processor, det_model = segformer.load_processor(), segformer.load_model()
        rec_model, rec_processor = load_model(), load_processor()

        predictions = run_ocr([image], [langs], det_model,
                              det_processor, rec_model, rec_processor)
                
        response = ' '.join(['' + text_line.text for text_line in predictions[0].text_lines])

        return {'message': response}
    except Exception as e:
        return f"{'message': 'There was an error uploading the file: {str(e)}'}"
    finally:
        pass

