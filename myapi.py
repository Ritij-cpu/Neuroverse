import nlpcloud


class API:

    def __init__(self):
        self.client = nlpcloud.Client("stable-diffusion", "67ee92a07a11daf205627520df4076cd3a7550ef", gpu=True)

    def image_generation(self,text):
        response = self.client.image_generation(text)
        return response



