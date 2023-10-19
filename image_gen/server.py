import os
import torch as T

from fastapi import FastAPI
from fastapi.responses import FileResponse
from diffusers import DiffusionPipeline
from diffusers.models.attention_processor import AttnProcessor2_0


MODEL_NAME = os.getenv("MODEL_NAME")
app = FastAPI()
pipe = DiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=T.bfloat16,
    safety_checker=None,
    use_safetensors=True,
).to("cuda")
pipe.unet.set_attn_processor(AttnProcessor2_0())


@app.post("/process/")
async def process_image(prompt: str):
    out = pipe(
        prompt=prompt,
        negative_prompt="(worst quality:1.6, low quality:1.6), (zombie, sketch, interlocked fingers, comic)",
        guidance_scale=7,
        height=1024,
        width=512,
        num_inference_steps=25,
        num_images_per_prompt=1,
    )
    image = out[0][0]
    image.save("./tmp.jpeg")
    
    return FileResponse("./tmp.jpeg", media_type="image/jpeg")
