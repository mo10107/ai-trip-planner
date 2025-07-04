from fastapi import FastAPI
from fastapi.responses import JSONResponse as JsonResponse
from fastapi.middleware.cors import CORSMiddleware
from agent.agent_workflow import GraphBuilder
import os
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str = Field(..., description="The query to be processed by the agent.")


@app.post("/query")
async def process_travel_agent(query: QueryRequest):
    try:
        graph = GraphBuilder(model_provider="together_ai")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as graph.png at {os.getcwd()}")
        messages = {"messages": [query.question]}
        response = react_app.invoke(messages)

        if isinstance(response, dict) and "messages" in response:
            response_message = response["messages"][-1].content
        else:
            response_message = str(response)

        return JsonResponse(
            {"response": response_message, "status": "success"}, status=200
        )
    
    except Exception as e:
        return JsonResponse({"error": str(e), "status": "error"}, status=500)
