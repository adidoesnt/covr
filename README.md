# Covr

## Overview

Covr is a command-line tool that allows users to upload files to a knowledge base and query the knowledge base using natural language queries. It uses the Chroma vector database to store the files and the OpenAI API to generate the answers.

Covr was originally intended to be used as a tool to tailor resumes and cover letters to specific job requirements. However, it can also be used for general retrieval-augmented generation (RAG) tasks.

## Installation

1. Install the required dependencies:

```bash
poetry install
```

2. Set up the environment variables:

```bash
cp .env.example .env

# The example .env file contains the required environment variables, except OPENAI_API_KEY.

# You will need to obtain your own OpenAI API key and set it in the .env file.
```

3. That's it! You can now use the tool.

## Usage

### Uploading Files

To upload files to the knowledge base, use the `upload` command:

```bash
poetry run covr upload --path <path_to_directory_or_file>
```

This will upload the files to the knowledge base and store them in the Chroma vector database.

### Querying the Knowledge Base

To query the knowledge base, use the `query` command:

```bash
poetry run covr query --query <query> --output <output_file_path>
```

This will query the knowledge base using the given query and write the results to the specified output file.
