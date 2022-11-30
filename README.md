# text_comparison_service
Implements some of the translation validation routines from Hugging Face's '''evaluate''' library.

The functions are wrapped with '''fastapi''' so their accessible via a REST call.

To run, execute 

'''
uvicorn service:app
'''
