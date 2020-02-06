FROM python:3
COPY . /reg
WORKDIR reg
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "registration.py"]
