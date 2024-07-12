from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
import image_to_text
import caption_generation
from fastapi.responses import JSONResponse
import time


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
   "*"
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_methods=["*"],
   allow_credentials=True,
   allow_headers=['*'])

class ImageRequest(BaseModel):
    image: str

@app.post("/caption/")
async def read_root(request: ImageRequest):
    image=request.image
    time.sleep(5)
    text=image_to_text.image_to_text(image)
    print(text)
    caption=caption_generation.create_caption(text)
    print(caption)
    return JSONResponse(content={"caption": caption})
    # if text:
    #     caption=caption_generation.create_caption(text)
    #     return caption
   


if __name__ == "__main__":
   import asyncio
   import nest_asyncio
   nest_asyncio.apply()  # Allows running asyncio code in Jupyter Notebook or similar environments
   loop = asyncio.get_event_loop()
   loop.create_task(uvicorn.run(app, host="127.0.0.1", port=9000))
   try:
       loop.run_forever()
   except KeyboardInterrupt:
       pass
   finally:
       loop.close()