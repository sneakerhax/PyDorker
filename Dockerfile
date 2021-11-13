FROM python:3

RUN apt update && apt upgrade -y
RUN git clone https://github.com/sneakerhax/PyDorker.git
RUN python -m pip install -r requirements.txt
WORKDIR /PyDorker

ENTRYPOINT [ "python", "PyDorker.py" ]