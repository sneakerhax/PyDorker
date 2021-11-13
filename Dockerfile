FROM python:3

RUN apt update && apt upgrade -y
RUN git clone https://github.com/sneakerhax/PyDorker.git
WORKDIR /PyDorker
RUN python -m pip install -r requirements.txt


ENTRYPOINT [ "python", "PyDorker.py" ]