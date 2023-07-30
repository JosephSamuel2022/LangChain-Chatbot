# LangChain-Chatbot
This repository contains a simple Flask-based API that serves as a chatbot. The chatbot uses a library called "langchain" to handle the questions and provide answers based on the data stored in "data.txt". The API receives questions through HTTP POST requests and responds with relevant information from the data file. If the question is not relevant, it responds with a predefined message.

## API Endpoints
POST /api/chatbot: This endpoint receives questions in JSON format and responds with answers based on the information available in the "data.txt" file.

## Example Usage
To ask a question to the chatbot, send a POST request with the question to the endpoint http://localhost:5000/api/chatbot. The question should be provided in JSON format, like this:

{
    "question": "What is your name?"
}

## About Langchain
Large language models (LLMs) are emerging as a transformative technology, enabling developers to build applications they previously could not. However, using these LLMs in isolation is often insufficient for creating a truly powerful app - the real power comes when you combine them with other sources of computation or knowledge.

This library aims to assist in the development of those types of applications

For further information about LangChain, visit :
https://github.com/langchain-ai/langchain

## Important:
This repository solely comprises the backend API, facilitating communication with the corresponding front-end repository located at https://github.com/JosephSamuel2022/My-Portfolio.
