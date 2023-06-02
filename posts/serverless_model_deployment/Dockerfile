FROM public.ecr.aws/lambda/python:3.9.2023.03.15.15-x86_64 

# Install the requirements.txt
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY predict_sklearn.py ${LAMBDA_TASK_ROOT}

# Copy model pickle (alternatively, upload it to S3)
COPY model.pickle ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "predict_sklearn.predict" ]