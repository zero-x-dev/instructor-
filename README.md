# Instructor:-

Instructor is often a library (like InstructorEmbedding from UKPLab) that you can install and use in your code. It provides pre-trained models that understand instructions to generate useful embeddings or outputs.

It’s not just a model, but usually a package or framework that wraps those models with code to easily apply instruction-following capabilities.
--------
# Requirements

* instructor
- openai
* pydantic
--------------------------
### Install the package:
```bash
pip install openai instructor pydantic
```

## URL :

    base_url="https://api.groq.com/openai/v1",

 
 
 # how it works means 
   - instructor :The instructor library enables parsing the natural language output of a language model into structured Pydantic models  

 - instructor.from_openai(client) wraps the OpenAI client so that you can request a response_model, which automatically parses and validates the model output.
 
 ----------
 # Run the script :
 ```bash
 python3 instructor-lm.py
 ```
