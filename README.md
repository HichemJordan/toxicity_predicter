#### toxicity_predicter
## Docker part
#To create the docker image placec yourself in the folder and run the command :
"docker build -t myimage ."
and then run the container with :
"docker run -d --name mycontainer -p 80:80 myimage"

## Fastapi part
#to test the code with fastapi only place yourself inside app folder and use:
"uvicorn main:app --reload"
uou might need to do pip install uvicorn
