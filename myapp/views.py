from rest_framework.response import Response
from rest_framework.decorators import api_view
from langchain_huggingface import HuggingFaceEndpoint

@api_view(['GET'])
def generate_text(request):
    sec_key = "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"
    repo = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceEndpoint(repo_id = repo, max_length = 128, temperature = 0.7, token = sec_key)
    val = llm.invoke("Design a 3D structure on the following description: cube[10,10,10]. I need the design data in JSON format. Do not put any other information or response")
    print(val)
    return Response(val)
