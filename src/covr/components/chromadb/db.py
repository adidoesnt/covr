from chromadb import HttpClient, config
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.outputs.llm_result import LLMResult

from covr.components.chromadb.constants import CHROMADB_HOST, CHROMADB_PORT, CHROMA_CLIENT_AUTH_PROVIDER, CHROMA_CLIENT_AUTH_CREDENTIALS, CHROMA_AUTH_TOKEN_TRANSPORT_HEADER
from covr.components.langchain.constants import EMBEDDINGS_MODEL_NAME
from covr.components.langchain.generator import llm

embeddings_model = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)

client = HttpClient(
    host=CHROMADB_HOST,
    port=int(CHROMADB_PORT),
    settings=config.Settings(
        chroma_client_auth_provider=CHROMA_CLIENT_AUTH_PROVIDER,
        chroma_client_auth_credentials=CHROMA_CLIENT_AUTH_CREDENTIALS,
        chroma_auth_token_transport_header=CHROMA_AUTH_TOKEN_TRANSPORT_HEADER
    )
)

def connect_chromadb():
    try:
        client.heartbeat()
        
        print("Connected to ChromaDB.")
    except Exception as e:
        print("Error connecting to ChromaDB:", e)
        exit(1)
        
def upload_resume(user_id, file_content):
    try:
        print(f"Uploading resume for user {user_id}...")
        
        collection = client.get_or_create_collection(f"user_{user_id}")
        embeddings = embeddings_model.embed_query(file_content)
        
        collection.add(
            ids=[f"resume_{user_id}"],
            metadatas=[{"user_id": user_id}],
            embeddings=embeddings,
            documents=[file_content]
        )
        
        print(f"Resume uploaded successfully for user {user_id}.")
    except Exception as e:
        print("Error uploading resume:", e)
        raise e
    
def check_if_resume_exists(user_id):
    try:
        collection = client.get_collection(f"user_{user_id}")
        
        if collection.count() == 0:
            return False
        else:
            return True
    except Exception as e:
        print("Error checking if resume exists:", e)
        raise e
    
def get_resume_collection(user_id):
    try:
        collection = client.get_collection(f"user_{user_id}")
        
        return collection
    except Exception as e:
        print("Error getting resume collection:", e)
        raise e
    
def query_resume_collection(user_id, embeddings):
    try:
        collection = get_resume_collection(user_id=user_id)
        
        documents = collection.query(
            query_embeddings=[embeddings], 
            n_results=1, 
            include=["documents", "metadatas"]
        )
        
        results = documents.get("documents", [])
        
        data = "\n".join(results[0])
        return data
    except Exception as e:
        print("Error querying resume collection:", e)
        raise e
    
def get_job_description_embeddings(job_description):
    try:
        embeddings = embeddings_model.embed_query(job_description)
        
        return embeddings
    except Exception as e:
        print("Error getting job description embeddings:", e)
        raise e
    
def build_prompt(job_description, resume_data):
    prompt = f"""
    You are a helpful assistant that excels at creating tailored cover letters for job applications.
    
    Job Description: {job_description}
    
    Candidate Resume: {resume_data}
    
    Please write a professional, engaging cover letter tailored to this job, highlighting the candidate's qualifications, skills, and experience. Use a formal tone and emphasize how the candidate's background aligns with the job requirements.
    
    Write the cover letter below:
    """
    
    return prompt  
    
def generate_cover_letter(user_id, job_description):
    try:
        embeddings = get_job_description_embeddings(job_description=job_description)
        resume_data = query_resume_collection(user_id=user_id, embeddings=embeddings)
        
        if not resume_data:
            raise Exception("No resume data found.")
        
        prompt = build_prompt(job_description=job_description, resume_data=resume_data)
        response: LLMResult = llm.generate([prompt])
        
        # TODO: fix this
        cover_letter = response.generations[0][0].text
        
        return cover_letter
    except Exception as e:
        print("Error generating cover letter:", e)
        raise e
    