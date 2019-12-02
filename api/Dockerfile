FROM continuumio/miniconda:4.3.27

# RUN sed -i '/jessie-updates/d' /etc/apt/sources.list
# RUN apt-get update && apt-get -y install gcc

WORKDIR /opt/frp-sscce/
COPY environment.yml .
RUN conda env create

COPY . .

EXPOSE 5000

CMD /bin/bash -c "source activate frp-sscce && pip install -e . && flask run -h 0.0.0.0"
