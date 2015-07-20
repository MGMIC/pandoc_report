FROM python:2.7-onbuild

RUN apt-get update && apt-get install -y vim pandoc

#RUN apt-get install -y texlive-full

ENV PATH $PATH:/usr/src/app/bin

#CMD ["make_report"]
