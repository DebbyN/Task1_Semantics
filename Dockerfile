#Dockerfile
#L3T12_Task1 Symantic Similarities

#Load different python interpreter
FROM pypy:latest

#Working directory for image 
WORKDIR /app

#Copies the requirements.txt from the computer where created to the image
COPY requirements.txt requirements.txt

# Installs the requirements specified in the requirements file
RUN pip3 install -r requirements.txt

#Copy all files from local directory
COPY . /app

#Run the code
#Samples of similarity tests
CMD python semantic.py

#Comparison between simple language model and advanced language model
#simple
CMD python example2.py
#advanced
CMD python example.py 

